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
                    'the_propotion_of_erc1155_ether_received_of_all_touched']
feature_set_opcode_tf_idf = ['push1(opcode)','dup1(opcode)','swap1(opcode)','pop(opcode)','push2(opcode)','dup2(opcode)','add(opcode)','jumpdest(opcode)','mstore(opcode)','and(opcode)','swap2(opcode)','push20(opcode)','iszero(opcode)','mload(opcode)','jumpi(opcode)','dup3(opcode)','jump(opcode)','sub(opcode)','dup4(opcode)','sload(opcode)','revert(opcode)','swap3(opcode)','sha3(opcode)','push4(opcode)','invalid(opcode)','eq(opcode)','exp(opcode)','calldataload(opcode)','dup5(opcode)','shl(opcode)','div(opcode)','mul(opcode)','callvalue(opcode)','returndatasize(opcode)','lt(opcode)','dup6(opcode)','return(opcode)','caller(opcode)','sstore(opcode)','swap4(opcode)','push32(opcode)','stop(opcode)','gt(opcode)','calldatasize(opcode)','codecopy(opcode)','dup7(opcode)','dup9(opcode)','address(opcode)','swap5(opcode)','dup8(opcode)','not(opcode)','call(opcode)','or(opcode)','push8(opcode)','swap6(opcode)','calldatacopy(opcode)','gas(opcode)','extcodesize(opcode)','push29(opcode)','returndatacopy(opcode)','push6(opcode)','delegatecall(opcode)','log1(opcode)','dup12(opcode)','dup15(opcode)','swap8(opcode)','log3(opcode)']
feature_set_ngram_bytecode = ['zmzmzg(bytecode)','mdawma(bytecode)','njawma(bytecode)','njayma(bytecode)','nti2ma(bytecode)','nty1yg(bytecode)','njawmq(bytecode)','mde2ma(bytecode)','mdaxng(bytecode)','njbhma(bytecode)','mtywyq(bytecode)','nja0ma(bytecode)','nta1ma(bytecode)','ode1mg(bytecode)','mtuyng(bytecode)','mdawoa(bytecode)','mdiwma(bytecode)','mjawmq(bytecode)','mdywma(bytecode)','mdiwyq(bytecode)','mjbhma(bytecode)','nwi2ma(bytecode)','mtu2mq(bytecode)','njving(bytecode)','ntyxma(bytecode)','mjywmg(bytecode)','mgewng(bytecode)','mduwnq(bytecode)','yta2ma(bytecode)','mda4ma(bytecode)','mde5ma(bytecode)','ntc2ma(bytecode)','mwiwmw(bytecode)','ytaxyg(bytecode)','mdqwnq(bytecode)','mtywma(bytecode)','mgewmq(bytecode)','mgzknq(bytecode)','zmq1yg(bytecode)','mdaxoq(bytecode)','nzywma(bytecode)','yjywma(bytecode)','mdfima(bytecode)','mdyxma(bytecode)','mdayma(bytecode)','zmzmmq(bytecode)','nznmzg(bytecode)','m2zmzg(bytecode)','njewmq(bytecode)','ota4mq(bytecode)','njawmg(bytecode)','ntq2ma(bytecode)','mgewmw(bytecode)','njewma(bytecode)','ndywma(bytecode)','mdgwnq(bytecode)','oda1na(bytecode)','ota5mq(bytecode)','ndyxma(bytecode)','mtaxnq(bytecode)','ote5ma(bytecode)','mjywma(bytecode)','mdaynq(bytecode)','mtawma(bytecode)','mtq2mq(bytecode)','oda1mq(bytecode)','mdawmg(bytecode)','mde1ng(bytecode)','ntc4ma(bytecode)','nte2ma(bytecode)','ntdmzq(bytecode)','mdywna(bytecode)','zmu1yg(bytecode)','nda1mq(bytecode)','n2zlnq(bytecode)','mtuxnq(bytecode)','mtawnq(bytecode)','mtywmg(bytecode)','mty2ma(bytecode)','mduwng(bytecode)','oda4mw(bytecode)','nwi2mq(bytecode)','mde4na(bytecode)','nwi1ma(bytecode)','odewmq(bytecode)','yjuwnq(bytecode)','yjyxma(bytecode)','mtaxoa(bytecode)','mdqwoa(bytecode)','njayna(bytecode)','ztving(bytecode)','nta1ng(bytecode)','njawna(bytecode)','mduxng(bytecode)','njywma(bytecode)','mduxoa(bytecode)','nta2ma(bytecode)','nte1ng(bytecode)','nte4ma(bytecode)','nte5ma(bytecode)','nda4ma(bytecode)','mdgwzg(bytecode)','odbmza(bytecode)','njewmg(bytecode)','njewna(bytecode)','ota2ma(bytecode)','odiwmq(bytecode)','zdving(bytecode)']
feature_set_ngram_all = ['rfvqmibnu1rpukugufvtsdegmhgyma(op)','tvnut1jfifbvu0gxidb4mjagqure(op)','ufvtsdegmhg0mcbnte9brcbevvax(op)','ufvtsdegmhgymcbbreqgu1dbude(op)','ufvtsdiwidb4zmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzibbtkqgufvtsdiw(op)','qu5eifbvu0gymcawegzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmygqu5e(op)','mhhmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmieforcbqvvnimjagmhhmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzm(op)','ufvtsdegmhgwiervudegukvwrvju(op)','mhgwiervudegukvwrvjuiepvtvbervnu(op)','slvnuekgufvtsdegmhgwiervude(op)','ufvtsdiwidb4zmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzibbtkqgrfvqmg(op)','mhhmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmieforcbevvayie1tve9srq(op)','qu5eiervudigtvnut1jfifbvu0gx(op)','ufvtsdegmhgxifbvu0gxidb4yta(op)','ufvtsdegmhgymcbbreqgufvtsde(op)','ufvtsdegmhgymcbbreqgu1dbudi(op)','u1dbudegrfvqmibnu1rpukugufvtsde(op)','qureifbvu0gxidb4mcbtseez(op)','mhgymcbbreqgu1dbudegrfvqmg(op)','mhgymcbbreqgufvtsdegmhgw(op)','qureifnxqvaxiervudigtvnut1jf(op)','mhgymcbbreqgu1dbudigue9q(op)','u1dbudegufvtsdegmhgymcbbreq(op)','tuxpquqgrfvqmsbtv0fqmibtvui(op)','rfvqmsbtv0fqmibtvuigu1dbude(op)','mhg0mcbnte9brcbevvaxifnxqvay(op)','ue9qifbvu0gxidb4ndagtuxpquq(op)','u1dbudigue9qifbpucbqvvnimq(op)','ue9qifbpucbqvvnimsawedqw(op)','qureifnxqvayifbpucbqt1a(op)','mhg0mcbnte9brcbevvaxiervudm(op)','ufvtsdegmhhhmcbqvvnimsawedi(op)','mhhhmcbqvvnimsawedigrvhq(op)','mhgxifbvu0gxidb4ytagufvtsde(op)','ufvtsdegmhgyievyucbtvui(op)','slvnuerfu1qgq0fmtfzbtfvfiervudegsvnarvjp(op)','ukvwrvjuiepvtvbervnuifbpucbqvvnimg(op)','u1dbudegu1dbudmgu1dbudigu1dbude(op)','slvnuerfu1qgufvtsdegmhg0mcbnte9bra(op)','slvnucbkvu1qrevtvcbqvvnimsawedqw(op)','mhgymcbbreqgu1dbudegu1dbudm(op)','qureifnxqvaxifnxqvazifnxqvay(op)','mhgxifbvu0gxidb4msbqvvnimq(op)','ufvtsdegmhgxifbvu0gxidb4mq(op)','mhgxifbvu0gxidb4ytagu0hm(op)','ue9qifbpucbqt1ague9q(op)','ufvtsdegmhhhmcbtsewgu1vc(op)','u1dbudegukvuvvjoiepvtvbervnuienbtexwquxvrq(op)','rfvqmsbsrvzfulqgslvnuerfu1qgue9q(op)','u1vcifnxqvaxifjfvfvstibkvu1qrevtva(op)','tfqgsvnarvjpifbvu0gyidb4mg(op)','svnarvjpifbvu0gyidb4mibkvu1qsq(op)','u0xpquqgufvtsdegmhgxifbvu0gx(op)','rfvqmibmvcbju1pfuk8gufvtsdi(op)','rfvqmibnte9brcbtv0fqmibnu1rpuku(op)','rfvqncbdt0rfq09qwsbevvayie1mt0fe(op)','ufvtsdegmhgwiervudegtuxpquq(op)','mhgwiervudegtuxpquqgufvtsde(op)','tuxpquqgufvtsdegmhgymcbqvvnimg(op)','q09erunpufkgrfvqmibnte9brcbtv0fqmg(op)','rfvqmsbnte9brcbqvvnimsawediw(op)','u1dbudegrfvqmibmvcbju1pfuk8(op)','ufvtsdegmhg0mcbevvaxie1mt0fe(op)','tvvmifbvu0gxidb4mcbevvax(op)','tuxpquqgu1dbudigtvnut1jfiefera(op)','rfvqmibkvu1qiepvtvbervnuifbvu0gy(op)','mhgyievyucbtvuigqu5e(op)','slvnuerfu1qgq0fmtfzbtfvfifbvu0gyidb4ma(op)','ufvtsdigmhgwiepvtvbjifbvu0gy(op)','q0fmtfzbtfvfifbvu0gyidb4mcbkvu1qsq(op)','slvnuerfu1qgufvtsdegmhg0mcbevvax(op)','rfvqmsbtte9brcbqvvnimsawede(op)','ufvtsdegmhgwifbvu0gxidb4ma(op)','rfvqmybevvayiervudigrfvqmg(op)','rfvqnibevva5iervudqgq0fmta(op)','rfvqmibevva2iervudkgrfvqna(op)','rfvqmibtv0fqmsbtvuigufvtsde(op)','qureifnxqvaxifjfvfvstibkvu1qrevtva(op)','mhgyievyucbtvuigtk9u(op)','rfvqmibevvayiervudygrfvqoq(op)','rfvqmibevvayiervudigrfvqng(op)','u1dbudegrfvqmibtv0fqmsbtvui(op)','tuxpquqgu1dbudegrfvqmibtv0fqmq(op)','svnarvjpifbvu0gyidb4mcbkvu1qsq(op)','ufvtsdigmhgyyzygr0ftifnvqg(op)','ue9qifbpucbqt1agufvtsde(op)','ue9qifbpucbqt1agslvnua(op)','ue9qifbpucbkvu1qiepvtvbervnu(op)','rfvqmsbevvaziervudugq0fmterbvefdt1bz(op)','slvnucbkvu1qrevtvcbtve9qiepvtvbervnu(op)','slvnuekgsu5wquxjrcbkvu1qrevtvcbqt1a(op)','slvnuekgsu5wquxjrcbkvu1qrevtvcbqvvnimg(op)','slvnuerfu1qgue9qifbpucbqt1a(op)','slvnuerfu1qgq0fmtfzbtfvfieltwkvstybqvvnimg(op)','mhg0mcbevvaxie1mt0feifbvu0gx(op)','rfvqmibbreqgrfvqnsbtv0fqmq(op)','mhg0mcbnte9brcbevvaxiervudq(op)','su5wquxjrcbkvu1qrevtvcbqt1ague9q(op)','u1dbudegrelwiervudugtvvm(op)','u1dbudegrfvqmibbreqgrfvqnq(op)','u1dbudcgue9qifbvu0gyidb4mwvm(op)','u1dbudegrfvqnsbbreqgrfvqna(op)','u1dbudegtvnut1jfiervudigtuxpquq(op)','u0xpquqgufvtsdegmhg0mcbevvax(op)','u0hbmybjtlzbteleiervudeyifjfvfvstkrbvefdt1bz(op)','u1dbudegu1dbudmgqureifnxqvay(op)','tvvmiervudygqureiervudu(op)','u1dbudmgu1dbudqgu1dbudigu1dbude(op)','u1dbudmgue9qifbpucbqt1a(op)','u1dbudmgu1dbudigue9qifbpua(op)','u1dbudegu1dbudqgqu5eifnxqvaz(op)','u1dbudigue9qifbpucbtv0fqmw(op)','u1dbudegu1dbudygtvnut1jfiervudu(op)','u1dbudegu1vciefercbevvay(op)','u1dbudegu1vcifbvu0gxidb4mja(op)','u1dbudegue9qiepvtvbervnuifnxqvaz(op)','u1dbudmgu1dbudegu1dbudqgqu5e(op)','u1dbudmgtuxpquqgu1dbudmgu1dbude(op)','u1dbudigrfvqmibtv0fqmsbevva1(op)','u1dbudigsvnarvjpieltwkvstybevvaz(op)','u1dbudigu1dbudegu1dbudmgqure(op)','u1dbudmgrfvqmybtv0fqmsbtvui(op)','u1dbudmgqureifnxqvayiervudi(op)','u1dbudigue9qifbpucbkvu1q(op)','u1dbudegue9qifbvu0gymcawegzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmy(op)','rfvqmsbsrvzfulqgslvnuerfu1qgufvtsdi(op)','q0fmtfzbtfvfiervudegsvnarvjpifbvu0gy(op)','slvnucbkvu1qrevtvcbqvvnimsaweda(op)','ufvtsdegmhg0mcbnte9brcbqvvnimq(op)','svnarvjpiervudegsvnarvjpifbvu0gy(op)','slvnuerfu1qgufvtsdegmhgwiervude(op)','mhgyievyucbtvuigu1dbude(op)','mhgymcbbreqgu1dbudegu1dbudi(op)','qureifnxqvaxifnxqvayifnxqvax(op)','rfvqmsbevva0ifnvqibevvay(op)','tuxpquqgrfvqmsbevva0ifnvqg(op)','ukvwrvjuiepvtvbervnuifbpucbqt1a(op)','ufvtsdigmhgxmdagrvhqifnxqvax(op)','mhgxmdagrvhqifnxqvaxierjvg(op)','u1dbudegufvtsdigmhgxmdagrvhq(op)','u0xpquqgu1dbudegufvtsdigmhgxmda(op)','u1dbudegu0xpquqgu1dbudegufvtsdi(op)','ufvtsdegmhgwifnxqvaxiervudi(op)','mhgwifnxqvaxiervudigtvnut1jf(op)','rfvqmsbsrvzfulqgslvnuerfu1qgufvtsde(op)','ue9qiepvtvagslvnuerfu1qgufvtsde(op)','tuxpquqgufvtsdegmhgymcbqvvnimq(op)','relwifbvu0gymcawegzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmygqu5e(op)','u1dbudegrelwifbvu0gymcawegzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmy(op)','rvhqifnxqvaxierjvibqvvnimja(op)','q0fmtevsifbvu0gymcawegzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmzmygqu5e(op)','ukvuvvjoiepvtvbervnuienbtexwquxvrsbju1pfuk8(op)','u1dbudigu1vcifnxqvaxifjfvfvstg(op)','ufvtsdegmhgwifniqtmgufvtsde(op)','mhgwifniqtmgufvtsdegmhgw(op)']
feature_set_operands_tf_idf = ['0x0(operands)','0x20(operands)','0xffffffffffffffffffffffffffffffffffffffff(operands)','0x40(operands)','0x1(operands)','0xa0(operands)','0x4(operands)','0x2(operands)','0x100(operands)','0x1f(operands)','0x24(operands)','0xffffffff(operands)','0xff(operands)','0x7(operands)','0x461bcd(operands)','0xe5(operands)','0x8c379a000000000000000000000000000000000000000000000000000000000(operands)','0x9(operands)','0x60(operands)','0x6(operands)','0x5(operands)','0xa(operands)','0x44(operands)','0xe0(operands)','0x3(operands)','0x64(operands)','0xf10f6a15e259465232009528ad32ea5743ce152309fc(operands)','0xe659bb22726afd6009b17c3ae23679ed41784f382129f7fb0b2ef6776e0413d9(operands)','0xaf1931c20ee0c11bea17a41bfbbad299b2763bc0(operands)','0x30(operands)','0x87(operands)','0x8fc(operands)','0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef(operands)','0x627a7a723058(operands)','0x25(operands)','0x8(operands)','0x26(operands)','0x100000000000000000000000000000000000000000000000000000000(operands)','0xb(operands)','0x2b(operands)','0x80(operands)','0xa9059cbb(operands)','0x23(operands)','0x2c6(operands)','0x70a08231(operands)','0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925(operands)','0x18160ddd(operands)','0x313ce567(operands)','0x95d89b41(operands)','0x23b872dd(operands)','0x290decd9548b62a8d60345a988386fc84ba6bc95484008f6362f93160ef3e563(operands)','0x107(operands)','0xa8d603(operands)','0xc84ba6bc95484008f6362f93160ef3e5(operands)','0xde0b6b3a7640000(operands)','0x18f(operands)','0xe97dcb62(operands)','0x8da5cb5b(operands)','0xa60f3588(operands)','0x188(operands)','0x6c(operands)','0x13af4035(operands)','0xb69ef8a8(operands)','0x167(operands)','0x9003adfe(operands)','0xd(operands)','0x8ac7230489e80000(operands)','0x129(operands)','0xbf(operands)','0x32(operands)','0xf(operands)','0x16e(operands)','0x50(operands)','0x5a(operands)','0xc0ee0b8a(operands)','0x9a(operands)','0x92(operands)','0x7e(operands)','0x6ea056a9(operands)','0x189(operands)','0x52(operands)','0x1e0(operands)','0x49(operands)','0x104(operands)','0x3c18d31800000000000000000000000000000000000000000000000000000000(operands)','0x3c18d318(operands)','0x17b(operands)','0x1ef(operands)','0x718(operands)','0x8796(operands)','0xa9059cbb00000000000000000000000000000000000000000000000000000000(operands)','0xec(operands)','0x125(operands)','0xfdcf3cf6cbee9677fe38(operands)','0x4b(operands)','0x4d2(operands)','0x1000000000000000000000000(operands)','0x14(operands)','0x25e(operands)','0x260(operands)','0x2ea(operands)','0x464(operands)','0x4de(operands)','0x61(operands)','0x77(operands)','0xffffffffffffffff(operands)','0x6e(operands)','0x3fad9ae0(operands)','0x8d(operands)','0x10b(operands)','0x3853682c(operands)','0x19d(operands)','0xb8(operands)','0x81(operands)','0x32d(operands)','0xfd(operands)','0xc(operands)','0xdd62ed3e(operands)','0xe(operands)','0x6fdde03(operands)','0x95ea7b3(operands)','0x12(operands)','0x10(operands)']

