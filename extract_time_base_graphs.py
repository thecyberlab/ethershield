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

multi_csv = 'multi.csv'
binary_csv = 'binary.csv'

accuracy_xgboost_multi_all = []
with open('top_features_xgboost_multi.txt', 'r') as newfile:
    feature_str = newfile.readline()
feature_list = feature_str[1:-2]
processing_feature_list = feature_list.replace('\'','').split(',')
without_time_list = []
for feature in processing_feature_list:
    without_time_list.append(feature.strip())
time_list = [' (1hours)', ' (3hours)', ' (6hours)', ' (12hours)', ' (1.0days)', ' (3.0days)', ' (7.0days)', ' (14.0days)', ' (30.0days)', ' (90.0days)', ' (180.0days)', ' (365.0days)', ' (1095.0days)', ' (1825.0days)', ' (3650.0days)']
for time in time_list:
    with_time_list = []
    temp_str = ''
    for each_str in without_time_list:
        if each_str[-1] != ')':
            temp_str = each_str + time
        else:
            temp_str = each_str
        with_time_list.append(temp_str)
    dtype_dict = {}
    for each_feature in with_time_list:
        dtype_dict[each_feature] = float

    df = pd.read_csv(multi_csv, dtype=dtype_dict)
    status_dict=df['category'].unique().tolist()
    df['transformed']=df['category'].apply(lambda x:status_dict.index(x))
    new_df = df.drop(['category'], axis=1)
    features = df[with_time_list]
    feature_label = df['transformed']


    temp_accuracy_list = []
    skf = StratifiedKFold(n_splits=4, shuffle=True, random_state=10)
    for train_index, test_index in skf.split(features, feature_label):
        f_train, f_test = features.iloc[train_index], features.iloc[test_index]
        l_train, l_test = feature_label.iloc[train_index], feature_label.iloc[test_index]
        f_train = np.nan_to_num(f_train.astype(np.float32))
        f_test = np.nan_to_num(f_test.astype(np.float32))
        l_train = np.nan_to_num(l_train.astype(np.float32))
        l_test = np.nan_to_num(l_test.astype(np.float32))
        xgb_clf = xgb.XGBClassifier(gamma= 0, max_delta_step= 0, max_depth= 7, min_child_weight= 5)
        xgb_clf.fit(f_train, l_train)
        l_predict = xgb_clf.predict(f_test)
        temp_accuracy_list.append(accuracy_score(l_test, l_predict))
    accuracy_xgboost_multi_all.append(mean(temp_accuracy_list))
    print(mean(temp_accuracy_list))

accuracy_xgboost_binary_all = []
with open('top_features_xgboost_binary.txt', 'r') as newfile:
    feature_str = newfile.readline()
feature_list = feature_str[1:-2]
processing_feature_list = feature_list.replace('\'','').split(',')
without_time_list = []
for feature in processing_feature_list:
    without_time_list.append(feature.strip())
time_list = [' (1hours)', ' (3hours)', ' (6hours)', ' (12hours)', ' (1.0days)', ' (3.0days)', ' (7.0days)', ' (14.0days)', ' (30.0days)', ' (90.0days)', ' (180.0days)', ' (365.0days)', ' (1095.0days)', ' (1825.0days)', ' (3650.0days)']
for time in time_list:
    with_time_list = []
    temp_str = ''
    for each_str in without_time_list:
        if each_str[-1] != ')':
            temp_str = each_str + time
        else:
            temp_str = each_str
        with_time_list.append(temp_str)
    dtype_dict = {}
    for each_feature in with_time_list:
        dtype_dict[each_feature] = float

    df = pd.read_csv(binary_csv, dtype=dtype_dict)
    status_dict=df['category'].unique().tolist()
    df['transformed']=df['category'].apply(lambda x:status_dict.index(x))
    new_df = df.drop(['category'], axis=1)
    features = df[with_time_list]
    feature_label = df['transformed']


    temp_accuracy_list = []
    skf = StratifiedKFold(n_splits=4, shuffle=True, random_state=10)
    for train_index, test_index in skf.split(features, feature_label):
        f_train, f_test = features.iloc[train_index], features.iloc[test_index]
        l_train, l_test = feature_label.iloc[train_index], feature_label.iloc[test_index]
        f_train = np.nan_to_num(f_train.astype(np.float32))
        f_test = np.nan_to_num(f_test.astype(np.float32))
        l_train = np.nan_to_num(l_train.astype(np.float32))
        l_test = np.nan_to_num(l_test.astype(np.float32))
        xgb_clf = xgb.XGBClassifier(gamma= 0, max_delta_step= 0, max_depth= 7, min_child_weight= 5)
        xgb_clf.fit(f_train, l_train)
        l_predict = xgb_clf.predict(f_test)
        temp_accuracy_list.append(accuracy_score(l_test, l_predict))
    accuracy_xgboost_binary_all.append(mean(temp_accuracy_list))
    print(mean(temp_accuracy_list))

