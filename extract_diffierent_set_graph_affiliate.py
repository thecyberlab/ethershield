from pickle import FALSE
from tokenize import Double
import numpy as np
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from DataGlitch.dtype_detector import find_numeric
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn import model_selection
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
import xgboost as xgb
import lightgbm as lgb
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from matplotlib import pyplot
from xgboost import plot_importance
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_validate
from sklearn.metrics import make_scorer

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import KFold,StratifiedKFold
from numpy import *
from sklearn.model_selection import StratifiedShuffleSplit

import numpy as np
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn import model_selection
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
import xgboost as xgb
import lightgbm as lgb
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from matplotlib import pyplot
from xgboost import plot_importance
from lightgbm import plot_importance
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_validate
from sklearn.metrics import make_scorer

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import KFold,StratifiedKFold
from numpy import *
from sklearn.model_selection import StratifiedShuffleSplit

without_time_list = ['average_time_between_incoming_transactions_normal', 'average_time_between_outcoming_transactions_normal',
                    'time_since_the_first_until_the_last_transaction_normal', 'longest_interval_between_two_transactions_normal',
                    'shortest_interval_between_two_transactions_normal', 'total_number_of_transactions_normal',
                    'the_number_of_unique_outcoming_addresses_normal', 'the_number_of_unique_incoming_addresses_normal',
                    'the_total_number_of_incoming_transactions_normal', 'the_total_number_of_outcoming_transactions_normal',
                    'the_proportion_of_unique_outcoming_address_transactions_normal','the_proportion_of_unique_incoming_address_transactions_normal',
                    'proportion_of_outcoming_address_transactions_normal', 'proportion_of_incoming_address_transactions_normal',
                    'minimum_value_in_Ether_ever_received_normal', 'maximum_value_in_Ether_ever_received_normal',
                    'avg_value_in_Ether_ever_received_normal', 'minimum_value_in_Ether_ever_sent_normal',
                    'maximum_value_in_Ether_ever_sent_normal', 'avg_value_in_Ether_ever_sent_normal',
                    'total_value_in_Ether_ever_received_normal', 'total_value_in_Ether_ever_sent_normal',
                    'the_number_of_transactions_per_day_normal', 'the_number_of_incoming_transactions_per_day_normal',
                    'the_number_of_outcoming_transactions_per_day_normal', 'the_number_of_incoming_transactions_per_hour_normal',
                    'the_number_of_outcoming_transactions_per_hour_normal', 'the_number_of_incoming_amounts_per_day_normal',
                    'the_number_of_outcoming_amounts_per_day_normal', 'the_total_number_of_amounts_outcoming_plus_incoming_normal',
                    'the_number_of_incoming_amounts_per_hour_normal', 'the_number_of_outcoming_amounts_per_hour_normal',
                    'the_number_of_transactions_per_hour_normal', 'the_number_of_amounts_per_day_normal',
                    'the_number_of_amounts_per_hour_normal', 'reverted_numbers_normal',

                    'average_time_between_incoming_transactions_internal', 'average_time_between_outcoming_transactions_internal',
                    'time_since_the_first_until_the_last_transaction_internal', 'longest_interval_between_two_transactions_internal',
                    'shortest_interval_between_two_transactions_internal', 'total_number_of_transactions_internal',
                    'the_number_of_unique_outcoming_addresses_internal', 'the_number_of_unique_incoming_addresses_internal',
                    'the_total_number_of_incoming_transactions_internal', 'the_total_number_of_outcoming_transactions_internal',
                    'the_proportion_of_unique_outcoming_address_transactions_internal','the_proportion_of_unique_incoming_address_transactions_internal',
                    'proportion_of_outcoming_address_transactions_internal', 'proportion_of_incoming_address_transactions_internal',
                    'minimum_value_in_Ether_ever_received_internal', 'maximum_value_in_Ether_ever_received_internal',
                    'avg_value_in_Ether_ever_received_internal', 'minimum_value_in_Ether_ever_sent_internal',
                    'maximum_value_in_Ether_ever_sent_internal', 'avg_value_in_Ether_ever_sent_internal',
                    'total_value_in_Ether_ever_received_internal', 'total_value_in_Ether_ever_sent_internal',
                    'the_number_of_transactions_per_day_internal', 'the_number_of_incoming_transactions_per_day_internal',
                    'the_number_of_outcoming_transactions_per_day_internal', 'the_number_of_incoming_transactions_per_hour_internal',
                    'the_number_of_outcoming_transactions_per_hour_internal', 'the_number_of_incoming_amounts_per_day_internal',
                    'the_number_of_outcoming_amounts_per_day_internal', 'the_total_number_of_amounts_outcoming_plus_incoming_internal',
                    'the_number_of_incoming_amounts_per_hour_internal', 'the_number_of_outcoming_amounts_per_hour_internal',
                    'the_number_of_transactions_per_hour_internal', 'the_number_of_amounts_per_day_internal',
                    'the_number_of_amounts_per_hour_internal', 'reverted_numbers_internal',

                    'average_time_between_incoming_transactions_erc20', 'average_time_between_outcoming_transactions_erc20',
                    'time_since_the_first_until_the_last_transaction_erc20', 'longest_interval_between_two_transactions_erc20',
                    'shortest_interval_between_two_transactions_erc20', 'total_number_of_transactions_erc20',
                    'the_number_of_unique_outcoming_addresses_erc20', 'the_number_of_unique_incoming_addresses_erc20',
                    'the_total_number_of_incoming_transactions_erc20', 'the_total_number_of_outcoming_transactions_erc20',
                    'the_proportion_of_unique_outcoming_address_transactions_erc20','the_proportion_of_unique_incoming_address_transactions_erc20',
                    'proportion_of_outcoming_address_transactions_erc20', 'proportion_of_incoming_address_transactions_erc20',
                    'minimum_value_in_Ether_ever_received_erc20', 'maximum_value_in_Ether_ever_received_erc20',
                    'avg_value_in_Ether_ever_received_erc20', 'minimum_value_in_Ether_ever_sent_erc20',
                    'maximum_value_in_Ether_ever_sent_erc20', 'avg_value_in_Ether_ever_sent_erc20',
                    'total_value_in_Ether_ever_received_erc20', 'total_value_in_Ether_ever_sent_erc20',
                    'the_number_of_transactions_per_day_erc20', 'the_number_of_incoming_transactions_per_day_erc20',
                    'the_number_of_outcoming_transactions_per_day_erc20', 'the_number_of_incoming_transactions_per_hour_erc20',
                    'the_number_of_outcoming_transactions_per_hour_erc20', 'the_number_of_incoming_amounts_per_day_erc20',
                    'the_number_of_outcoming_amounts_per_day_erc20', 'the_total_number_of_amounts_outcoming_plus_incoming_erc20',
                    'the_number_of_incoming_amounts_per_hour_erc20', 'the_number_of_outcoming_amounts_per_hour_erc20',
                    'the_number_of_transactions_per_hour_erc20', 'the_number_of_amounts_per_day_erc20',
                    'the_number_of_amounts_per_hour_erc20',

                    'average_time_between_incoming_transactions_nft', 'average_time_between_outcoming_transactions_nft',
                    'time_since_the_first_until_the_last_transaction_nft', 'longest_interval_between_two_transactions_nft',
                    'shortest_interval_between_two_transactions_nft', 'total_number_of_transactions_nft',
                    'the_number_of_unique_outcoming_addresses_nft', 'the_number_of_unique_incoming_addresses_nft',
                    'the_total_number_of_incoming_transactions_nft', 'the_total_number_of_outcoming_transactions_nft',
                    'the_proportion_of_unique_outcoming_address_transactions_nft', 'the_proportion_of_unique_incoming_address_transactions_nft',
                    'proportion_of_outcoming_address_transactions_nft', 'proportion_of_incoming_address_transactions_nft',
                    'minimum_value_in_Ether_ever_received_nft', 'maximum_value_in_Ether_ever_received_nft',
                    'avg_value_in_Ether_ever_received_nft', 'minimum_value_in_Ether_ever_sent_nft',
                    'maximum_value_in_Ether_ever_sent_nft', 'avg_value_in_Ether_ever_sent_nft',
                    'total_value_in_Ether_ever_received_nft', 'total_value_in_Ether_ever_sent_nft',
                    'the_number_of_transactions_per_day_nft', 'the_number_of_incoming_transactions_per_day_nft',
                    'the_number_of_outcoming_transactions_per_day_nft', 'the_number_of_incoming_transactions_per_hour_nft',
                    'the_number_of_outcoming_transactions_per_hour_nft', 'the_number_of_incoming_amounts_per_day_nft',
                    'the_number_of_outcoming_amounts_per_day_nft', 'the_total_number_of_amounts_outcoming_plus_incoming_nft',
                    'the_number_of_incoming_amounts_per_hour_nft', 'the_number_of_outcoming_amounts_per_hour_nft',
                    'the_number_of_transactions_per_hour_nft', 'the_number_of_amounts_per_day_nft',
                    'the_number_of_amounts_per_hour_nft',

                    'average_time_between_incoming_transactions_erc1155','average_time_between_outcoming_transactions_erc1155',
                    'time_since_the_first_until_the_last_transaction_erc1155', 'longest_interval_between_two_transactions_erc1155',
                    'shortest_interval_between_two_transactions_erc1155', 'total_number_of_transactions_erc1155',
                    'the_number_of_unique_outcoming_addresses_erc1155', 'the_number_of_unique_incoming_addresses_erc1155',
                    'the_total_number_of_incoming_transactions_erc1155', 'the_total_number_of_outcoming_transactions_erc1155',
                    'the_proportion_of_unique_outcoming_address_transactions_erc1155', 'the_proportion_of_unique_incoming_address_transactions_erc1155',
                    'proportion_of_outcoming_address_transactions_erc1155', 'proportion_of_incoming_address_transactions_erc1155',
                    'minimum_value_in_Ether_ever_received_erc1155', 'maximum_value_in_Ether_ever_received_erc1155',
                    'avg_value_in_Ether_ever_received_erc1155', 'minimum_value_in_Ether_ever_sent_erc1155',
                    'maximum_value_in_Ether_ever_sent_erc1155', 'avg_value_in_Ether_ever_sent_erc1155',
                    'total_value_in_Ether_ever_received_erc1155', 'total_value_in_Ether_ever_sent_erc1155',
                    'the_number_of_transactions_per_day_erc1155', 'the_number_of_incoming_transactions_per_day_erc1155',
                    'the_number_of_outcoming_transactions_per_day_erc1155', 'the_number_of_incoming_transactions_per_hour_erc1155',
                    'the_number_of_outcoming_transactions_per_hour_erc1155', 'the_number_of_incoming_amounts_per_day_erc1155',
                    'the_number_of_outcoming_amounts_per_day_erc1155', 'the_total_number_of_amounts_outcoming_plus_incoming_erc1155',
                    'the_number_of_incoming_amounts_per_hour_erc1155', 'the_number_of_outcoming_amounts_per_hour_erc1155',
                    'the_number_of_transactions_per_hour_erc1155', 'the_number_of_amounts_per_day_erc1155',
                    'the_number_of_amounts_per_hour_erc1155',

                    'average_time_between_incoming_transactions_all', 'average_time_between_outcoming_transactions_all',
                    'time_since_the_first_until_the_last_transaction_all', 'longest_interval_between_two_transactions_all',
                    'shortest_interval_between_two_transactions_all', 'total_number_of_transactions_all',
                    'the_number_of_unique_outcoming_addresses_all', 'the_number_of_unique_incoming_addresses_all',
                    'the_total_number_of_incoming_transactions_all', 'the_total_number_of_outcoming_transactions_all',
                    'the_proportion_of_unique_outcoming_address_transactions_all','the_proportion_of_unique_incoming_address_transactions_all',
                    'proportion_of_outcoming_address_transactions_all', 'proportion_of_incoming_address_transactions_all',
                    'minimum_value_in_Ether_ever_received_all', 'maximum_value_in_Ether_ever_received_all',
                    'avg_value_in_Ether_ever_received_all', 'minimum_value_in_Ether_ever_sent_all',
                    'maximum_value_in_Ether_ever_sent_all', 'avg_value_in_Ether_ever_sent_all',
                    'total_value_in_Ether_ever_received_all', 'total_value_in_Ether_ever_sent_all',
                    'the_number_of_transactions_per_day_all', 'the_number_of_incoming_transactions_per_day_all',
                    'the_number_of_outcoming_transactions_per_day_all', 'the_number_of_incoming_transactions_per_hour_all',
                    'the_number_of_outcoming_transactions_per_hour_all', 'the_number_of_incoming_amounts_per_day_all',
                    'the_number_of_outcoming_amounts_per_day_all', 'the_total_number_of_amounts_outcoming_plus_incoming_all',
                    'the_number_of_incoming_amounts_per_hour_all', 'the_number_of_outcoming_amounts_per_hour_all',
                    'the_number_of_transactions_per_hour_all', 'the_number_of_amounts_per_day_all',
                    'the_number_of_amounts_per_hour_all', 'reverted_numbers_all',

                    'the_propotion_of_normal_transactions_of_all', 'the_propotion_of_normal_incoming_transactions_of_all',
                    'the_propotion_of_normal_incoming_transactions_of_all_transactions', 'the_propotion_of_normal_outcoming_transactions_of_all',
                    'the_propotion_of_normal_outcoming_transactions_of_all_transactions', 
                    
                    'the_propotion_of_internal_transactions_of_all', 'the_propotion_of_internal_incoming_transactions_of_all',
                    'the_propotion_of_internal_incoming_transactions_of_all_transactions', 'the_propotion_of_internal_outcoming_transactions_of_all',
                    'the_propotion_of_internal_outcoming_transactions_of_all_transactions',
                    
                    'the_propotion_of_erc20_transactions_of_all','the_propotion_of_erc20_incoming_transactions_of_all',
                    'the_propotion_of_erc20_incoming_transactions_of_all_transactions', 'the_propotion_of_erc20_outcoming_transactions_of_all',
                    'the_propotion_of_erc20_outcoming_transactions_of_all_transactions',
                    
                    'the_propotion_of_nft_transactions_of_all', 'the_propotion_of_nft_incoming_transactions_of_all',
                    'the_propotion_of_nft_incoming_transactions_of_all_transactions', 'the_propotion_of_nft_outcoming_transactions_of_all',
                    'the_propotion_of_nft_outcoming_transactions_of_all_transactions',
                    
                    'the_propotion_of_erc1155_transactions_of_all', 'the_propotion_of_erc1155_incoming_transactions_of_all',
                    'the_propotion_of_erc1155_incoming_transactions_of_all_transactions', 'the_propotion_of_erc1155_outcoming_transactions_of_all',
                    'the_propotion_of_erc1155_outcoming_transactions_of_all_transactions',

                    'the_propotion_of_normal_ether_transfered_of_all', 'the_propotion_of_normal_ether_sent_of_all_sent',
                    'the_propotion_of_normal_ether_sent_of_all_touched', 'the_propotion_of_normal_ether_received_of_all_sent',
                    'the_propotion_of_normal_ether_received_of_all_touched',

                    'the_propotion_of_internal_ether_transfered_of_all','the_propotion_of_internal_ether_sent_of_all_sent',
                    'the_propotion_of_internal_ether_sent_of_all_touched','the_propotion_of_internal_ether_received_of_all_sent',
                    'the_propotion_of_internal_ether_received_of_all_touched',

                    'the_propotion_of_erc20_ether_transfered_of_all', 'the_propotion_of_erc20_ether_sent_of_all_sent',
                    'the_propotion_of_erc20_ether_sent_of_all_touched', 'the_propotion_of_erc20_ether_received_of_all_sent',
                    'the_propotion_of_erc20_ether_received_of_all_touched',
                    
                    'the_propotion_of_nft_ether_transfered_of_all', 'the_propotion_of_nft_ether_sent_of_all_sent',
                    'the_propotion_of_nft_ether_sent_of_all_touched', 'the_propotion_of_nft_ether_received_of_all_sent',
                    'the_propotion_of_nft_ether_received_of_all_touched',
                    
                    'the_propotion_of_erc1155_ether_transfered_of_all', 'the_propotion_of_erc1155_ether_sent_of_all_sent',
                    'the_propotion_of_erc1155_ether_sent_of_all_touched', 'the_propotion_of_erc1155_ether_received_of_all_sent',
                    'the_propotion_of_erc1155_ether_received_of_all_touched',
                    'only_incoming_result', 'only_outcoming_result',
                    'get_maximum_number_for_same_incoming_address_result', 'get_maximum_number_for_same_outcoming_address_result',
                    'get_maximum_number_for_same_touched_address_result', 'get_minimum_number_for_same_incoming_address_result',
                    'get_minimum_number_for_same_outcoming_address_result', 'get_minimum_number_for_same_touched_address_result',
                    'how_many_address_with_a_single_transaction_for_incoming_result', 'how_many_address_with_a_single_transaction_for_outcoming_result',
                    'how_many_address_with_a_single_transaction_for_all_result' , 'incoming_address_with_a_single_transaction_out_of_all_unique_incoming_addresses_result',
                    'incoming_address_with_a_single_transaction_out_of_all_unique_addresses_result', 'outcoming_address_with_a_single_transaction_out_of_all_unique_outcoming_addresses_result',
                    'outcoming_address_with_a_single_transaction_out_of_all_unique_addresses_result', 'all_address_with_a_single_transaction_out_of_all_unique_addresses_result',
                    'the_maximum_repeated_Ether_value_in_incoming_amount_result', 'the_minimum_repeated_Ether_value_in_incoming_amount_result',
                    'the_maximum_repeated_Ether_value_in_outcoming_amount_result', 'the_minimum_repeated_Ether_value_in_outcoming_amount_result',
                    'the_maximum_repeated_Ether_value_in_all_amount_result', 'the_minimum_repeated_Ether_value_in_all_amount_result',
                    'the_maximum_repeated_Ether_value_in_incoming_times_result', 'the_minimum_repeated_Ether_value_in_incoming_times_result',
                    'the_maximum_repeated_Ether_value_in_outcoming_times_result', 'the_minimum_repeated_Ether_value_in_outcoming_times_result',
                    'the_maximum_repeated_Ether_value_in_all_times_result', 'the_minimum_repeated_Ether_value_in_all_times_result']