multi_csv = 'multi.csv'
binary_csv = 'binary.csv'
top_many = 50


#lightgbm binary
top_features_xgboost_binary = []
top_features_xgboost_binary_score = {}
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
    for each_feature in feature_set_opcode_tf_idf:
        dtype_dict[each_feature] = float
    for each_feature in feature_set_ngram_bytecode:
        dtype_dict[each_feature] = float
    for each_feature in feature_set_ngram_all:
        dtype_dict[each_feature] = float
    for each_feature in feature_set_operands_tf_idf:
        dtype_dict[each_feature] = float

    df = pd.read_csv(binary_csv, dtype=dtype_dict)
    status_dict=df['category'].unique().tolist()
    df['transformed']=df['category'].apply(lambda x:status_dict.index(x))
    new_df = df.drop(['category'], axis=1)
    features = df[with_time_list + feature_set_opcode_tf_idf + feature_set_ngram_bytecode + feature_set_ngram_all + feature_set_operands_tf_idf]
    feature_label = df['transformed']
    features = np.nan_to_num(features.astype(np.float32))
    feature_label = np.nan_to_num(feature_label.astype(np.float32))
    lgb_clf = lgb.LGBMClassifier(max_delta_step = 8, max_depth = 8, num_leaves = 21)
    lgb_clf.fit(features, feature_label)

    converted_list = with_time_list + feature_set_opcode_tf_idf + feature_set_ngram_bytecode + feature_set_ngram_all + feature_set_operands_tf_idf

    df_feature_importance = (pd.DataFrame({'feature': lgb_clf.feature_name_, 'importance': lgb_clf.feature_importances_,}).sort_values('importance', ascending=False))
    feature_names = df_feature_importance['feature'].tolist()
    scores = df_feature_importance['importance'].tolist()

    new_name = []
    for name in feature_names:
        new_name.append(name[7:])

    ranked_list = []
    for name in new_name:
        ranked_list.append(converted_list[int(name)])
    top_ranked_list = ranked_list[0:top_many]
    i = 0
    for real_feature_name in top_ranked_list:
        if real_feature_name.split(" ")[0] not in top_features_xgboost_binary:
            top_features_xgboost_binary.append(real_feature_name.split(" ")[0])
        if real_feature_name.split(" ")[0] in top_features_xgboost_binary_score:
            top_features_xgboost_binary_score[real_feature_name.split(" ")[0]] = top_features_xgboost_binary_score[real_feature_name.split(" ")[0]] + scores[i]
        else:
            top_features_xgboost_binary_score[real_feature_name.split(" ")[0]] = scores[i]
        i = i + 1