accuracy_xgboost_multi_transaction = []
with open('top_features_xgboost_multi_only_transaction.txt', 'r') as newfile:
    feature_str = newfile.readline()
feature_list = feature_str[1:-2]
processing_feature_list = feature_list.replace('\'','').split(',')
without_time_list = []
for feature in processing_feature_list:
    without_time_list.append(feature.strip())
time_list = [' (1hours)', ' (3hours)', ' (6hours)', ' (12hours)', ' (1.0days)', ' (3.0days)', ' (7.0days)', ' (14.0days)', ' (30.0days)', ' (90.0days)', ' (180.0days)', ' (365.0days)', ' (1095.0days)', ' (1825.0days)', ' (3650.0days)']
for time in time_list:
    with_time_list = []
    temp_str = ''
    for each_str in without_time_list:
        if each_str[-1] != ')':
            temp_str = each_str + time
        else:
            temp_str = each_str
        with_time_list.append(temp_str)
    dtype_dict = {}
    for each_feature in with_time_list:
        dtype_dict[each_feature] = float

    df = pd.read_csv(multi_csv, dtype=dtype_dict)
    status_dict=df['category'].unique().tolist()
    df['transformed']=df['category'].apply(lambda x:status_dict.index(x))
    new_df = df.drop(['category'], axis=1)
    features = df[with_time_list]
    feature_label = df['transformed']


    temp_accuracy_list = []
    skf = StratifiedKFold(n_splits=4, shuffle=True, random_state=10)
    for train_index, test_index in skf.split(features, feature_label):
        f_train, f_test = features.iloc[train_index], features.iloc[test_index]
        l_train, l_test = feature_label.iloc[train_index], feature_label.iloc[test_index]
        f_train = np.nan_to_num(f_train.astype(np.float32))
        f_test = np.nan_to_num(f_test.astype(np.float32))
        l_train = np.nan_to_num(l_train.astype(np.float32))
        l_test = np.nan_to_num(l_test.astype(np.float32))
        xgb_clf = xgb.XGBClassifier(gamma= 0, max_delta_step= 0, max_depth= 7, min_child_weight= 5)
        xgb_clf.fit(f_train, l_train)
        l_predict = xgb_clf.predict(f_test)
        temp_accuracy_list.append(accuracy_score(l_test, l_predict))
    accuracy_xgboost_multi_transaction.append(mean(temp_accuracy_list))
    print(mean(temp_accuracy_list))

accuracy_xgboost_binary_transaction = []
with open('top_features_xgboost_binary_only_transaction.txt', 'r') as newfile:
    feature_str = newfile.readline()
feature_list = feature_str[1:-2]
processing_feature_list = feature_list.replace('\'','').split(',')
without_time_list = []
for feature in processing_feature_list:
    without_time_list.append(feature.strip())
time_list = [' (1hours)', ' (3hours)', ' (6hours)', ' (12hours)', ' (1.0days)', ' (3.0days)', ' (7.0days)', ' (14.0days)', ' (30.0days)', ' (90.0days)', ' (180.0days)', ' (365.0days)', ' (1095.0days)', ' (1825.0days)', ' (3650.0days)']
for time in time_list:
    with_time_list = []
    temp_str = ''
    for each_str in without_time_list:
        if each_str[-1] != ')':
            temp_str = each_str + time
        else:
            temp_str = each_str
        with_time_list.append(temp_str)
    dtype_dict = {}
    for each_feature in with_time_list:
        dtype_dict[each_feature] = float

    df = pd.read_csv(binary_csv, dtype=dtype_dict)
    status_dict=df['category'].unique().tolist()
    df['transformed']=df['category'].apply(lambda x:status_dict.index(x))
    new_df = df.drop(['category'], axis=1)
    features = df[with_time_list]
    feature_label = df['transformed']


    temp_accuracy_list = []
    skf = StratifiedKFold(n_splits=4, shuffle=True, random_state=10)
    for train_index, test_index in skf.split(features, feature_label):
        f_train, f_test = features.iloc[train_index], features.iloc[test_index]
        l_train, l_test = feature_label.iloc[train_index], feature_label.iloc[test_index]
        f_train = np.nan_to_num(f_train.astype(np.float32))
        f_test = np.nan_to_num(f_test.astype(np.float32))
        l_train = np.nan_to_num(l_train.astype(np.float32))
        l_test = np.nan_to_num(l_test.astype(np.float32))
        xgb_clf = xgb.XGBClassifier(gamma= 0, max_delta_step= 0, max_depth= 7, min_child_weight= 5)
        xgb_clf.fit(f_train, l_train)
        l_predict = xgb_clf.predict(f_test)
        temp_accuracy_list.append(accuracy_score(l_test, l_predict))
    accuracy_xgboost_binary_transaction.append(mean(temp_accuracy_list))
    print(mean(temp_accuracy_list))