first_csv = 'set3_malicious_be.csv'
second_csv = 'set1_malicious_be.csv'
accuracy_xgboost_binary_all_31 = []
time_list = [' (1hours)', ' (3hours)', ' (6hours)', ' (12hours)', ' (1.0days)', ' (3.0days)', ' (7.0days)', ' (14.0days)', ' (30.0days)', ' (90.0days)', ' (180.0days)', ' (365.0days)', ' (1095.0days)', ' (1825.0days)', ' (3650.0days)']
for time in time_list:
    with_time_list = []
    temp_str = ''
    for each_str in without_time_list:
        temp_str = each_str + time
        with_time_list.append(temp_str)
    dtype_dict = {}
    for each_feature in with_time_list:
        dtype_dict[each_feature] = float

    df = pd.read_csv(first_csv, dtype=dtype_dict)
    # for column in df.columns:
    #     print(column,':',pd.api.types.infer_dtype(df[column]))
    # print(df)
    # for column in df.columns:
    #     with open('test.txt', 'a') as newfile:
    #         newfile.write(pd.api.types.infer_dtype(df['minimum_value_in_Ether_ever_received_normal (14600.0days)']) + '\n')

    status_dict=df['category'].unique().tolist()
    df['transformed']=df['category'].apply(lambda x:status_dict.index(x))
    new_df = df.drop(['category'], axis=1)
    features = df[with_time_list]
    feature_label = df['transformed']

    f_train = features
    l_train = feature_label
    f_train = np.nan_to_num(f_train.astype(np.float32))
    l_train = np.nan_to_num(l_train.astype(np.float32))

    df = pd.read_csv(second_csv, dtype=dtype_dict)
    # for column in df.columns:
    #     print(column,':',pd.api.types.infer_dtype(df[column]))
    # print(df)
    # for column in df.columns:
    #     with open('test.txt', 'a') as newfile:
    #         newfile.write(pd.api.types.infer_dtype(df['minimum_value_in_Ether_ever_received_normal (14600.0days)']) + '\n')

    status_dict=df['category'].unique().tolist()
    df['transformed']=df['category'].apply(lambda x:status_dict.index(x))
    new_df = df.drop(['category'], axis=1)
    features = df[with_time_list]
    feature_label = df['transformed']

    f_test = features
    l_test = feature_label
    f_test = np.nan_to_num(f_test.astype(np.float32))
    l_test = np.nan_to_num(l_test.astype(np.float32))


    xgb_clf = xgb.XGBClassifier()
    xgb_clf.fit(f_train, l_train)
    l_predict = xgb_clf.predict(f_test)
    score = accuracy_score(l_test, l_predict)
    print(mean(score))
    accuracy_xgboost_binary_all_31.append(score)