with open('top_features_lightgbm_binary.txt', 'a') as newfile:
        newfile.write(str(top_features_xgboost_binary) + '\n')
with open('top_features_lightgbm_binary.txt', 'a') as newfile:
        newfile.write(str(top_features_xgboost_binary_score) + '\n')
for name, score in top_features_xgboost_binary_score.items():
    with open('top_features_lightgbm_binary.txt', 'a') as newfile:
        newfile.write(name + ' ' + str(score) + '\n')

#lightgbm multi
top_features_xgboost_multi = []
top_features_xgboost_multi_score = {}
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
    for each_feature in feature_set_opcode_tf_idf:
        dtype_dict[each_feature] = float
    for each_feature in feature_set_ngram_bytecode:
        dtype_dict[each_feature] = float
    for each_feature in feature_set_ngram_all:
        dtype_dict[each_feature] = float
    for each_feature in feature_set_operands_tf_idf:
        dtype_dict[each_feature] = float

    df = pd.read_csv(multi_csv, dtype=dtype_dict)
    status_dict=df['category'].unique().tolist()
    df['transformed']=df['category'].apply(lambda x:status_dict.index(x))
    new_df = df.drop(['category'], axis=1)
    features = df[with_time_list + feature_set_opcode_tf_idf + feature_set_ngram_bytecode + feature_set_ngram_all + feature_set_operands_tf_idf]
    feature_label = df['transformed']
    features = np.nan_to_num(features.astype(np.float32))
    feature_label = np.nan_to_num(feature_label.astype(np.float32))
    lgb_clf = lgb.LGBMClassifier(max_delta_step = 8, max_depth = 8, num_leaves = 21)
    lgb_clf.fit(features, feature_label)

    converted_list = with_time_list + feature_set_opcode_tf_idf + feature_set_ngram_bytecode + feature_set_ngram_all + feature_set_operands_tf_idf

    df_feature_importance = (pd.DataFrame({'feature': lgb_clf.feature_name_, 'importance': lgb_clf.feature_importances_,}).sort_values('importance', ascending=False))
    feature_names = df_feature_importance['feature'].tolist()
    scores = df_feature_importance['importance'].tolist()

    new_name = []
    for name in feature_names:
        new_name.append(name[7:])

    ranked_list = []
    for name in new_name:
        ranked_list.append(converted_list[int(name)])
    top_ranked_list = ranked_list[0:top_many]
    i = 0
    for real_feature_name in top_ranked_list:
        if real_feature_name.split(" ")[0] not in top_features_xgboost_multi:
            top_features_xgboost_multi.append(real_feature_name.split(" ")[0])
        if real_feature_name.split(" ")[0] in top_features_xgboost_multi_score:
            top_features_xgboost_multi_score[real_feature_name.split(" ")[0]] = top_features_xgboost_multi_score[real_feature_name.split(" ")[0]] + scores[i]
        else:
            top_features_xgboost_multi_score[real_feature_name.split(" ")[0]] = scores[i]
        i = i + 1