accuracy_lightgbm_multi_all = []
with open('top_features_lightgbm_multi.txt', 'r') as newfile:
    feature_str = newfile.readline()
feature_list = feature_str[1:-2]
processing_feature_list = feature_list.replace('\'','').split(',')
without_time_list = []
for feature in processing_feature_list:
    without_time_list.append(feature.strip())
time_list = [' (1hours)', ' (3hours)', ' (6hours)', ' (12hours)', ' (1.0days)', ' (3.0days)', ' (7.0days)', ' (14.0days)', ' (30.0days)', ' (90.0days)', ' (180.0days)', ' (365.0days)', ' (1095.0days)', ' (1825.0days)', ' (3650.0days)']
for time in time_list:
    with_time_list = []
    temp_str = ''
    for each_str in without_time_list:
        if each_str[-1] != ')':
            temp_str = each_str + time
        else:
            temp_str = each_str
        with_time_list.append(temp_str)
    dtype_dict = {}
    for each_feature in with_time_list:
        dtype_dict[each_feature] = float

    df = pd.read_csv(multi_csv, dtype=dtype_dict)
    status_dict=df['category'].unique().tolist()
    df['transformed']=df['category'].apply(lambda x:status_dict.index(x))
    new_df = df.drop(['category'], axis=1)
    features = df[with_time_list]
    feature_label = df['transformed']


    temp_accuracy_list = []
    skf = StratifiedKFold(n_splits=4, shuffle=True, random_state=10)
    for train_index, test_index in skf.split(features, feature_label):
        f_train, f_test = features.iloc[train_index], features.iloc[test_index]
        l_train, l_test = feature_label.iloc[train_index], feature_label.iloc[test_index]
        f_train = np.nan_to_num(f_train.astype(np.float32))
        f_test = np.nan_to_num(f_test.astype(np.float32))
        l_train = np.nan_to_num(l_train.astype(np.float32))
        l_test = np.nan_to_num(l_test.astype(np.float32))
        lgb_clf = lgb.LGBMClassifier(max_delta_step = 8, max_depth = 8, num_leaves = 21)
        lgb_clf.fit(f_train, l_train)
        l_predict = lgb_clf.predict(f_test)
        temp_accuracy_list.append(accuracy_score(l_test, l_predict))
    accuracy_lightgbm_multi_all.append(mean(temp_accuracy_list))
    print(mean(temp_accuracy_list))

accuracy_lightgbm_binary_all = []
with open('top_features_lightgbm_binary.txt', 'r') as newfile:
    feature_str = newfile.readline()
feature_list = feature_str[1:-2]
processing_feature_list = feature_list.replace('\'','').split(',')
without_time_list = []
for feature in processing_feature_list:
    without_time_list.append(feature.strip())
time_list = [' (1hours)', ' (3hours)', ' (6hours)', ' (12hours)', ' (1.0days)', ' (3.0days)', ' (7.0days)', ' (14.0days)', ' (30.0days)', ' (90.0days)', ' (180.0days)', ' (365.0days)', ' (1095.0days)', ' (1825.0days)', ' (3650.0days)']
for time in time_list:
    with_time_list = []
    temp_str = ''
    for each_str in without_time_list:
        if each_str[-1] != ')':
            temp_str = each_str + time
        else:
            temp_str = each_str
        with_time_list.append(temp_str)
    dtype_dict = {}
    for each_feature in with_time_list:
        dtype_dict[each_feature] = float

    df = pd.read_csv(binary_csv, dtype=dtype_dict)
    status_dict=df['category'].unique().tolist()
    df['transformed']=df['category'].apply(lambda x:status_dict.index(x))
    new_df = df.drop(['category'], axis=1)
    features = df[with_time_list]
    feature_label = df['transformed']


    temp_accuracy_list = []
    skf = StratifiedKFold(n_splits=4, shuffle=True, random_state=10)
    for train_index, test_index in skf.split(features, feature_label):
        f_train, f_test = features.iloc[train_index], features.iloc[test_index]
        l_train, l_test = feature_label.iloc[train_index], feature_label.iloc[test_index]
        f_train = np.nan_to_num(f_train.astype(np.float32))
        f_test = np.nan_to_num(f_test.astype(np.float32))
        l_train = np.nan_to_num(l_train.astype(np.float32))
        l_test = np.nan_to_num(l_test.astype(np.float32))
        lgb_clf = lgb.LGBMClassifier(max_delta_step = 8, max_depth = 8, num_leaves = 21)
        lgb_clf.fit(f_train, l_train)
        l_predict = lgb_clf.predict(f_test)
        temp_accuracy_list.append(accuracy_score(l_test, l_predict))
    accuracy_lightgbm_binary_all.append(mean(temp_accuracy_list))
    print(mean(temp_accuracy_list))