with open('lastdance.txt', 'a') as newfile:
    newfile.write(first_csv + str(accuracy_xgboost_binary_all_31) + '\n')


first_csv = 'set3_malicious_be.csv'
second_csv = 'set2_malicious_be.csv'
accuracy_xgboost_binary_all_32 = []
time_list = [' (1hours)', ' (3hours)', ' (6hours)', ' (12hours)', ' (1.0days)', ' (3.0days)', ' (7.0days)', ' (14.0days)', ' (30.0days)', ' (90.0days)', ' (180.0days)', ' (365.0days)', ' (1095.0days)', ' (1825.0days)', ' (3650.0days)']
for time in time_list:
    with_time_list = []
    temp_str = ''
    for each_str in without_time_list:
        temp_str = each_str + time
        with_time_list.append(temp_str)
    dtype_dict = {}
    for each_feature in with_time_list:
        dtype_dict[each_feature] = float

    df = pd.read_csv(first_csv, dtype=dtype_dict)
    # for column in df.columns:
    #     print(column,':',pd.api.types.infer_dtype(df[column]))
    # print(df)
    # for column in df.columns:
    #     with open('test.txt', 'a') as newfile:
    #         newfile.write(pd.api.types.infer_dtype(df['minimum_value_in_Ether_ever_received_normal (14600.0days)']) + '\n')

    status_dict=df['category'].unique().tolist()
    df['transformed']=df['category'].apply(lambda x:status_dict.index(x))
    new_df = df.drop(['category'], axis=1)
    features = df[with_time_list]
    feature_label = df['transformed']

    f_train = features
    l_train = feature_label
    f_train = np.nan_to_num(f_train.astype(np.float32))
    l_train = np.nan_to_num(l_train.astype(np.float32))

    df = pd.read_csv(second_csv, dtype=dtype_dict)
    # for column in df.columns:
    #     print(column,':',pd.api.types.infer_dtype(df[column]))
    # print(df)
    # for column in df.columns:
    #     with open('test.txt', 'a') as newfile:
    #         newfile.write(pd.api.types.infer_dtype(df['minimum_value_in_Ether_ever_received_normal (14600.0days)']) + '\n')

    status_dict=df['category'].unique().tolist()
    df['transformed']=df['category'].apply(lambda x:status_dict.index(x))
    new_df = df.drop(['category'], axis=1)
    features = df[with_time_list]
    feature_label = df['transformed']

    f_test = features
    l_test = feature_label
    f_test = np.nan_to_num(f_test.astype(np.float32))
    l_test = np.nan_to_num(l_test.astype(np.float32))


    xgb_clf = xgb.XGBClassifier()
    xgb_clf.fit(f_train, l_train)
    l_predict = xgb_clf.predict(f_test)
    score = accuracy_score(l_test, l_predict)
    print(mean(score))
    accuracy_xgboost_binary_all_32.append(score)