with open('top_features_lightgbm_multi.txt', 'a') as newfile:
        newfile.write(str(top_features_xgboost_multi) + '\n')
with open('top_features_lightgbm_multi.txt', 'a') as newfile:
        newfile.write(str(top_features_xgboost_multi_score) + '\n')
for name, score in top_features_xgboost_multi_score.items():
    with open('top_features_lightgbm_multi.txt', 'a') as newfile:
        newfile.write(name + ' ' + str(score) + '\n')

#xgboost binary
top_features_xgboost_binary = []
top_features_xgboost_binary_score = {}
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
    for each_feature in feature_set_opcode_tf_idf:
        dtype_dict[each_feature] = float
    for each_feature in feature_set_ngram_bytecode:
        dtype_dict[each_feature] = float
    for each_feature in feature_set_ngram_all:
        dtype_dict[each_feature] = float
    for each_feature in feature_set_operands_tf_idf:
        dtype_dict[each_feature] = float

    df = pd.read_csv(binary_csv, dtype=dtype_dict)
    status_dict=df['category'].unique().tolist()
    df['transformed']=df['category'].apply(lambda x:status_dict.index(x))
    new_df = df.drop(['category'], axis=1)
    features = df[with_time_list + feature_set_opcode_tf_idf + feature_set_ngram_bytecode + feature_set_ngram_all + feature_set_operands_tf_idf]
    feature_label = df['transformed']
    features = np.nan_to_num(features.astype(np.float32))
    feature_label = np.nan_to_num(feature_label.astype(np.float32))
    xgb_clf = xgb.XGBClassifier(gamma= 0, max_delta_step= 0, max_depth= 7, min_child_weight= 5)
    xgb_clf.fit(features, feature_label)

    converted_list = with_time_list + feature_set_opcode_tf_idf + feature_set_ngram_bytecode + feature_set_ngram_all + feature_set_operands_tf_idf

    importance = xgb_clf.get_booster().get_score()
    tuples = [(k, importance[k]) for k in importance]
    tuples = sorted(tuples, key=lambda x:x[1], reverse=True)
    feature_names, scores = map(list, zip(*tuples))

    new_name = []
    for name in feature_names:
        new_name.append(name[1:])

    ranked_list = []
    for name in new_name:
        ranked_list.append(converted_list[int(name)])
    top_ranked_list = ranked_list[0:top_many]
    i = 0
    for real_feature_name in top_ranked_list:
        if real_feature_name.split(" ")[0] not in top_features_xgboost_binary:
            top_features_xgboost_binary.append(real_feature_name.split(" ")[0])
        if real_feature_name.split(" ")[0] in top_features_xgboost_binary_score:
            top_features_xgboost_binary_score[real_feature_name.split(" ")[0]] = top_features_xgboost_binary_score[real_feature_name.split(" ")[0]] + scores[i]
        else:
            top_features_xgboost_binary_score[real_feature_name.split(" ")[0]] = scores[i]
        i = i + 1
