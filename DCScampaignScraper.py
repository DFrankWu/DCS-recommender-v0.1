import requests
from bs4 import BeautifulSoup
import pandas as pd

baseurl='https://www.digitalcombatsimulator.com'

headers = {
           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
           }

productlinks = []

for x in range(1,7):
    r = requests.get(f'https://www.digitalcombatsimulator.com/en/shop/campaigns/?PAGEN_1={x}')
    soup = BeautifulSoup(r.content, 'html.parser')
    productlist = soup.find_all('h2')
    
    for item in productlist:
        for link in item.find_all('a', href=True):
            productlinks.append(baseurl + link['href'])
            
print(len(productlinks))
## Test Complete

# testlink = 'https://www.digitalcombatsimulator.com/en/shop/campaigns/fa-18c_rising_squall_campaign/'

dcs_campaign_list = []

for link in productlinks:
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')   

    # Parse product name
    name = soup.find('h1').text.strip()

    # Parse product description (Joined string form)
    description = []
    for item in soup.find_all('p')[1:]:
        container = item.text.strip()
        if 'Localization' in container:
            break
        description.append(container)

    description = ' '.join(description)


    #Parse product advertised features (Joined string form)
    key_features = []
    for key in soup.find_all('div', class_='col-xs-9 col-sm-6'):
        ulList = key.find_all('li')
        for li in ulList:
            key_features.append(li.text.strip())      
    
    # Extract model requirements from the list (end of the key_features list that contains 'DCS')
    module_requirements = [i for i in key_features if 'DCS' in i]
    # Keep real key_features in list and redefine
    key_features = [i for i in key_features if 'DCS' not in i]    

    # Parse localization of the module, spliting over voiceovers and subtitles
    # Some campaigns are too old that its localization info is not properly displaying, thus some error handling here
    try:
        localization_vo = soup.find_all('td')[1].text.strip()
        localization_text = soup.find_all('td')[3].text.strip()
    except:
        for item in soup.find_all('p')[1:]:
            container = item.text.strip()
            if 'Localization:' in container:
                localization_vo = container.replace('Localization:', '').strip()
                localization_text = container.replace('Localization:', '').strip()

        
    dcs_campaign = {
            'name': name,
            'description': description,
            'key_features': key_features,
            'module_requirements': module_requirements,
            'voice_over_loc': localization_vo,
            'subtitle_loc': localization_text
    }
    dcs_campaign_list.append(dcs_campaign)
    print('Saving: ', dcs_campaign['name'])



df = pd.DataFrame(dcs_campaign_list)
df.to_csv('dcs_campaign_data.csv')
    
print('\n All data parsing complete, CSV file saved') 

#     print(f'CAMPAIGN NAME: {name} \n')
#     print(f'PRODUCT DESCRIPTION: {description} \n')
#     print(f'KEY FEATURES: {key_features} \n')
#     print(f'MODULE REQUIREMENTS: {module_requirements} \n')
#     print(f'VOICE OVER: {localization_vo} \n')
#     print(f'SUBTITLE: {localization_text} \n')