with open('lastdance.txt', 'a') as newfile:
    newfile.write(first_csv + str(accuracy_xgboost_binary_all_32) + '\n')

first_csv = 'set3_malicious_be.csv'
second_csv = 'set4_malicious_be.csv'
accuracy_xgboost_binary_all_34 = []
time_list = [' (1hours)', ' (3hours)', ' (6hours)', ' (12hours)', ' (1.0days)', ' (3.0days)', ' (7.0days)', ' (14.0days)', ' (30.0days)', ' (90.0days)', ' (180.0days)', ' (365.0days)', ' (1095.0days)', ' (1825.0days)', ' (3650.0days)']
for time in time_list:
    with_time_list = []
    temp_str = ''
    for each_str in without_time_list:
        temp_str = each_str + time
        with_time_list.append(temp_str)
    dtype_dict = {}
    for each_feature in with_time_list:
        dtype_dict[each_feature] = float

    df = pd.read_csv(first_csv, dtype=dtype_dict)
    # for column in df.columns:
    #     print(column,':',pd.api.types.infer_dtype(df[column]))
    # print(df)
    # for column in df.columns:
    #     with open('test.txt', 'a') as newfile:
    #         newfile.write(pd.api.types.infer_dtype(df['minimum_value_in_Ether_ever_received_normal (14600.0days)']) + '\n')

    status_dict=df['category'].unique().tolist()
    df['transformed']=df['category'].apply(lambda x:status_dict.index(x))
    new_df = df.drop(['category'], axis=1)
    features = df[with_time_list]
    feature_label = df['transformed']

    f_train = features
    l_train = feature_label
    f_train = np.nan_to_num(f_train.astype(np.float32))
    l_train = np.nan_to_num(l_train.astype(np.float32))

    df = pd.read_csv(second_csv, dtype=dtype_dict)
    # for column in df.columns:
    #     print(column,':',pd.api.types.infer_dtype(df[column]))
    # print(df)
    # for column in df.columns:
    #     with open('test.txt', 'a') as newfile:
    #         newfile.write(pd.api.types.infer_dtype(df['minimum_value_in_Ether_ever_received_normal (14600.0days)']) + '\n')

    status_dict=df['category'].unique().tolist()
    df['transformed']=df['category'].apply(lambda x:status_dict.index(x))
    new_df = df.drop(['category'], axis=1)
    features = df[with_time_list]
    feature_label = df['transformed']

    f_test = features
    l_test = feature_label
    f_test = np.nan_to_num(f_test.astype(np.float32))
    l_test = np.nan_to_num(l_test.astype(np.float32))


    xgb_clf = xgb.XGBClassifier()
    xgb_clf.fit(f_train, l_train)
    l_predict = xgb_clf.predict(f_test)
    score = accuracy_score(l_test, l_predict)
    print(mean(score))
    accuracy_xgboost_binary_all_34.append(score)

