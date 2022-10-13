import time
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer
from sklearn.metrics.pairwise import cosine_similarity


class DCSRecommender:
    '''
    This is a experimental non-commercial project by Donghang WU
        - The project intend to recommend relevant campaigns to players using
        the PorterStemmer NLP algorithm as a content-based processor
        
        - GUI and other front-end application will be added for UX and first stage implementation
        - Collaborative filtering may be added if data becomes available
    
    
    
    The recommender takes in 1 dataset argument
    
    **dataset must be prepared for nltk,
    all features must been concatenated in 'tags' column form and lowercased
    
    There are two functions currently available:
    
    - choose_campaign: allow user to choose desired campaign from list 
    
    - *recommend: recommend campaign using user choice or direct input 
      (input must be exact excluding "DCS:" from the title)
    
    PACKAGE REQUIREMENTS:
        import pandas as pd
        import time
        from sklearn.feature_extraction.text import CountVectorizer
        from nltk.stem.porter import PorterStemmer
        from sklearn.metrics.pairwise import cosine_similarity
    
    
    *make sure to run **df['tags'] = df['tags'].apply(rec.stem)** before running the recommend method
    **temporary
    '''
    def __init__(self, dataset):
        self.dataset = dataset
        self.campaign_dict = {'ww2': ['Mosquito FB VI', 'P-47D', 'Fw 190', 'I-16','Yak-52','Spitfire','Bf 109','P-51'], 'coldwar': ['F-86F', 'Mirage F1','Mi-24P', 'MiG-19','AJS-37','MiG-15','MiG-21'], 'modern': ['Su-25','F-15C','Su-33','Su-27','Black Shark','Combined Arms','UH-1','Mi-8','AH-64D','A-10C','JF-17','F-16C','MiG-29','F-14','F/A-18C','AV-8','F-5E','SA342','M-2000C','L-39','C-101']}
        self.choice = ''
        self.mask_all = dataset.name.str.contains('|'.join(self.campaign_dict['modern']+self.campaign_dict['coldwar']+self.campaign_dict['ww2']))
        self.mask_ww2 = dataset.name.str.contains('|'.join(self.campaign_dict['ww2']))
        self.mask_coldwar = dataset.name.str.contains('|'.join(self.campaign_dict['coldwar']))
        self.mask_modern = dataset.name.str.contains('|'.join(self.campaign_dict['modern']))
        self.ww2_campaigns = dataset.name[self.mask_ww2].sort_values()
        self.coldwar_campaigns = dataset.name[self.mask_coldwar].sort_values()
        self.modern_campaigns = dataset.name[self.mask_modern].sort_values()
        self.other_campaigns = dataset.name[~self.mask_all].sort_values()
        self.ps = PorterStemmer()
        print('------ Welcome to the DCS Campaign Recommender! ------ \n You can use "choose_campaign" method to choose an campaign from our list \n Already knew what you own/want? \n Try using "recommend" method and input exact campaign name as argument \n Our mighty R2D2 will recommend some campaigns for you to purchase in the future!')
    def choose_campaign(self, module_kind=''):