accuracy_lightgbm_multi_transaction = []
with open('top_features_lightgbm_multi_only_transaction.txt', 'r') as newfile:
    feature_str = newfile.readline()
feature_list = feature_str[1:-2]
processing_feature_list = feature_list.replace('\'','').split(',')
without_time_list = []
for feature in processing_feature_list:
    without_time_list.append(feature.strip())
time_list = [' (1hours)', ' (3hours)', ' (6hours)', ' (12hours)', ' (1.0days)', ' (3.0days)', ' (7.0days)', ' (14.0days)', ' (30.0days)', ' (90.0days)', ' (180.0days)', ' (365.0days)', ' (1095.0days)', ' (1825.0days)', ' (3650.0days)']
for time in time_list:
    with_time_list = []
    temp_str = ''
    for each_str in without_time_list:
        if each_str[-1] != ')':
            temp_str = each_str + time
        else:
            temp_str = each_str
        with_time_list.append(temp_str)
    dtype_dict = {}
    for each_feature in with_time_list:
        dtype_dict[each_feature] = float

    df = pd.read_csv(multi_csv, dtype=dtype_dict)
    status_dict=df['category'].unique().tolist()
    df['transformed']=df['category'].apply(lambda x:status_dict.index(x))
    new_df = df.drop(['category'], axis=1)
    features = df[with_time_list]
    feature_label = df['transformed']


    temp_accuracy_list = []
    skf = StratifiedKFold(n_splits=4, shuffle=True, random_state=10)
    for train_index, test_index in skf.split(features, feature_label):
        f_train, f_test = features.iloc[train_index], features.iloc[test_index]
        l_train, l_test = feature_label.iloc[train_index], feature_label.iloc[test_index]
        f_train = np.nan_to_num(f_train.astype(np.float32))
        f_test = np.nan_to_num(f_test.astype(np.float32))
        l_train = np.nan_to_num(l_train.astype(np.float32))
        l_test = np.nan_to_num(l_test.astype(np.float32))
        lgb_clf = lgb.LGBMClassifier(max_delta_step = 8, max_depth = 8, num_leaves = 21)
        lgb_clf.fit(f_train, l_train)
        l_predict = lgb_clf.predict(f_test)
        temp_accuracy_list.append(accuracy_score(l_test, l_predict))
    accuracy_lightgbm_multi_transaction.append(mean(temp_accuracy_list))
    print(mean(temp_accuracy_list))

accuracy_lightgbm_binary_transaction = []
with open('top_features_lightgbm_binary_only_transaction.txt', 'r') as newfile:
    feature_str = newfile.readline()
feature_list = feature_str[1:-2]
processing_feature_list = feature_list.replace('\'','').split(',')
without_time_list = []
for feature in processing_feature_list:
    without_time_list.append(feature.strip())