with open('lastdance.txt', 'a') as newfile:
    newfile.write(first_csv + str(accuracy_xgboost_binary_all_34) + '\n')


first_csv = 'set1_malicious_be.csv'
second_csv = 'set2_malicious_be.csv'
accuracy_xgboost_binary_all_12 = []
time_list = [' (1hours)', ' (3hours)', ' (6hours)', ' (12hours)', ' (1.0days)', ' (3.0days)', ' (7.0days)', ' (14.0days)', ' (30.0days)', ' (90.0days)', ' (180.0days)', ' (365.0days)', ' (1095.0days)', ' (1825.0days)', ' (3650.0days)']
for time in time_list:
    with_time_list = []
    temp_str = ''
    for each_str in without_time_list:
        temp_str = each_str + time
        with_time_list.append(temp_str)
    dtype_dict = {}
    for each_feature in with_time_list:
        dtype_dict[each_feature] = float

    df = pd.read_csv(first_csv, dtype=dtype_dict)
    # for column in df.columns:
    #     print(column,':',pd.api.types.infer_dtype(df[column]))
    # print(df)
    # for column in df.columns:
    #     with open('test.txt', 'a') as newfile:
    #         newfile.write(pd.api.types.infer_dtype(df['minimum_value_in_Ether_ever_received_normal (14600.0days)']) + '\n')

    status_dict=df['category'].unique().tolist()
    df['transformed']=df['category'].apply(lambda x:status_dict.index(x))
    new_df = df.drop(['category'], axis=1)
    features = df[with_time_list]
    feature_label = df['transformed']

    f_train = features
    l_train = feature_label
    f_train = np.nan_to_num(f_train.astype(np.float32))
    l_train = np.nan_to_num(l_train.astype(np.float32))

    df = pd.read_csv(second_csv, dtype=dtype_dict)
    # for column in df.columns:
    #     print(column,':',pd.api.types.infer_dtype(df[column]))
    # print(df)
    # for column in df.columns:
    #     with open('test.txt', 'a') as newfile:
    #         newfile.write(pd.api.types.infer_dtype(df['minimum_value_in_Ether_ever_received_normal (14600.0days)']) + '\n')

    status_dict=df['category'].unique().tolist()
    df['transformed']=df['category'].apply(lambda x:status_dict.index(x))
    new_df = df.drop(['category'], axis=1)
    features = df[with_time_list]
    feature_label = df['transformed']

    f_test = features
    l_test = feature_label
    f_test = np.nan_to_num(f_test.astype(np.float32))
    l_test = np.nan_to_num(l_test.astype(np.float32))


    xgb_clf = xgb.XGBClassifier()
    xgb_clf.fit(f_train, l_train)
    l_predict = xgb_clf.predict(f_test)
    score = accuracy_score(l_test, l_predict)
    print(mean(score))
    accuracy_xgboost_binary_all_12.append(score)