#         print('Please choose module kind(plane, campaign, map):')
#         module_kind = input()
#         while module_kind not in ['plane', 'campaign', 'map']:
#             print('Please enter valid kind!')
#         print(f'You have chosen {module_kind}')
#          time.sleep(5)
        print('Is there a particular airframe era you are looking for?')
        yes_no = ''
        while yes_no.lower() != 'yes' or yes_no.lower() != 'no':
            print('Please enter "yes" or "no"!')
            yes_no = input()
            if yes_no.lower() == 'yes' or yes_no.lower() == 'no':
                if yes_no.lower() == 'yes':
                    print('What is the airframe era (ww2, coldwar, modern, other)?')
                    era_choice = input()
                    n_era = 3
                    n = 3
                    while era_choice not in ['ww2', 'coldwar', 'modern', 'other']:
                        if n_era == 0:
                            return 'We are unable to find the time era, please try again!'
                        print(f'You have {n_era} chances left')
                        print('Please enter a valid kind!')
                        n_era -= 1
                        era_choice = input()
                    if era_choice == 'ww2':
                        print('This is the list of World War II campaigns')
                        print(self.ww2_campaigns)
                        time.sleep(5)
                        print('Please make your choice:')
                        self.choice = input()
                        while self.ww2_campaigns.str.contains(self.choice) is False :
                            if n == 0:
                                return 'We are unable to find the campaign, please try again!'
                            print(f'You have {n} chances left')
                            print('Please enter a valid kind!')
                            n -= 1
                            self.choice = input()
                        print(f'You have chosen {self.choice}, \n that is a great choice!')
                        break
                    elif era_choice == 'coldwar':
                        print('This is the list of Cold War campaigns')
                        print(self.coldwar_campaigns)
                        time.sleep(5)
                        print('Please make your choice:')
                        self.choice = input()
                        while self.coldwar_campaigns.str.contains(self.choice) is False :
                            if n == 0:
                                return 'We are unable to find the campaign, please try again!'
                            print(f'You have {n} chances left')
                            print('Please enter a valid kind!')
                            n -= 1
                            self.choice = input()
                        print(f'You have chosen {self.choice}, \n that is a great choice!')
                        break
                    elif era_choice == 'modern':
                        print('This is the list of Modern campaigns')
                        print(self.modern_campaigns)
                        time.sleep(5)
                        print('Please make your choice:')
                        self.choice = input()
                        while self.modern_campaigns.str.contains(self.choice) is False :
                            if n == 0:
                                return 'We are unable to find the campaign, please try again!'
                            print(f'You have {n} chances left')
                            print('Please enter a valid kind!')
                            n -= 1
                            self.choice = input()
                        print(f'You have chosen {self.choice},\n that is a great choice!')
                        break
                    elif era_choice == 'other':
                        print('This is the list of other campaigns that has no module name')
                        print(self.other_campaigns)
                        time.sleep(5)
                        print('Please make your choice:')
                        self.choice = input()
                        while self.other_campaigns.str.contains(self.choice) is False :
                            if n == 0:
                                return 'We are unable to find the campaign, please try again!'
                            print(f'You have {n} chances left')
                            print('Please enter a valid kind!')
                            n -= 1
                            self.choice = input()
                        print(f'You have chosen {self.choice},\n that is a great choice!')
                        break
                elif yes_no.lower() =='no':
                    print('OK, \n This is the list of all campaigns')
                    print(self.dataset.name.sort_values())
                    time.sleep(5)
                    print('Please make your choice:')
                    self.choice = input()
                    while self.other_campaigns.str.contains(self.choice) is False :
                        if n == 0:
                            return 'We are unable to find the campaign, please try again!'
                        print(f'You have {n} chances left')
                        print('Please enter a valid kind!')
                        n -= 1
                        self.choice = input()
                    print(f'You have chosen {self.choice},\n that is a great choice!')
                    break
            ## Include vectorizer, cosine similarity
    def stem(self, text):
        y=[]
        for i in text.split():
            y.append(self.ps.stem(i))
        return ' '.join(y)
    def recommend(self, campaign_name=''):
        cv = CountVectorizer(max_features=5000, stop_words='english')
        vectors = cv.fit_transform(self.dataset['tags']).toarray()
        similarity = cosine_similarity(vectors)
        if self.choice is None or len(campaign_name) > 0:
            self.choice = campaign_name
            campaign_name = self.choice
        elif self.choice is not None and len(campaign_name) == 0:
            campaign_name = self.choice
        try:
            campaign_index = self.dataset[self.dataset['name'] == campaign_name].index[0]
        except IndexError as error:
            print('You have not made the choice yet!')
        distances = similarity[campaign_index]
        campaign_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]
        print('Based on your choice, we also recommend the following campaign')
        for i in campaign_list:
            print(self.dataset.iloc[i[0]]['name'])
            time.sleep(0.5)