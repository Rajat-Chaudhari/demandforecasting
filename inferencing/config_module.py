#!/usr/bin/env python
# coding: utf-8

# In[3]:


import json
from datetime import datetime
#Create dictionary for configuration
dictionary_config = {
    "bucket": "s3-dx-tdem-ie-nonprod-persist",
    "bucket_new": "s3-dx-tdem-ie-nonprod-curated",
    "model_training_date":"20240826",
    "model_forecasting_date": "20240826",
    "primary_path": "persist-bo/persist-bo-demand-forecast",
    "tpcap_model": "tpcap-models",
    "model_output_folder_name": "model-training-output",
    "prefix_cleaned_training_file_path": "persist-bo/persist-bo-demand-forecast/cleaned-training-data/",
    "prefix_bestfit_file": "curated-bo/curated-bo-demand-forecast/bestfit-selected-models/",
    "prefix_monthly_parquet": "persist-bo/persist-bo-demand-forecast/input-data/monthly-demand-data",
    "prefix_daily_dom_parquet":"persist-bo/persist-bo-demand-forecast/input-data/domestic-daily-data",
    "prefix_daily_exp_parquet":"persist-bo/persist-bo-demand-forecast/input-data/export-daily-data",
    "part_list_file_path":"persist-bo/persist-bo-demand-forecast/to-be-removed/test_data/part_list_file.xlsx",
    "file_name_bestfit": "bestfit_selected_models_historic_months_",
    "file_name_bestfit_powerbi": "bestfit_selected_models_historic_months_powerbi_",
    "prophet_config_filename": "train_prophet_config_",
    "cleaned_training_filename_prefix": "clean_data_imputed_",
    "file_name_train_ridge_prefix": "train_ridge_forecast_",
    "file_name_train_lasso_prefix": "train_lasso_forecast_",
    "file_name_train_xgboost_prefix": "train_xgboost_forecast_",
    "prefix_inp": "persist-bo/persist-bo-demand-forecast/master_data/job3/etljob3input",
    "ridge_forecast_file_name": "ridge_forecast_data_",
    "lasso_forecast_file_name": "lasso_forecast_data_",
    "xgb_forecast_file_name": "xgb_forecast_data_",
    "prefix_model_output_forecast_path": "persist-bo/persist-bo-demand-forecast/model-forecasted-output",
    "file_name_prophet_train": "train_prophet_forecast_",
    "filename_bestfit_prophet_config": "train_prophet_config_",
    "prophet_forecast_file_name": "prophet_forecast_data_",
    "file_name_training_lstm": "train_lstm_forecast_",
    "lstm_forecast_file_name": "lstm_forecast_data_",
    "inp_path_forecast": "persist-bo/persist-bo-demand-forecast/model-forecasted-output/",
    "best_file_base_name_powerbi": "bestfit_selected_models_historic_months_powerbi_",
    "prefix_forecast_file": "curated-bo/curated-bo-demand-forecast/selected-models-forecasted-output/",
    "file_name_bestfit_forecast": "forecast_selected_models_future_months_",
    "filename_forecast_powerbi": "forecast_selected_models_future_months_powerbi_",
    "arima_bestfit_config_file_name": "arima_bestfit_config_",
    "arima_train_data_file_name": "arima_train_",
    "arima_forecasted_file_name": "arima_forecasted_data_",
    "final_file_with_history_name": "final_model_outcome_with_history_",
    "final_file_path_prefix": "curated-bo/curated-bo-demand-forecast/curated-model-outcome",
    "final_file_name": "final_model_outcome_",
    "prefix_gtmaster" : 'curated-common/curated-common-dpv/curated_dpv_dvjo0202',
    "prefix_proc" : 'curated-common/curated-common-dpv/curated_dpv_dvjo0302',
    "prefix_pic_master_path" : "curated-bo/curated-bo-manual/curated_pic_master",
    "product_master_path_prefix" : 'curated-bo/curated-bo-demand-forecast/product-group-master/Product_Group_Master.xlsx'
}
# In[4]:


#Convert dictionary to JSON & save it to a config file
# with open('config.json', 'w') as json_file:
#     json.dump(dictionary_config, json_file, indent=4)


# In[5]:


#Create a new file named config_module.py:
import json

class Config:
    def __init__(self, file_path='config.json'):
        self.config = self._read_config(file_path)

    def _read_config(self, file_path):
        with open(file_path, 'r') as json_file:
            return json.load(json_file)

    def get_value(self, key_name):
        if key_name in self.config:
            return self.config[key_name]
        else:
            raise ValueError(f"Key '{key_name}' not found in the configuration")


# In[ ]:


# from config_module import Config
# config = Config()


# In[1]:


#In other notebooks usage: 
#from config_module import Config
#config = Config()
#bucket_name = config.get_value('bucket')
#prefix_output_lstm = config.get_prefix_output_lstm()