with open('lastdance.txt', 'a') as newfile:
    newfile.write(first_csv + str(accuracy_xgboost_binary_all_12) + '\n')

first_csv = 'set1_malicious_be.csv'
second_csv = 'set3_malicious_be.csv'
accuracy_xgboost_binary_all_13 = []
time_list = [' (1hours)', ' (3hours)', ' (6hours)', ' (12hours)', ' (1.0days)', ' (3.0days)', ' (7.0days)', ' (14.0days)', ' (30.0days)', ' (90.0days)', ' (180.0days)', ' (365.0days)', ' (1095.0days)', ' (1825.0days)', ' (3650.0days)']
for time in time_list:
    with_time_list = []
    temp_str = ''
    for each_str in without_time_list:
        temp_str = each_str + time
        with_time_list.append(temp_str)
    dtype_dict = {}
    for each_feature in with_time_list:
        dtype_dict[each_feature] = float

    df = pd.read_csv(first_csv, dtype=dtype_dict)
    # for column in df.columns:
    #     print(column,':',pd.api.types.infer_dtype(df[column]))
    # print(df)
    # for column in df.columns:
    #     with open('test.txt', 'a') as newfile:
    #         newfile.write(pd.api.types.infer_dtype(df['minimum_value_in_Ether_ever_received_normal (14600.0days)']) + '\n')

    status_dict=df['category'].unique().tolist()
    df['transformed']=df['category'].apply(lambda x:status_dict.index(x))
    new_df = df.drop(['category'], axis=1)
    features = df[with_time_list]
    feature_label = df['transformed']

    f_train = features
    l_train = feature_label
    f_train = np.nan_to_num(f_train.astype(np.float32))
    l_train = np.nan_to_num(l_train.astype(np.float32))

    df = pd.read_csv(second_csv, dtype=dtype_dict)
    # for column in df.columns:
    #     print(column,':',pd.api.types.infer_dtype(df[column]))
    # print(df)
    # for column in df.columns:
    #     with open('test.txt', 'a') as newfile:
    #         newfile.write(pd.api.types.infer_dtype(df['minimum_value_in_Ether_ever_received_normal (14600.0days)']) + '\n')

    status_dict=df['category'].unique().tolist()
    df['transformed']=df['category'].apply(lambda x:status_dict.index(x))
    new_df = df.drop(['category'], axis=1)
    features = df[with_time_list]
    feature_label = df['transformed']

    f_test = features
    l_test = feature_label
    f_test = np.nan_to_num(f_test.astype(np.float32))
    l_test = np.nan_to_num(l_test.astype(np.float32))


    xgb_clf = xgb.XGBClassifier()
    xgb_clf.fit(f_train, l_train)
    l_predict = xgb_clf.predict(f_test)
    score = accuracy_score(l_test, l_predict)
    print(mean(score))
    accuracy_xgboost_binary_all_13.append(score)

with open('lastdance.txt', 'a') as newfile:
    newfile.write(first_csv + str(accuracy_xgboost_binary_all_13) + '\n')

first_csv = 'set1_malicious_be.csv'
second_csv = 'set4_malicious_be.csv'
accuracy_xgboost_binary_all_14 = []
time_list = [' (1hours)', ' (3hours)', ' (6hours)', ' (12hours)', ' (1.0days)', ' (3.0days)', ' (7.0days)', ' (14.0days)', ' (30.0days)', ' (90.0days)', ' (180.0days)', ' (365.0days)', ' (1095.0days)', ' (1825.0days)', ' (3650.0days)']
for time in time_list:
    with_time_list = []
    temp_str = ''
    for each_str in without_time_list:
        temp_str = each_str + time
        with_time_list.append(temp_str)
    dtype_dict = {}
    for each_feature in with_time_list:
        dtype_dict[each_feature] = float

    df = pd.read_csv(first_csv, dtype=dtype_dict)
    # for column in df.columns:
    #     print(column,':',pd.api.types.infer_dtype(df[column]))
    # print(df)
    # for column in df.columns:
    #     with open('test.txt', 'a') as newfile:
    #         newfile.write(pd.api.types.infer_dtype(df['minimum_value_in_Ether_ever_received_normal (14600.0days)']) + '\n')

    status_dict=df['category'].unique().tolist()
    df['transformed']=df['category'].apply(lambda x:status_dict.index(x))
    new_df = df.drop(['category'], axis=1)
    features = df[with_time_list]
    feature_label = df['transformed']

    f_train = features
    l_train = feature_label
    f_train = np.nan_to_num(f_train.astype(np.float32))
    l_train = np.nan_to_num(l_train.astype(np.float32))

    df = pd.read_csv(second_csv, dtype=dtype_dict)
    # for column in df.columns:
    #     print(column,':',pd.api.types.infer_dtype(df[column]))
    # print(df)
    # for column in df.columns:
    #     with open('test.txt', 'a') as newfile:
    #         newfile.write(pd.api.types.infer_dtype(df['minimum_value_in_Ether_ever_received_normal (14600.0days)']) + '\n')

    status_dict=df['category'].unique().tolist()
    df['transformed']=df['category'].apply(lambda x:status_dict.index(x))
    new_df = df.drop(['category'], axis=1)
    features = df[with_time_list]
    feature_label = df['transformed']

    f_test = features
    l_test = feature_label
    f_test = np.nan_to_num(f_test.astype(np.float32))
    l_test = np.nan_to_num(l_test.astype(np.float32))


    xgb_clf = xgb.XGBClassifier()
    xgb_clf.fit(f_train, l_train)
    l_predict = xgb_clf.predict(f_test)
    score = accuracy_score(l_test, l_predict)
    print(mean(score))
    accuracy_xgboost_binary_all_14.append(score)

