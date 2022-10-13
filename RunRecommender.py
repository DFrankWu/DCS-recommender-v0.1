from dcs_recommender import DCSRecommender
import pandas as pd

campaign_data_model = pd.read_csv('dcs_campaign_data_tagged.csv')
rec = DCSRecommender(campaign_data_model)
campaign_data_model['tags'] = campaign_data_model['tags'].apply(rec.stem)