with open('top_features_xgboost_binary.txt', 'a') as newfile:
        newfile.write(str(top_features_xgboost_binary) + '\n')
with open('top_features_xgboost_binary.txt', 'a') as newfile:
        newfile.write(str(top_features_xgboost_binary_score) + '\n')
for name, score in top_features_xgboost_binary_score.items():
    with open('top_features_xgboost_binary.txt', 'a') as newfile:
        newfile.write(name + ' ' + str(score) + '\n')

#xgboost multi
top_features_xgboost_multi = []
top_features_xgboost_multi_score = {}
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
    for each_feature in feature_set_opcode_tf_idf:
        dtype_dict[each_feature] = float
    for each_feature in feature_set_ngram_bytecode:
        dtype_dict[each_feature] = float
    for each_feature in feature_set_ngram_all:
        dtype_dict[each_feature] = float
    for each_feature in feature_set_operands_tf_idf:
        dtype_dict[each_feature] = float

    df = pd.read_csv(multi_csv, dtype=dtype_dict)
    status_dict=df['category'].unique().tolist()
    df['transformed']=df['category'].apply(lambda x:status_dict.index(x))
    new_df = df.drop(['category'], axis=1)
    features = df[with_time_list + feature_set_opcode_tf_idf + feature_set_ngram_bytecode + feature_set_ngram_all + feature_set_operands_tf_idf]
    feature_label = df['transformed']
    features = np.nan_to_num(features.astype(np.float32))
    feature_label = np.nan_to_num(feature_label.astype(np.float32))
    xgb_clf = xgb.XGBClassifier(gamma= 0, max_delta_step= 0, max_depth= 7, min_child_weight= 5)
    xgb_clf.fit(features, feature_label)

    converted_list = with_time_list + feature_set_opcode_tf_idf + feature_set_ngram_bytecode + feature_set_ngram_all + feature_set_operands_tf_idf

    importance = xgb_clf.get_booster().get_score()
    tuples = [(k, importance[k]) for k in importance]
    tuples = sorted(tuples, key=lambda x:x[1], reverse=True)
    feature_names, scores = map(list, zip(*tuples))

    new_name = []
    for name in feature_names:
        new_name.append(name[1:])

    ranked_list = []
    for name in new_name:
        ranked_list.append(converted_list[int(name)])
    top_ranked_list = ranked_list[0:top_many]
    i = 0
    for real_feature_name in top_ranked_list:
        if real_feature_name.split(" ")[0] not in top_features_xgboost_multi:
            top_features_xgboost_multi.append(real_feature_name.split(" ")[0])
        if real_feature_name.split(" ")[0] in top_features_xgboost_multi_score:
            top_features_xgboost_multi_score[real_feature_name.split(" ")[0]] = top_features_xgboost_multi_score[real_feature_name.split(" ")[0]] + scores[i]
        else:
            top_features_xgboost_multi_score[real_feature_name.split(" ")[0]] = scores[i]
        i = i + 1
with open('top_features_xgboost_multi.txt', 'a') as newfile:
        newfile.write(str(top_features_xgboost_multi) + '\n')
with open('top_features_xgboost_multi.txt', 'a') as newfile:
        newfile.write(str(top_features_xgboost_multi_score) + '\n')
for name, score in top_features_xgboost_multi_score.items():
    with open('top_features_xgboost_multi.txt', 'a') as newfile:
        newfile.write(name + ' ' + str(score) + '\n')