with open('lastdance.txt', 'a') as newfile:
    newfile.write(first_csv + str(accuracy_xgboost_binary_all_14) + '\n')

first_csv = 'set4_malicious_be.csv'
second_csv = 'set1_malicious_be.csv'
accuracy_xgboost_binary_all_41 = []
time_list = [' (1hours)', ' (3hours)', ' (6hours)', ' (12hours)', ' (1.0days)', ' (3.0days)', ' (7.0days)', ' (14.0days)', ' (30.0days)', ' (90.0days)', ' (180.0days)', ' (365.0days)', ' (1095.0days)', ' (1825.0days)', ' (3650.0days)']
for time in time_list:
    with_time_list = []
    temp_str = ''
    for each_str in without_time_list:
        temp_str = each_str + time
        with_time_list.append(temp_str)
    dtype_dict = {}
    for each_feature in with_time_list:
        dtype_dict[each_feature] = float

    df = pd.read_csv(first_csv, dtype=dtype_dict)
    # for column in df.columns:
    #     print(column,':',pd.api.types.infer_dtype(df[column]))
    # print(df)
    # for column in df.columns:
    #     with open('test.txt', 'a') as newfile:
    #         newfile.write(pd.api.types.infer_dtype(df['minimum_value_in_Ether_ever_received_normal (14600.0days)']) + '\n')

    status_dict=df['category'].unique().tolist()
    df['transformed']=df['category'].apply(lambda x:status_dict.index(x))
    new_df = df.drop(['category'], axis=1)
    features = df[with_time_list]
    feature_label = df['transformed']

    f_train = features
    l_train = feature_label
    f_train = np.nan_to_num(f_train.astype(np.float32))
    l_train = np.nan_to_num(l_train.astype(np.float32))

    df = pd.read_csv(second_csv, dtype=dtype_dict)
    # for column in df.columns:
    #     print(column,':',pd.api.types.infer_dtype(df[column]))
    # print(df)
    # for column in df.columns:
    #     with open('test.txt', 'a') as newfile:
    #         newfile.write(pd.api.types.infer_dtype(df['minimum_value_in_Ether_ever_received_normal (14600.0days)']) + '\n')

    status_dict=df['category'].unique().tolist()
    df['transformed']=df['category'].apply(lambda x:status_dict.index(x))
    new_df = df.drop(['category'], axis=1)
    features = df[with_time_list]
    feature_label = df['transformed']

    f_test = features
    l_test = feature_label
    f_test = np.nan_to_num(f_test.astype(np.float32))
    l_test = np.nan_to_num(l_test.astype(np.float32))


    xgb_clf = xgb.XGBClassifier()
    xgb_clf.fit(f_train, l_train)
    l_predict = xgb_clf.predict(f_test)
    score = accuracy_score(l_test, l_predict)
    print(mean(score))
    accuracy_xgboost_binary_all_41.append(score)

with open('lastdance.txt', 'a') as newfile:
    newfile.write(first_csv + str(accuracy_xgboost_binary_all_41) + '\n')


first_csv = 'set4_malicious_be.csv'
second_csv = 'set2_malicious_be.csv'
accuracy_xgboost_binary_all_42 = []
time_list = [' (1hours)', ' (3hours)', ' (6hours)', ' (12hours)', ' (1.0days)', ' (3.0days)', ' (7.0days)', ' (14.0days)', ' (30.0days)', ' (90.0days)', ' (180.0days)', ' (365.0days)', ' (1095.0days)', ' (1825.0days)', ' (3650.0days)']
for time in time_list:
    with_time_list = []
    temp_str = ''
    for each_str in without_time_list:
        temp_str = each_str + time
        with_time_list.append(temp_str)
    dtype_dict = {}
    for each_feature in with_time_list:
        dtype_dict[each_feature] = float

    df = pd.read_csv(first_csv, dtype=dtype_dict)
    # for column in df.columns:
    #     print(column,':',pd.api.types.infer_dtype(df[column]))
    # print(df)
    # for column in df.columns:
    #     with open('test.txt', 'a') as newfile:
    #         newfile.write(pd.api.types.infer_dtype(df['minimum_value_in_Ether_ever_received_normal (14600.0days)']) + '\n')

    status_dict=df['category'].unique().tolist()
    df['transformed']=df['category'].apply(lambda x:status_dict.index(x))
    new_df = df.drop(['category'], axis=1)
    features = df[with_time_list]
    feature_label = df['transformed']

    f_train = features
    l_train = feature_label
    f_train = np.nan_to_num(f_train.astype(np.float32))
    l_train = np.nan_to_num(l_train.astype(np.float32))

    df = pd.read_csv(second_csv, dtype=dtype_dict)
    # for column in df.columns:
    #     print(column,':',pd.api.types.infer_dtype(df[column]))
    # print(df)
    # for column in df.columns:
    #     with open('test.txt', 'a') as newfile:
    #         newfile.write(pd.api.types.infer_dtype(df['minimum_value_in_Ether_ever_received_normal (14600.0days)']) + '\n')

    status_dict=df['category'].unique().tolist()
    df['transformed']=df['category'].apply(lambda x:status_dict.index(x))
    new_df = df.drop(['category'], axis=1)
    features = df[with_time_list]
    feature_label = df['transformed']

    f_test = features
    l_test = feature_label
    f_test = np.nan_to_num(f_test.astype(np.float32))
    l_test = np.nan_to_num(l_test.astype(np.float32))


    xgb_clf = xgb.XGBClassifier()
    xgb_clf.fit(f_train, l_train)
    l_predict = xgb_clf.predict(f_test)
    score = accuracy_score(l_test, l_predict)
    print(mean(score))
    accuracy_xgboost_binary_all_42.append(score)