time_list = [' (1hours)', ' (3hours)', ' (6hours)', ' (12hours)', ' (1.0days)', ' (3.0days)', ' (7.0days)', ' (14.0days)', ' (30.0days)', ' (90.0days)', ' (180.0days)', ' (365.0days)', ' (1095.0days)', ' (1825.0days)', ' (3650.0days)']
for time in time_list:
    with_time_list = []
    temp_str = ''
    for each_str in without_time_list:
        if each_str[-1] != ')':
            temp_str = each_str + time
        else:
            temp_str = each_str
        with_time_list.append(temp_str)
    dtype_dict = {}
    for each_feature in with_time_list:
        dtype_dict[each_feature] = float

    df = pd.read_csv(binary_csv, dtype=dtype_dict)
    status_dict=df['category'].unique().tolist()
    df['transformed']=df['category'].apply(lambda x:status_dict.index(x))
    new_df = df.drop(['category'], axis=1)
    features = df[with_time_list]
    feature_label = df['transformed']


    temp_accuracy_list = []
    skf = StratifiedKFold(n_splits=4, shuffle=True, random_state=10)
    for train_index, test_index in skf.split(features, feature_label):
        f_train, f_test = features.iloc[train_index], features.iloc[test_index]
        l_train, l_test = feature_label.iloc[train_index], feature_label.iloc[test_index]
        f_train = np.nan_to_num(f_train.astype(np.float32))
        f_test = np.nan_to_num(f_test.astype(np.float32))
        l_train = np.nan_to_num(l_train.astype(np.float32))
        l_test = np.nan_to_num(l_test.astype(np.float32))
        lgb_clf = lgb.LGBMClassifier(max_delta_step = 8, max_depth = 8, num_leaves = 21)
        lgb_clf.fit(f_train, l_train)
        l_predict = lgb_clf.predict(f_test)
        temp_accuracy_list.append(accuracy_score(l_test, l_predict))
    accuracy_lightgbm_binary_transaction.append(mean(temp_accuracy_list))
    print(mean(temp_accuracy_list))

names = ['1hour', '3hours', '6hours', '12hours', '1day', '3days', '7days', '14days', '30days', '90days', '180days', '1year', '3years', '5years', '10years']

x = range(len(names))
plt.plot(x, accuracy_xgboost_multi_all, marker='v', label='Multi-class classification with all features')
plt.plot(x, accuracy_xgboost_binary_all, marker='.', label='Binary classification with all features')
plt.plot(x, accuracy_xgboost_multi_transaction, marker='o', label='Multi-class classification with activity features')
plt.plot(x, accuracy_xgboost_binary_transaction, marker='^', label='Binary classification with activity features')
plt.legend()
plt.xticks(x, names, rotation=45)
plt.xlabel("Time")
plt.ylabel("Accuracy")
#plt.title("A simple plot")
plt.subplots_adjust(bottom=0.18)
plt.savefig('time_base_xgboost.png', dpi=300)

plt.cla()

names = ['1hour', '3hours', '6hours', '12hours', '1day', '3days', '7days', '14days', '30days', '90days', '180days', '1year', '3years', '5years', '10years']

x = range(len(names))
plt.plot(x, accuracy_lightgbm_multi_all, marker='v', label='Multi-class classification with all features')
plt.plot(x, accuracy_lightgbm_binary_all, marker='.', label='Binary classification with all features')
plt.plot(x, accuracy_lightgbm_multi_transaction, marker='o', label='Multi-class classification with activity features')
plt.plot(x, accuracy_lightgbm_binary_transaction, marker='^', label='Binary classification with activity features')
plt.legend()
plt.xticks(x, names, rotation=45)
plt.xlabel("Time")
plt.ylabel("Accuracy")
#plt.title("A simple plot")
plt.subplots_adjust(bottom=0.18)
plt.savefig('time_base_lightgbm.png', dpi=300)


with open('xgboost_time_base_data.txt', 'a') as newfile:
    newfile.write('accuracy_xgboost_multi_all' + str(accuracy_xgboost_multi_all) + '\n')
with open('xgboost_time_base_data.txt', 'a') as newfile:
    newfile.write('accuracy_xgboost_binary_all' + str(accuracy_xgboost_binary_all) + '\n')
with open('xgboost_time_base_data.txt', 'a') as newfile:
    newfile.write('accuracy_xgboost_multi_transaction' + str(accuracy_xgboost_multi_transaction) + '\n')
with open('xgboost_time_base_data.txt', 'a') as newfile:
    newfile.write('accuracy_xgboost_binary_transaction' + str(accuracy_xgboost_binary_transaction) + '\n')

with open('lightgbm_time_base_data.txt', 'a') as newfile:
    newfile.write('accuracy_lightgbm_multi_all' + str(accuracy_lightgbm_multi_all) + '\n')
with open('lightgbm_time_base_data.txt', 'a') as newfile:
    newfile.write('accuracy_lightgbm_binary_all' + str(accuracy_lightgbm_binary_all) + '\n')
with open('lightgbm_time_base_data.txt', 'a') as newfile:
    newfile.write('accuracy_lightgbm_multi_transaction' + str(accuracy_lightgbm_multi_transaction) + '\n')
with open('lightgbm_time_base_data.txt', 'a') as newfile:
    newfile.write('accuracy_lightgbm_binary_transaction' + str(accuracy_lightgbm_binary_transaction) + '\n')