with open('lastdance.txt', 'a') as newfile:
    newfile.write(first_csv + str(accuracy_xgboost_binary_all_42) + '\n')


first_csv = 'set4_malicious_be.csv'
second_csv = 'set3_malicious_be.csv'
accuracy_xgboost_binary_all_43 = []
time_list = [' (1hours)', ' (3hours)', ' (6hours)', ' (12hours)', ' (1.0days)', ' (3.0days)', ' (7.0days)', ' (14.0days)', ' (30.0days)', ' (90.0days)', ' (180.0days)', ' (365.0days)', ' (1095.0days)', ' (1825.0days)', ' (3650.0days)']
for time in time_list:
    with_time_list = []
    temp_str = ''
    for each_str in without_time_list:
        temp_str = each_str + time
        with_time_list.append(temp_str)
    dtype_dict = {}
    for each_feature in with_time_list:
        dtype_dict[each_feature] = float

    df = pd.read_csv(first_csv, dtype=dtype_dict)
    # for column in df.columns:
    #     print(column,':',pd.api.types.infer_dtype(df[column]))
    # print(df)
    # for column in df.columns:
    #     with open('test.txt', 'a') as newfile:
    #         newfile.write(pd.api.types.infer_dtype(df['minimum_value_in_Ether_ever_received_normal (14600.0days)']) + '\n')

    status_dict=df['category'].unique().tolist()
    df['transformed']=df['category'].apply(lambda x:status_dict.index(x))
    new_df = df.drop(['category'], axis=1)
    features = df[with_time_list]
    feature_label = df['transformed']

    f_train = features
    l_train = feature_label
    f_train = np.nan_to_num(f_train.astype(np.float32))
    l_train = np.nan_to_num(l_train.astype(np.float32))

    df = pd.read_csv(second_csv, dtype=dtype_dict)
    # for column in df.columns:
    #     print(column,':',pd.api.types.infer_dtype(df[column]))
    # print(df)
    # for column in df.columns:
    #     with open('test.txt', 'a') as newfile:
    #         newfile.write(pd.api.types.infer_dtype(df['minimum_value_in_Ether_ever_received_normal (14600.0days)']) + '\n')

    status_dict=df['category'].unique().tolist()
    df['transformed']=df['category'].apply(lambda x:status_dict.index(x))
    new_df = df.drop(['category'], axis=1)
    features = df[with_time_list]
    feature_label = df['transformed']

    f_test = features
    l_test = feature_label
    f_test = np.nan_to_num(f_test.astype(np.float32))
    l_test = np.nan_to_num(l_test.astype(np.float32))


    xgb_clf = xgb.XGBClassifier()
    xgb_clf.fit(f_train, l_train)
    l_predict = xgb_clf.predict(f_test)
    score = accuracy_score(l_test, l_predict)
    print(mean(score))
    accuracy_xgboost_binary_all_43.append(score)

with open('lastdance.txt', 'a') as newfile:
    newfile.write(first_csv + str(accuracy_xgboost_binary_all_43) + '\n')



names = ['1hour', '3hours', '6hours', '12hours', '1day', '3days', '7days', '14days', '30days', '90days', '180days', '1year', '3years', '5years', '10years']

x = range(len(names))
plt.plot(x, accuracy_xgboost_binary_all_32, marker='.', label='Dataset 2')
plt.plot(x, accuracy_xgboost_binary_all_34, marker='o', label='Dataset 4')
plt.legend()
plt.xticks(x, names, rotation=45)
plt.xlabel("Time")
plt.ylabel("Accuracy")
#plt.title("A simple plot")
plt.subplots_adjust(bottom=0.18)
plt.savefig('time_base_xgboost_dataset3_trained.png', dpi=300)

plt.cla()

names = ['1hour', '3hours', '6hours', '12hours', '1day', '3days', '7days', '14days', '30days', '90days', '180days', '1year', '3years', '5years', '10years']

x = range(len(names))
plt.plot(x, accuracy_xgboost_binary_all_14, marker='o', label='Dataset 4')
plt.legend()
plt.xticks(x, names, rotation=45)
plt.xlabel("Time")
plt.ylabel("Accuracy")
#plt.title("A simple plot")
plt.subplots_adjust(bottom=0.18)
plt.savefig('time_base_xgboost_dataset1_trained.png', dpi=300)

plt.cla()

names = ['1hour', '3hours', '6hours', '12hours', '1day', '3days', '7days', '14days', '30days', '90days', '180days', '1year', '3years', '5years', '10years']

x = range(len(names))
plt.plot(x, accuracy_xgboost_binary_all_41, marker='v', label='Dataset 1')
plt.plot(x, accuracy_xgboost_binary_all_42, marker='.', label='Dataset 2')
plt.plot(x, accuracy_xgboost_binary_all_43, marker='o', label='Dataset 3')
plt.legend()
plt.xticks(x, names, rotation=45)
plt.xlabel("Time")
plt.ylabel("Accuracy")
#plt.title("A simple plot")
plt.subplots_adjust(bottom=0.18)
plt.savefig('time_base_xgboost_dataset4_trained.png', dpi=300)

plt.cla()