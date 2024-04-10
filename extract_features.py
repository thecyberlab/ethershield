import os
import csv
import requests
import json
import time

output = 'dataset' # define your dataset's name and output file name here
def get_csv(apikey, csv_address, time_window_list, malicious_list):
    with open(csv_address, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            if '0x' in row[0]:
                request_and_write(apikey, row, time_window_list, malicious_list)
         
def request_and_write(apikey, row, time_window_list, malicious_list):
    url = 'https://api.etherscan.io/api?module=account&action=txlist&address=' + row[0] + '&startblock=0&endblock=99999999&page=1&offset=10000&sort=asc&apikey=' + apikey
    print(url)
    success_flag = True
    while True:
        try:
            normal_transcations = requests.get(url, timeout=25).json()
            success_flag = True
        except Exception as e:
            success_flag = False
            print(e)
        if success_flag == True:
            break
    
    url = 'https://api.etherscan.io/api?module=account&action=txlistinternal&address=' + row[0] + '&startblock=0&endblock=99999999&page=1&offset=10000&sort=asc&apikey=' + apikey
    print(url)
    success_flag = True
    while True:
        try:
            internal_transcations = requests.get(url, timeout=25).json()
            success_flag = True
        except Exception as e:
            success_flag = False
            print(e)
        if success_flag == True:
            break
    
    url = 'https://api.etherscan.io/api?module=account&action=tokentx&address='+ row[0] + '&page=1&offset=10000&startblock=0&endblock=99999999&sort=asc&apikey=' + apikey
    print(url)
    success_flag = True
    while True:
        try:
            erc_transcations = requests.get(url, timeout=25).json()
            success_flag = True
        except Exception as e:
            success_flag = False
            print(e)
        if success_flag == True:
            break
    
    url = 'https://api.etherscan.io/api?module=account&action=tokennfttx&address='+ row[0] + '&page=1&offset=10000&startblock=0&endblock=99999999&sort=asc&apikey=' + apikey
    print(url)
    success_flag = True
    while True:
        try:
            nft_transcations = requests.get(url, timeout=25).json()
            success_flag = True
        except Exception as e:
            success_flag = False
            print(e)
        if success_flag == True:
            break
    
    url = 'https://api.etherscan.io/api?module=account&action=token1155tx&address='+ row[0] + '&page=1&offset=10000&startblock=0&endblock=99999999&sort=asc&apikey=' + apikey
    print(url)
    success_flag = True
    while True:
        try:
            erc1155_transcations = requests.get(url, timeout=25).json()
            success_flag = True
        except Exception as e:
            success_flag = False
            print(e)
        if success_flag == True:
            break
    

    normal_transcations = merge_normal_internal(normal_transcations)
    internal_transcations = merge_normal_internal(internal_transcations)
    erc_transcations = merge_erc20(erc_transcations)
    nft_transcations = merge_nft(nft_transcations)
    erc1155_transcations = merge_1155(erc1155_transcations)
    merged_list = merge_transaction_list(normal_transcations, internal_transcations, erc_transcations, nft_transcations, erc1155_transcations)
    merge_without_erc_list = merge_without_erc(normal_transcations, internal_transcations)
    # with open('extract_middle/' + row[0] + '_normal', 'a') as strfile:
    #     strfile.write(str(normal_transcations))
    # with open('extract_middle/' + row[0] + '_internal', 'a') as strfile:
    #     strfile.write(str(internal_transcations))
    # with open('extract_middle/' + row[0] + '_erc20', 'a') as strfile:
    #     strfile.write(str(erc_transcations))
    # with open('extract_middle/' + row[0] + '_nft', 'a') as strfile:
    #     strfile.write(str(nft_transcations))
    # with open('extract_middle/' + row[0] + '_erc1155', 'a') as strfile:
    #     strfile.write(str(erc1155_transcations))
    # with open('extract_middle/' + row[0] + '_merge', 'a') as strfile:
    #     strfile.write(str(merged_list))
    # with open('extract_middle/' + row[0] + '_without', 'a') as strfile:
    #     strfile.write(str(merge_without_erc_list))
    current_time = 1703664376

    write_list = []
    write_list.append(row[0])
    write_list.append(row[1])
    for time_window in time_window_list:
        get_average_time_between_incoming_transactions_result_normal = get_average_time_between_incoming_transactions(apikey, row[0], time_window, normal_transcations, merged_list, current_time)
        get_average_time_between_outcoming_transactions_result_normal = get_average_time_between_outcoming_transactions(apikey, row[0], time_window, normal_transcations, merged_list, current_time)
        time_since_the_first_until_the_last_transaction_result_normal = time_since_the_first_until_the_last_transaction(apikey, row[0], time_window, normal_transcations, merged_list, current_time)
        get_longest_interval_between_two_transactions_result_normal = get_longest_interval_between_two_transactions(apikey, row[0], time_window, normal_transcations, merged_list, current_time)
        get_shortest_interval_between_two_transactions_result_normal = get_shortest_interval_between_two_transactions(apikey, row[0], time_window, normal_transcations, merged_list, current_time)
        get_total_number_of_transactions_result_normal = get_total_number_of_transactions(apikey, row[0], time_window, normal_transcations, merged_list, current_time)
        get_the_number_of_unique_outcoming_addresses_result_normal = get_the_number_of_unique_outcoming_addresses(apikey, row[0], time_window, normal_transcations, merged_list, current_time)
        get_the_number_of_unique_incoming_addresses_result_normal = get_the_number_of_unique_incoming_addresses(apikey, row[0], time_window, normal_transcations, merged_list, current_time)
        get_the_total_number_of_incoming_transactions_result_normal = get_the_total_number_of_incoming_transactions(apikey, row[0], time_window, normal_transcations, merged_list, current_time)
        get_the_total_number_of_outcoming_transactions_result_normal = get_the_total_number_of_outcoming_transactions(apikey, row[0], time_window, normal_transcations, merged_list, current_time)
        get_the_proportion_of_unique_outcoming_address_transactions_result_normal = get_the_proportion_of_unique_outcoming_address_transactions(apikey, row[0], time_window, normal_transcations, merged_list, current_time)
        get_the_proportion_of_unique_incoming_address_transactions_result_normal = get_the_proportion_of_unique_incoming_address_transactions(apikey, row[0], time_window, normal_transcations, merged_list, current_time)
        
        get_proportion_of_outcoming_address_transactions_result_normal = get_proportion_of_outcoming_address_transactions(apikey, row[0], time_window, normal_transcations, merged_list, current_time)
        get_proportion_of_incoming_address_transactions_result_normal = get_proportion_of_incoming_address_transactions(apikey, row[0], time_window, normal_transcations, merged_list, current_time)
        
        
        get_minimum_value_in_Ether_ever_received_result_normal = get_minimum_value_in_Ether_ever_received(apikey, row[0], time_window, normal_transcations, merged_list, current_time)
        get_maximum_value_in_Ether_ever_received_result_normal = get_maximum_value_in_Ether_ever_received(apikey, row[0], time_window, normal_transcations, merged_list, current_time)
        get_avg_value_in_Ether_ever_received_result_normal = get_avg_value_in_Ether_ever_received(apikey, row[0], time_window, normal_transcations, merged_list, current_time)
        get_minimum_value_in_Ether_ever_sent_result_normal = get_minimum_value_in_Ether_ever_sent(apikey, row[0], time_window, normal_transcations, merged_list, current_time)
        get_maximum_value_in_Ether_ever_sent_result_normal = get_maximum_value_in_Ether_ever_sent(apikey, row[0], time_window, normal_transcations, merged_list, current_time)
        get_avg_value_in_Ether_ever_sent_result_normal = get_avg_value_in_Ether_ever_sent(apikey, row[0], time_window, normal_transcations, merged_list, current_time)
        get_total_value_in_Ether_ever_received_result_normal = get_total_value_in_Ether_ever_received(apikey, row[0], time_window, normal_transcations, merged_list, current_time)
        get_total_value_in_Ether_ever_sent_result_normal = get_total_value_in_Ether_ever_sent(apikey, row[0], time_window, normal_transcations, merged_list, current_time)
        # get_the_initial_amount_result = get_the_initial_amount(apikey, row[0])
        # get_the_final_amount_result = get_the_final_amount(apikey, row[0])

        get_the_number_of_transactions_per_day_result_normal = get_the_number_of_transactions_per_day(apikey, row[0], time_window, normal_transcations, merged_list, current_time)
        get_the_number_of_incoming_transactions_per_day_result_normal = get_the_number_of_incoming_transactions_per_day(apikey, row[0], time_window, normal_transcations, merged_list, current_time)
        get_the_number_of_outcoming_transactions_per_day_result_normal = get_the_number_of_outcoming_transactions_per_day(apikey, row[0], time_window, normal_transcations, merged_list, current_time)
        get_the_number_of_incoming_transactions_per_hour_result_normal = get_the_number_of_incoming_transactions_per_hour(apikey, row[0], time_window, normal_transcations, merged_list, current_time)
        get_the_number_of_outcoming_transactions_per_hour_result_normal = get_the_number_of_outcoming_transactions_per_hour(apikey, row[0], time_window, normal_transcations, merged_list, current_time)
        get_the_number_of_incoming_amounts_per_day_result_normal = get_the_number_of_incoming_amounts_per_day(apikey, row[0], time_window, normal_transcations, merged_list, current_time)
        get_the_number_of_outcoming_amounts_per_day_result_normal = get_the_number_of_outcoming_amounts_per_day(apikey, row[0], time_window, normal_transcations, merged_list, current_time)
        get_the_total_number_of_amounts_outcoming_plus_incoming_result_normal = get_the_total_number_of_amounts_outcoming_plus_incoming(apikey, row[0], time_window, normal_transcations, merged_list, current_time)
        get_the_number_of_incoming_amounts_per_hour_result_normal = get_the_number_of_incoming_amounts_per_hour(apikey, row[0], time_window, normal_transcations, merged_list, current_time)
        get_the_number_of_outcoming_amounts_per_hour_result_normal = get_the_number_of_outcoming_amounts_per_hour(apikey, row[0], time_window, normal_transcations, merged_list, current_time)

        get_the_number_of_transactions_per_hour_result_normal = get_the_number_of_transactions_per_hour(apikey, row[0], time_window, normal_transcations, merged_list, current_time)
        get_the_number_of_amounts_per_day_result_normal = get_the_number_of_amounts_per_day(apikey, row[0], time_window, normal_transcations, merged_list, current_time)
        get_the_number_of_amounts_per_hour_result_normal = get_the_number_of_amounts_per_hour(apikey, row[0], time_window, normal_transcations, merged_list, current_time)
        get_reverted_numbers_result_normal = get_reverted_numbers(apikey, row[0], time_window, normal_transcations, merged_list, current_time)

        write_list.append(str(get_average_time_between_incoming_transactions_result_normal))
        write_list.append(str(get_average_time_between_outcoming_transactions_result_normal))
        write_list.append(str(time_since_the_first_until_the_last_transaction_result_normal))
        write_list.append(str(get_longest_interval_between_two_transactions_result_normal))
        write_list.append(str(get_shortest_interval_between_two_transactions_result_normal))
        write_list.append(str(get_total_number_of_transactions_result_normal))
        write_list.append(str(get_the_number_of_unique_outcoming_addresses_result_normal))
        write_list.append(str(get_the_number_of_unique_incoming_addresses_result_normal))
        write_list.append(str(get_the_total_number_of_incoming_transactions_result_normal))
        write_list.append(str(get_the_total_number_of_outcoming_transactions_result_normal))
        write_list.append(str(get_the_proportion_of_unique_outcoming_address_transactions_result_normal))
        write_list.append(str(get_the_proportion_of_unique_incoming_address_transactions_result_normal))
        write_list.append(str(get_proportion_of_outcoming_address_transactions_result_normal))
        write_list.append(str(get_proportion_of_incoming_address_transactions_result_normal))
        write_list.append(str(get_minimum_value_in_Ether_ever_received_result_normal))
        write_list.append(str(get_maximum_value_in_Ether_ever_received_result_normal))
        write_list.append(str(get_avg_value_in_Ether_ever_received_result_normal))
        write_list.append(str(get_minimum_value_in_Ether_ever_sent_result_normal))
        write_list.append(str(get_maximum_value_in_Ether_ever_sent_result_normal))
        write_list.append(str(get_avg_value_in_Ether_ever_sent_result_normal))
        write_list.append(str(get_total_value_in_Ether_ever_received_result_normal))
        write_list.append(str(get_total_value_in_Ether_ever_sent_result_normal))
        # write_list.append(str(get_the_initial_amount_result))
        # write_list.append(str(get_the_final_amount_result))
        write_list.append(str(get_the_number_of_transactions_per_day_result_normal))

        write_list.append(str(get_the_number_of_incoming_transactions_per_day_result_normal))
        write_list.append(str(get_the_number_of_outcoming_transactions_per_day_result_normal))
        write_list.append(str(get_the_number_of_incoming_transactions_per_hour_result_normal))
        write_list.append(str(get_the_number_of_outcoming_transactions_per_hour_result_normal))
        write_list.append(str(get_the_number_of_incoming_amounts_per_day_result_normal))
        write_list.append(str(get_the_number_of_outcoming_amounts_per_day_result_normal))
        write_list.append(str(get_the_total_number_of_amounts_outcoming_plus_incoming_result_normal))
        write_list.append(str(get_the_number_of_incoming_amounts_per_hour_result_normal))
        write_list.append(str(get_the_number_of_outcoming_amounts_per_hour_result_normal))

        write_list.append(str(get_the_number_of_transactions_per_hour_result_normal))
        write_list.append(str(get_the_number_of_amounts_per_day_result_normal))
        write_list.append(str(get_the_number_of_amounts_per_hour_result_normal))
        write_list.append(str(get_reverted_numbers_result_normal))

        get_average_time_between_incoming_transactions_result_internal = get_average_time_between_incoming_transactions(apikey, row[0], time_window, internal_transcations, merged_list, current_time)
        get_average_time_between_outcoming_transactions_result_internal = get_average_time_between_outcoming_transactions(apikey, row[0], time_window, internal_transcations, merged_list, current_time)
        time_since_the_first_until_the_last_transaction_result_internal = time_since_the_first_until_the_last_transaction(apikey, row[0], time_window, internal_transcations, merged_list, current_time)
        get_longest_interval_between_two_transactions_result_internal = get_longest_interval_between_two_transactions(apikey, row[0], time_window, internal_transcations, merged_list, current_time)
        get_shortest_interval_between_two_transactions_result_internal = get_shortest_interval_between_two_transactions(apikey, row[0], time_window, internal_transcations, merged_list, current_time)
        get_total_number_of_transactions_result_internal = get_total_number_of_transactions(apikey, row[0], time_window, internal_transcations, merged_list, current_time)
        get_the_number_of_unique_outcoming_addresses_result_internal = get_the_number_of_unique_outcoming_addresses(apikey, row[0], time_window, internal_transcations, merged_list, current_time)
        get_the_number_of_unique_incoming_addresses_result_internal = get_the_number_of_unique_incoming_addresses(apikey, row[0], time_window, internal_transcations, merged_list, current_time)
        get_the_total_number_of_incoming_transactions_result_internal = get_the_total_number_of_incoming_transactions(apikey, row[0], time_window, internal_transcations, merged_list, current_time)
        get_the_total_number_of_outcoming_transactions_result_internal = get_the_total_number_of_outcoming_transactions(apikey, row[0], time_window, internal_transcations, merged_list, current_time)

        get_the_proportion_of_unique_outcoming_address_transactions_result_internal = get_the_proportion_of_unique_outcoming_address_transactions(apikey, row[0], time_window, internal_transcations, merged_list, current_time)
        get_the_proportion_of_unique_incoming_address_transactions_result_internal = get_the_proportion_of_unique_incoming_address_transactions(apikey, row[0], time_window, internal_transcations, merged_list, current_time)
        get_proportion_of_outcoming_address_transactions_result_internal = get_proportion_of_outcoming_address_transactions(apikey, row[0], time_window, internal_transcations, merged_list, current_time)
        get_proportion_of_incoming_address_transactions_result_internal = get_proportion_of_incoming_address_transactions(apikey, row[0], time_window, internal_transcations, merged_list, current_time)

        get_minimum_value_in_Ether_ever_received_result_internal = get_minimum_value_in_Ether_ever_received(apikey, row[0], time_window, internal_transcations, merged_list, current_time)
        get_maximum_value_in_Ether_ever_received_result_internal= get_maximum_value_in_Ether_ever_received(apikey, row[0], time_window, internal_transcations, merged_list, current_time)
        get_avg_value_in_Ether_ever_received_result_internal = get_avg_value_in_Ether_ever_received(apikey, row[0], time_window, internal_transcations, merged_list, current_time)
        get_minimum_value_in_Ether_ever_sent_result_internal = get_minimum_value_in_Ether_ever_sent(apikey, row[0], time_window, internal_transcations, merged_list, current_time)
        get_maximum_value_in_Ether_ever_sent_result_internal = get_maximum_value_in_Ether_ever_sent(apikey, row[0], time_window, internal_transcations, merged_list, current_time)
        get_avg_value_in_Ether_ever_sent_result_internal = get_avg_value_in_Ether_ever_sent(apikey, row[0], time_window, internal_transcations, merged_list, current_time)
        get_total_value_in_Ether_ever_received_result_internal = get_total_value_in_Ether_ever_received(apikey, row[0], time_window, internal_transcations, merged_list, current_time)
        get_total_value_in_Ether_ever_sent_result_internal = get_total_value_in_Ether_ever_sent(apikey, row[0], time_window, internal_transcations, merged_list, current_time)
        # get_the_initial_amount_result = get_the_initial_amount(apikey, row[0])
        # get_the_final_amount_result = get_the_final_amount(apikey, row[0])
        get_the_number_of_transactions_per_day_result_internal = get_the_number_of_transactions_per_day(apikey, row[0], time_window, internal_transcations, merged_list, current_time)

        get_the_number_of_incoming_transactions_per_day_result_internal = get_the_number_of_incoming_transactions_per_day(apikey, row[0], time_window, internal_transcations, merged_list, current_time)
        get_the_number_of_outcoming_transactions_per_day_result_internal = get_the_number_of_outcoming_transactions_per_day(apikey, row[0], time_window, internal_transcations, merged_list, current_time)
        get_the_number_of_incoming_transactions_per_hour_result_internal = get_the_number_of_incoming_transactions_per_hour(apikey, row[0], time_window, internal_transcations, merged_list, current_time)
        get_the_number_of_outcoming_transactions_per_hour_result_internal = get_the_number_of_outcoming_transactions_per_hour(apikey, row[0], time_window, internal_transcations, merged_list, current_time)
        get_the_number_of_incoming_amounts_per_day_result_internal = get_the_number_of_incoming_amounts_per_day(apikey, row[0], time_window, internal_transcations, merged_list, current_time)
        get_the_number_of_outcoming_amounts_per_day_result_internal = get_the_number_of_outcoming_amounts_per_day(apikey, row[0], time_window, internal_transcations, merged_list, current_time)
        get_the_total_number_of_amounts_outcoming_plus_incoming_result_internal = get_the_total_number_of_amounts_outcoming_plus_incoming(apikey, row[0], time_window, internal_transcations, merged_list, current_time)
        get_the_number_of_incoming_amounts_per_hour_result_internal = get_the_number_of_incoming_amounts_per_hour(apikey, row[0], time_window, internal_transcations, merged_list, current_time)
        get_the_number_of_outcoming_amounts_per_hour_result_internal = get_the_number_of_outcoming_amounts_per_hour(apikey, row[0], time_window, internal_transcations, merged_list, current_time)

        get_the_number_of_transactions_per_hour_result_internal = get_the_number_of_transactions_per_hour(apikey, row[0], time_window, internal_transcations, merged_list, current_time)
        get_the_number_of_amounts_per_day_result_internal = get_the_number_of_amounts_per_day(apikey, row[0], time_window, internal_transcations, merged_list, current_time)
        get_the_number_of_amounts_per_hour_result_internal = get_the_number_of_amounts_per_hour(apikey, row[0], time_window, internal_transcations, merged_list, current_time)
        get_reverted_numbers_result_internal = get_reverted_numbers(apikey, row[0], time_window, internal_transcations, merged_list, current_time)

        write_list.append(str(get_average_time_between_incoming_transactions_result_internal))
        write_list.append(str(get_average_time_between_outcoming_transactions_result_internal))
        write_list.append(str(time_since_the_first_until_the_last_transaction_result_internal))
        write_list.append(str(get_longest_interval_between_two_transactions_result_internal))
        write_list.append(str(get_shortest_interval_between_two_transactions_result_internal))
        write_list.append(str(get_total_number_of_transactions_result_internal))
        write_list.append(str(get_the_number_of_unique_outcoming_addresses_result_internal))
        write_list.append(str(get_the_number_of_unique_incoming_addresses_result_internal))
        write_list.append(str(get_the_total_number_of_incoming_transactions_result_internal))
        write_list.append(str(get_the_total_number_of_outcoming_transactions_result_internal))
        write_list.append(str(get_the_proportion_of_unique_outcoming_address_transactions_result_internal))
        write_list.append(str(get_the_proportion_of_unique_incoming_address_transactions_result_internal))
        write_list.append(str(get_proportion_of_outcoming_address_transactions_result_internal))
        write_list.append(str(get_proportion_of_incoming_address_transactions_result_internal))
        write_list.append(str(get_minimum_value_in_Ether_ever_received_result_internal))
        write_list.append(str(get_maximum_value_in_Ether_ever_received_result_internal))
        write_list.append(str(get_avg_value_in_Ether_ever_received_result_internal))
        write_list.append(str(get_minimum_value_in_Ether_ever_sent_result_internal))
        write_list.append(str(get_maximum_value_in_Ether_ever_sent_result_internal))
        write_list.append(str(get_avg_value_in_Ether_ever_sent_result_internal))
        write_list.append(str(get_total_value_in_Ether_ever_received_result_internal))
        write_list.append(str(get_total_value_in_Ether_ever_sent_result_internal))
        # write_list.append(str(get_the_initial_amount_result))
        # write_list.append(str(get_the_final_amount_result))
        write_list.append(str(get_the_number_of_transactions_per_day_result_internal))

        write_list.append(str(get_the_number_of_incoming_transactions_per_day_result_internal))
        write_list.append(str(get_the_number_of_outcoming_transactions_per_day_result_internal))
        write_list.append(str(get_the_number_of_incoming_transactions_per_hour_result_internal))
        write_list.append(str(get_the_number_of_outcoming_transactions_per_hour_result_internal))
        write_list.append(str(get_the_number_of_incoming_amounts_per_day_result_internal))
        write_list.append(str(get_the_number_of_outcoming_amounts_per_day_result_internal))
        write_list.append(str(get_the_total_number_of_amounts_outcoming_plus_incoming_result_internal))
        write_list.append(str(get_the_number_of_incoming_amounts_per_hour_result_internal))
        write_list.append(str(get_the_number_of_outcoming_amounts_per_hour_result_internal))

        write_list.append(str(get_the_number_of_transactions_per_hour_result_internal))
        write_list.append(str(get_the_number_of_amounts_per_day_result_internal))
        write_list.append(str(get_the_number_of_amounts_per_hour_result_internal))
        write_list.append(str(get_reverted_numbers_result_internal))

        get_average_time_between_incoming_transactions_result_erc20 = get_average_time_between_incoming_transactions(apikey, row[0], time_window, erc_transcations, merged_list, current_time)
        get_average_time_between_outcoming_transactions_result_erc20 = get_average_time_between_outcoming_transactions(apikey, row[0], time_window, erc_transcations, merged_list, current_time)
        time_since_the_first_until_the_last_transaction_result_erc20 = time_since_the_first_until_the_last_transaction(apikey, row[0], time_window, erc_transcations, merged_list, current_time)
        get_longest_interval_between_two_transactions_result_erc20 = get_longest_interval_between_two_transactions(apikey, row[0], time_window, erc_transcations, merged_list, current_time)
        get_shortest_interval_between_two_transactions_result_erc20 = get_shortest_interval_between_two_transactions(apikey, row[0], time_window, erc_transcations, merged_list, current_time)
        get_total_number_of_transactions_result_erc20 = get_total_number_of_transactions(apikey, row[0], time_window, erc_transcations, merged_list, current_time)
        get_the_number_of_unique_outcoming_addresses_result_erc20 = get_the_number_of_unique_outcoming_addresses(apikey, row[0], time_window, erc_transcations, merged_list, current_time)
        get_the_number_of_unique_incoming_addresses_result_erc20 = get_the_number_of_unique_incoming_addresses(apikey, row[0], time_window, erc_transcations, merged_list, current_time)
        get_the_total_number_of_incoming_transactions_result_erc20 = get_the_total_number_of_incoming_transactions(apikey, row[0], time_window, erc_transcations, merged_list, current_time)
        get_the_total_number_of_outcoming_transactions_result_erc20 = get_the_total_number_of_outcoming_transactions(apikey, row[0], time_window, erc_transcations, merged_list, current_time)
        get_the_proportion_of_unique_outcoming_address_transactions_result_erc20 = get_the_proportion_of_unique_outcoming_address_transactions(apikey, row[0], time_window, erc_transcations, merged_list, current_time)
        get_the_proportion_of_unique_incoming_address_transactions_result_erc20 = get_the_proportion_of_unique_incoming_address_transactions(apikey, row[0], time_window, erc_transcations, merged_list, current_time)
        get_proportion_of_outcoming_address_transactions_result_erc20 = get_proportion_of_outcoming_address_transactions(apikey, row[0], time_window, erc_transcations, merged_list, current_time)
        get_proportion_of_incoming_address_transactions_result_erc20= get_proportion_of_incoming_address_transactions(apikey, row[0], time_window, erc_transcations, merged_list, current_time)
        get_minimum_value_in_Ether_ever_received_result_erc20 = get_minimum_value_in_Ether_ever_received(apikey, row[0], time_window, erc_transcations, merged_list, current_time)
        get_maximum_value_in_Ether_ever_received_result_erc20 = get_maximum_value_in_Ether_ever_received(apikey, row[0], time_window, erc_transcations, merged_list, current_time)
        get_avg_value_in_Ether_ever_received_result_erc20 = get_avg_value_in_Ether_ever_received(apikey, row[0], time_window, erc_transcations, merged_list, current_time)
        get_minimum_value_in_Ether_ever_sent_result_erc20 = get_minimum_value_in_Ether_ever_sent(apikey, row[0], time_window, erc_transcations, merged_list, current_time)
        get_maximum_value_in_Ether_ever_sent_result_erc20 = get_maximum_value_in_Ether_ever_sent(apikey, row[0], time_window, erc_transcations, merged_list, current_time)
        get_avg_value_in_Ether_ever_sent_result_erc20 = get_avg_value_in_Ether_ever_sent(apikey, row[0], time_window, erc_transcations, merged_list, current_time)
        get_total_value_in_Ether_ever_received_result_erc20 = get_total_value_in_Ether_ever_received(apikey, row[0], time_window, erc_transcations, merged_list, current_time)
        get_total_value_in_Ether_ever_sent_result_erc20 = get_total_value_in_Ether_ever_sent(apikey, row[0], time_window, erc_transcations, merged_list, current_time)
        # get_the_initial_amount_result = get_the_initial_amount(apikey, row[0])
        # get_the_final_amount_result = get_the_final_amount(apikey, row[0])
        get_the_number_of_transactions_per_day_result_erc20 = get_the_number_of_transactions_per_day(apikey, row[0], time_window, erc_transcations, merged_list, current_time)

        get_the_number_of_incoming_transactions_per_day_result_erc20 = get_the_number_of_incoming_transactions_per_day(apikey, row[0], time_window, erc_transcations, merged_list, current_time)
        get_the_number_of_outcoming_transactions_per_day_result_erc20 = get_the_number_of_outcoming_transactions_per_day(apikey, row[0], time_window, erc_transcations, merged_list, current_time)
        get_the_number_of_incoming_transactions_per_hour_result_erc20 = get_the_number_of_incoming_transactions_per_hour(apikey, row[0], time_window, erc_transcations, merged_list, current_time)
        get_the_number_of_outcoming_transactions_per_hour_result_erc20 = get_the_number_of_outcoming_transactions_per_hour(apikey, row[0], time_window, erc_transcations, merged_list, current_time)
        get_the_number_of_incoming_amounts_per_day_result_erc20 = get_the_number_of_incoming_amounts_per_day(apikey, row[0], time_window, erc_transcations, merged_list, current_time)
        get_the_number_of_outcoming_amounts_per_day_result_erc20 = get_the_number_of_outcoming_amounts_per_day(apikey, row[0], time_window, erc_transcations, merged_list, current_time)
        get_the_total_number_of_amounts_outcoming_plus_incoming_result_erc20 = get_the_total_number_of_amounts_outcoming_plus_incoming(apikey, row[0], time_window, erc_transcations, merged_list, current_time)
        get_the_number_of_incoming_amounts_per_hour_result_erc20 = get_the_number_of_incoming_amounts_per_hour(apikey, row[0], time_window, erc_transcations, merged_list, current_time)
        get_the_number_of_outcoming_amounts_per_hour_result_erc20 = get_the_number_of_outcoming_amounts_per_hour(apikey, row[0], time_window, erc_transcations, merged_list, current_time)

        get_the_number_of_transactions_per_hour_result_erc20 = get_the_number_of_transactions_per_hour(apikey, row[0], time_window, erc_transcations, merged_list, current_time)
        get_the_number_of_amounts_per_day_result_erc20 = get_the_number_of_amounts_per_day(apikey, row[0], time_window, erc_transcations, merged_list, current_time)
        get_the_number_of_amounts_per_hour_result_erc20 = get_the_number_of_amounts_per_hour(apikey, row[0], time_window, erc_transcations, merged_list, current_time)

        write_list.append(str(get_average_time_between_incoming_transactions_result_erc20))
        write_list.append(str(get_average_time_between_outcoming_transactions_result_erc20))
        write_list.append(str(time_since_the_first_until_the_last_transaction_result_erc20))
        write_list.append(str(get_longest_interval_between_two_transactions_result_erc20))
        write_list.append(str(get_shortest_interval_between_two_transactions_result_erc20))
        write_list.append(str(get_total_number_of_transactions_result_erc20))
        write_list.append(str(get_the_number_of_unique_outcoming_addresses_result_erc20))
        write_list.append(str(get_the_number_of_unique_incoming_addresses_result_erc20))
        write_list.append(str(get_the_total_number_of_incoming_transactions_result_erc20))
        write_list.append(str(get_the_total_number_of_outcoming_transactions_result_erc20))
        write_list.append(str(get_the_proportion_of_unique_outcoming_address_transactions_result_erc20))
        write_list.append(str(get_the_proportion_of_unique_incoming_address_transactions_result_erc20))
        write_list.append(str(get_proportion_of_outcoming_address_transactions_result_erc20))
        write_list.append(str(get_proportion_of_incoming_address_transactions_result_erc20))
        write_list.append(str(get_minimum_value_in_Ether_ever_received_result_erc20))
        write_list.append(str(get_maximum_value_in_Ether_ever_received_result_erc20))
        write_list.append(str(get_avg_value_in_Ether_ever_received_result_erc20))
        write_list.append(str(get_minimum_value_in_Ether_ever_sent_result_erc20))
        write_list.append(str(get_maximum_value_in_Ether_ever_sent_result_erc20))
        write_list.append(str(get_avg_value_in_Ether_ever_sent_result_erc20))
        write_list.append(str(get_total_value_in_Ether_ever_received_result_erc20))
        write_list.append(str(get_total_value_in_Ether_ever_sent_result_erc20))
        # write_list.append(str(get_the_initial_amount_result))
        # write_list.append(str(get_the_final_amount_result))
        write_list.append(str(get_the_number_of_transactions_per_day_result_erc20))

        write_list.append(str(get_the_number_of_incoming_transactions_per_day_result_erc20))
        write_list.append(str(get_the_number_of_outcoming_transactions_per_day_result_erc20))
        write_list.append(str(get_the_number_of_incoming_transactions_per_hour_result_erc20))
        write_list.append(str(get_the_number_of_outcoming_transactions_per_hour_result_erc20))
        write_list.append(str(get_the_number_of_incoming_amounts_per_day_result_erc20))

        write_list.append(str(get_the_number_of_outcoming_amounts_per_day_result_erc20))
        write_list.append(str(get_the_total_number_of_amounts_outcoming_plus_incoming_result_erc20))
        write_list.append(str(get_the_number_of_incoming_amounts_per_hour_result_erc20))
        write_list.append(str(get_the_number_of_outcoming_amounts_per_hour_result_erc20))

        write_list.append(str(get_the_number_of_transactions_per_hour_result_erc20))
        write_list.append(str(get_the_number_of_amounts_per_day_result_erc20))
        write_list.append(str(get_the_number_of_amounts_per_hour_result_erc20))


        get_average_time_between_incoming_transactions_result_nft_transcations = get_average_time_between_incoming_transactions(apikey, row[0], time_window, nft_transcations, merged_list, current_time)
        get_average_time_between_outcoming_transactions_result_nft_transcations = get_average_time_between_outcoming_transactions(apikey, row[0], time_window, nft_transcations, merged_list, current_time)
        time_since_the_first_until_the_last_transaction_result_nft_transcations = time_since_the_first_until_the_last_transaction(apikey, row[0], time_window, nft_transcations, merged_list, current_time)
        get_longest_interval_between_two_transactions_result_nft_transcations = get_longest_interval_between_two_transactions(apikey, row[0], time_window, nft_transcations, merged_list, current_time)
        get_shortest_interval_between_two_transactions_result_nft_transcations = get_shortest_interval_between_two_transactions(apikey, row[0], time_window, nft_transcations, merged_list, current_time)
        get_total_number_of_transactions_result_nft_transcations = get_total_number_of_transactions(apikey, row[0], time_window, nft_transcations, merged_list, current_time)
        get_the_number_of_unique_outcoming_addresses_result_nft_transcations = get_the_number_of_unique_outcoming_addresses(apikey, row[0], time_window, nft_transcations, merged_list, current_time)
        get_the_number_of_unique_incoming_addresses_result_nft_transcations = get_the_number_of_unique_incoming_addresses(apikey, row[0], time_window, nft_transcations, merged_list, current_time)
        get_the_total_number_of_incoming_transactions_result_nft_transcations = get_the_total_number_of_incoming_transactions(apikey, row[0], time_window, nft_transcations, merged_list, current_time)
        get_the_total_number_of_outcoming_transactions_result_nft_transcations = get_the_total_number_of_outcoming_transactions(apikey, row[0], time_window, nft_transcations, merged_list, current_time)
        get_the_proportion_of_unique_outcoming_address_transactions_result_nft_transcations = get_the_proportion_of_unique_outcoming_address_transactions(apikey, row[0], time_window, nft_transcations, merged_list, current_time)
        get_the_proportion_of_unique_incoming_address_transactions_result_nft_transcations = get_the_proportion_of_unique_incoming_address_transactions(apikey, row[0], time_window, nft_transcations, merged_list, current_time)
        get_proportion_of_outcoming_address_transactions_result_nft_transcations = get_proportion_of_outcoming_address_transactions(apikey, row[0], time_window, nft_transcations, merged_list, current_time)
        get_proportion_of_incoming_address_transactions_result_nft_transcations = get_proportion_of_incoming_address_transactions(apikey, row[0], time_window, nft_transcations, merged_list, current_time)
        get_minimum_value_in_Ether_ever_received_result_nft_transcations = get_minimum_value_in_Ether_ever_received(apikey, row[0], time_window, nft_transcations, merged_list, current_time)
        get_maximum_value_in_Ether_ever_received_result_nft_transcations = get_maximum_value_in_Ether_ever_received(apikey, row[0], time_window, nft_transcations, merged_list, current_time)
        get_avg_value_in_Ether_ever_received_result_nft_transcations = get_avg_value_in_Ether_ever_received(apikey, row[0], time_window, nft_transcations, merged_list, current_time)
        get_minimum_value_in_Ether_ever_sent_result_nft_transcations = get_minimum_value_in_Ether_ever_sent(apikey, row[0], time_window, nft_transcations, merged_list, current_time)
        get_maximum_value_in_Ether_ever_sent_result_nft_transcations = get_maximum_value_in_Ether_ever_sent(apikey, row[0], time_window, nft_transcations, merged_list, current_time)
        get_avg_value_in_Ether_ever_sent_result_nft_transcations = get_avg_value_in_Ether_ever_sent(apikey, row[0], time_window, nft_transcations, merged_list, current_time)
        get_total_value_in_Ether_ever_received_result_nft_transcations = get_total_value_in_Ether_ever_received(apikey, row[0], time_window, nft_transcations, merged_list, current_time)
        get_total_value_in_Ether_ever_sent_result_nft_transcations = get_total_value_in_Ether_ever_sent(apikey, row[0], time_window, nft_transcations, merged_list, current_time)
        # get_the_initial_amount_result = get_the_initial_amount(apikey, row[0])
        # get_the_final_amount_result = get_the_final_amount(apikey, row[0])
        get_the_number_of_transactions_per_day_result_nft_transcations = get_the_number_of_transactions_per_day(apikey, row[0], time_window, nft_transcations, merged_list, current_time)

        get_the_number_of_incoming_transactions_per_day_result_nft_transcations = get_the_number_of_incoming_transactions_per_day(apikey, row[0], time_window, nft_transcations, merged_list, current_time)
        get_the_number_of_outcoming_transactions_per_day_result_nft_transcations = get_the_number_of_outcoming_transactions_per_day(apikey, row[0], time_window, nft_transcations, merged_list, current_time)
        get_the_number_of_incoming_transactions_per_hour_result_nft_transcations = get_the_number_of_incoming_transactions_per_hour(apikey, row[0], time_window, nft_transcations, merged_list, current_time)
        get_the_number_of_outcoming_transactions_per_hour_result_nft_transcations = get_the_number_of_outcoming_transactions_per_hour(apikey, row[0], time_window, nft_transcations, merged_list, current_time)
        get_the_number_of_incoming_amounts_per_day_result_nft_transcations = get_the_number_of_incoming_amounts_per_day(apikey, row[0], time_window, nft_transcations, merged_list, current_time)
        get_the_number_of_outcoming_amounts_per_day_result_nft_transcations = get_the_number_of_outcoming_amounts_per_day(apikey, row[0], time_window, nft_transcations, merged_list, current_time)
        get_the_total_number_of_amounts_outcoming_plus_incoming_result_nft_transcations = get_the_total_number_of_amounts_outcoming_plus_incoming(apikey, row[0], time_window, nft_transcations, merged_list, current_time)
        get_the_number_of_incoming_amounts_per_hour_result_nft_transcations = get_the_number_of_incoming_amounts_per_hour(apikey, row[0], time_window, nft_transcations, merged_list, current_time)
        get_the_number_of_outcoming_amounts_per_hour_result_nft_transcations = get_the_number_of_outcoming_amounts_per_hour(apikey, row[0], time_window, nft_transcations, merged_list, current_time)

        get_the_number_of_transactions_per_hour_result_nft_transcations = get_the_number_of_transactions_per_hour(apikey, row[0], time_window, nft_transcations, merged_list, current_time)
        get_the_number_of_amounts_per_day_result_nft_transcations = get_the_number_of_amounts_per_day(apikey, row[0], time_window, nft_transcations, merged_list, current_time)
        get_the_number_of_amounts_per_hour_result_nft_transcations = get_the_number_of_amounts_per_hour(apikey, row[0], time_window, nft_transcations, merged_list, current_time)

        write_list.append(str(get_average_time_between_incoming_transactions_result_nft_transcations))
        write_list.append(str(get_average_time_between_outcoming_transactions_result_nft_transcations))
        write_list.append(str(time_since_the_first_until_the_last_transaction_result_nft_transcations))
        write_list.append(str(get_longest_interval_between_two_transactions_result_nft_transcations))
        write_list.append(str(get_shortest_interval_between_two_transactions_result_nft_transcations))
        write_list.append(str(get_total_number_of_transactions_result_nft_transcations))
        write_list.append(str(get_the_number_of_unique_outcoming_addresses_result_nft_transcations))
        write_list.append(str(get_the_number_of_unique_incoming_addresses_result_nft_transcations))
        write_list.append(str(get_the_total_number_of_incoming_transactions_result_nft_transcations))
        write_list.append(str(get_the_total_number_of_outcoming_transactions_result_nft_transcations))
        write_list.append(str(get_the_proportion_of_unique_outcoming_address_transactions_result_nft_transcations))
        write_list.append(str(get_the_proportion_of_unique_incoming_address_transactions_result_nft_transcations))
        write_list.append(str(get_proportion_of_outcoming_address_transactions_result_nft_transcations))
        write_list.append(str(get_proportion_of_incoming_address_transactions_result_nft_transcations))
        write_list.append(str(get_minimum_value_in_Ether_ever_received_result_nft_transcations))
        write_list.append(str(get_maximum_value_in_Ether_ever_received_result_nft_transcations))
        write_list.append(str(get_avg_value_in_Ether_ever_received_result_nft_transcations))
        write_list.append(str(get_minimum_value_in_Ether_ever_sent_result_nft_transcations))
        write_list.append(str(get_maximum_value_in_Ether_ever_sent_result_nft_transcations))
        write_list.append(str(get_avg_value_in_Ether_ever_sent_result_nft_transcations))
        write_list.append(str(get_total_value_in_Ether_ever_received_result_nft_transcations))
        write_list.append(str(get_total_value_in_Ether_ever_sent_result_nft_transcations))
        # write_list.append(str(get_the_initial_amount_result))
        # write_list.append(str(get_the_final_amount_result))
        write_list.append(str(get_the_number_of_transactions_per_day_result_nft_transcations))

        write_list.append(str(get_the_number_of_incoming_transactions_per_day_result_nft_transcations))
        write_list.append(str(get_the_number_of_outcoming_transactions_per_day_result_nft_transcations))
        write_list.append(str(get_the_number_of_incoming_transactions_per_hour_result_nft_transcations))
        write_list.append(str(get_the_number_of_outcoming_transactions_per_hour_result_nft_transcations))
        write_list.append(str(get_the_number_of_incoming_amounts_per_day_result_nft_transcations))

        write_list.append(str(get_the_number_of_outcoming_amounts_per_day_result_nft_transcations))
        write_list.append(str(get_the_total_number_of_amounts_outcoming_plus_incoming_result_nft_transcations))
        write_list.append(str(get_the_number_of_incoming_amounts_per_hour_result_nft_transcations))
        write_list.append(str(get_the_number_of_outcoming_amounts_per_hour_result_nft_transcations))

        write_list.append(str(get_the_number_of_transactions_per_hour_result_nft_transcations))
        write_list.append(str(get_the_number_of_amounts_per_day_result_nft_transcations))
        write_list.append(str(get_the_number_of_amounts_per_hour_result_nft_transcations))

        get_average_time_between_incoming_transactions_result_erc1155_transcations = get_average_time_between_incoming_transactions(apikey, row[0], time_window, erc1155_transcations, merged_list, current_time)
        get_average_time_between_outcoming_transactions_result_erc1155_transcations = get_average_time_between_outcoming_transactions(apikey, row[0], time_window, erc1155_transcations, merged_list, current_time)
        time_since_the_first_until_the_last_transaction_result_erc1155_transcations = time_since_the_first_until_the_last_transaction(apikey, row[0], time_window, erc1155_transcations, merged_list, current_time)
        get_longest_interval_between_two_transactions_result_erc1155_transcations = get_longest_interval_between_two_transactions(apikey, row[0], time_window, erc1155_transcations, merged_list, current_time)
        get_shortest_interval_between_two_transactions_result_erc1155_transcations = get_shortest_interval_between_two_transactions(apikey, row[0], time_window, erc1155_transcations, merged_list, current_time)
        get_total_number_of_transactions_result_erc1155_transcations = get_total_number_of_transactions(apikey, row[0], time_window, erc1155_transcations, merged_list, current_time)
        get_the_number_of_unique_outcoming_addresses_result_erc1155_transcations = get_the_number_of_unique_outcoming_addresses(apikey, row[0], time_window, erc1155_transcations, merged_list, current_time)
        get_the_number_of_unique_incoming_addresses_result_erc1155_transcations = get_the_number_of_unique_incoming_addresses(apikey, row[0], time_window, erc1155_transcations, merged_list, current_time)
        get_the_total_number_of_incoming_transactions_result_erc1155_transcations = get_the_total_number_of_incoming_transactions(apikey, row[0], time_window, erc1155_transcations, merged_list, current_time)
        get_the_total_number_of_outcoming_transactions_result_erc1155_transcations = get_the_total_number_of_outcoming_transactions(apikey, row[0], time_window, erc1155_transcations, merged_list, current_time)
        get_the_proportion_of_unique_outcoming_address_transactions_result_erc1155_transcations = get_the_proportion_of_unique_outcoming_address_transactions(apikey, row[0], time_window, erc1155_transcations, merged_list, current_time)
        get_the_proportion_of_unique_incoming_address_transactions_result_erc1155_transcations = get_the_proportion_of_unique_incoming_address_transactions(apikey, row[0], time_window, erc1155_transcations, merged_list, current_time)
        get_proportion_of_outcoming_address_transactions_result_erc1155_transcations = get_proportion_of_outcoming_address_transactions(apikey, row[0], time_window, erc1155_transcations, merged_list, current_time)
        get_proportion_of_incoming_address_transactions_result_erc1155_transcations = get_proportion_of_incoming_address_transactions(apikey, row[0], time_window, erc1155_transcations, merged_list, current_time)
        get_minimum_value_in_Ether_ever_received_result_erc1155_transcations = get_minimum_value_in_Ether_ever_received(apikey, row[0], time_window, erc1155_transcations, merged_list, current_time)
        get_maximum_value_in_Ether_ever_received_result_erc1155_transcations = get_maximum_value_in_Ether_ever_received(apikey, row[0], time_window, erc1155_transcations, merged_list, current_time)
        get_avg_value_in_Ether_ever_received_result_erc1155_transcations = get_avg_value_in_Ether_ever_received(apikey, row[0], time_window, erc1155_transcations, merged_list, current_time)
        get_minimum_value_in_Ether_ever_sent_result_erc1155_transcations = get_minimum_value_in_Ether_ever_sent(apikey, row[0], time_window, erc1155_transcations, merged_list, current_time)
        get_maximum_value_in_Ether_ever_sent_result_erc1155_transcations = get_maximum_value_in_Ether_ever_sent(apikey, row[0], time_window, erc1155_transcations, merged_list, current_time)
        get_avg_value_in_Ether_ever_sent_result_erc1155_transcations = get_avg_value_in_Ether_ever_sent(apikey, row[0], time_window, erc1155_transcations, merged_list, current_time)
        get_total_value_in_Ether_ever_received_result_erc1155_transcations = get_total_value_in_Ether_ever_received(apikey, row[0], time_window, erc1155_transcations, merged_list, current_time)
        get_total_value_in_Ether_ever_sent_result_erc1155_transcations = get_total_value_in_Ether_ever_sent(apikey, row[0], time_window, erc1155_transcations, merged_list, current_time)
        # get_the_initial_amount_result = get_the_initial_amount(apikey, row[0])
        # get_the_final_amount_result = get_the_final_amount(apikey, row[0])
        get_the_number_of_transactions_per_day_result_erc1155_transcations = get_the_number_of_transactions_per_day(apikey, row[0], time_window, erc1155_transcations, merged_list, current_time)

        get_the_number_of_incoming_transactions_per_day_result_erc1155_transcations = get_the_number_of_incoming_transactions_per_day(apikey, row[0], time_window, erc1155_transcations, merged_list, current_time)
        get_the_number_of_outcoming_transactions_per_day_result_erc1155_transcations = get_the_number_of_outcoming_transactions_per_day(apikey, row[0], time_window, erc1155_transcations, merged_list, current_time)
        get_the_number_of_incoming_transactions_per_hour_result_erc1155_transcations = get_the_number_of_incoming_transactions_per_hour(apikey, row[0], time_window, erc1155_transcations, merged_list, current_time)
        get_the_number_of_outcoming_transactions_per_hour_result_erc1155_transcations = get_the_number_of_outcoming_transactions_per_hour(apikey, row[0], time_window, erc1155_transcations, merged_list, current_time)
        get_the_number_of_incoming_amounts_per_day_result_erc1155_transcations = get_the_number_of_incoming_amounts_per_day(apikey, row[0], time_window, erc1155_transcations, merged_list, current_time)
        get_the_number_of_outcoming_amounts_per_day_result_erc1155_transcations = get_the_number_of_outcoming_amounts_per_day(apikey, row[0], time_window, erc1155_transcations, merged_list, current_time)
        get_the_total_number_of_amounts_outcoming_plus_incoming_result_erc1155_transcations = get_the_total_number_of_amounts_outcoming_plus_incoming(apikey, row[0], time_window, erc1155_transcations, merged_list, current_time)
        get_the_number_of_incoming_amounts_per_hour_result_erc1155_transcations = get_the_number_of_incoming_amounts_per_hour(apikey, row[0], time_window, erc1155_transcations, merged_list, current_time)
        get_the_number_of_outcoming_amounts_per_hour_result_erc1155_transcations = get_the_number_of_outcoming_amounts_per_hour(apikey, row[0], time_window, erc1155_transcations, merged_list, current_time)

        get_the_number_of_transactions_per_hour_result_erc1155_transcations = get_the_number_of_transactions_per_hour(apikey, row[0], time_window, erc1155_transcations, merged_list, current_time)
        get_the_number_of_amounts_per_day_result_erc1155_transcations = get_the_number_of_amounts_per_day(apikey, row[0], time_window, erc1155_transcations, merged_list, current_time)
        get_the_number_of_amounts_per_hour_result_erc1155_transcations = get_the_number_of_amounts_per_hour(apikey, row[0], time_window, erc1155_transcations, merged_list, current_time)

        write_list.append(str(get_average_time_between_incoming_transactions_result_erc1155_transcations))
        write_list.append(str(get_average_time_between_outcoming_transactions_result_erc1155_transcations))
        write_list.append(str(time_since_the_first_until_the_last_transaction_result_erc1155_transcations))
        write_list.append(str(get_longest_interval_between_two_transactions_result_erc1155_transcations))
        write_list.append(str(get_shortest_interval_between_two_transactions_result_erc1155_transcations))
        write_list.append(str(get_total_number_of_transactions_result_erc1155_transcations))
        write_list.append(str(get_the_number_of_unique_outcoming_addresses_result_erc1155_transcations))
        write_list.append(str(get_the_number_of_unique_incoming_addresses_result_erc1155_transcations))
        write_list.append(str(get_the_total_number_of_incoming_transactions_result_erc1155_transcations))
        write_list.append(str(get_the_total_number_of_outcoming_transactions_result_erc1155_transcations))
        write_list.append(str(get_the_proportion_of_unique_outcoming_address_transactions_result_erc1155_transcations))
        write_list.append(str(get_the_proportion_of_unique_incoming_address_transactions_result_erc1155_transcations))
        write_list.append(str(get_proportion_of_outcoming_address_transactions_result_erc1155_transcations))
        write_list.append(str(get_proportion_of_incoming_address_transactions_result_erc1155_transcations))
        write_list.append(str(get_minimum_value_in_Ether_ever_received_result_erc1155_transcations))
        write_list.append(str(get_maximum_value_in_Ether_ever_received_result_erc1155_transcations))
        write_list.append(str(get_avg_value_in_Ether_ever_received_result_erc1155_transcations))
        write_list.append(str(get_minimum_value_in_Ether_ever_sent_result_erc1155_transcations))
        write_list.append(str(get_maximum_value_in_Ether_ever_sent_result_erc1155_transcations))
        write_list.append(str(get_avg_value_in_Ether_ever_sent_result_erc1155_transcations))
        write_list.append(str(get_total_value_in_Ether_ever_received_result_erc1155_transcations))
        write_list.append(str(get_total_value_in_Ether_ever_sent_result_erc1155_transcations))
        # write_list.append(str(get_the_initial_amount_result))
        # write_list.append(str(get_the_final_amount_result))
        write_list.append(str(get_the_number_of_transactions_per_day_result_erc1155_transcations))

        write_list.append(str(get_the_number_of_incoming_transactions_per_day_result_erc1155_transcations))
        write_list.append(str(get_the_number_of_outcoming_transactions_per_day_result_erc1155_transcations))
        write_list.append(str(get_the_number_of_incoming_transactions_per_hour_result_erc1155_transcations))
        write_list.append(str(get_the_number_of_outcoming_transactions_per_hour_result_erc1155_transcations))
        write_list.append(str(get_the_number_of_incoming_amounts_per_day_result_erc1155_transcations))

        write_list.append(str(get_the_number_of_outcoming_amounts_per_day_result_erc1155_transcations))
        write_list.append(str(get_the_total_number_of_amounts_outcoming_plus_incoming_result_erc1155_transcations))
        write_list.append(str(get_the_number_of_incoming_amounts_per_hour_result_erc1155_transcations))
        write_list.append(str(get_the_number_of_outcoming_amounts_per_hour_result_erc1155_transcations))

        write_list.append(str(get_the_number_of_transactions_per_hour_result_erc1155_transcations))
        write_list.append(str(get_the_number_of_amounts_per_day_result_erc1155_transcations))
        write_list.append(str(get_the_number_of_amounts_per_hour_result_erc1155_transcations))

        get_average_time_between_incoming_transactions_result_all = get_average_time_between_incoming_transactions(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_average_time_between_outcoming_transactions_result_all = get_average_time_between_outcoming_transactions(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        time_since_the_first_until_the_last_transaction_result_all = time_since_the_first_until_the_last_transaction(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_longest_interval_between_two_transactions_result_all = get_longest_interval_between_two_transactions(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_shortest_interval_between_two_transactions_result_all = get_shortest_interval_between_two_transactions(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_total_number_of_transactions_result_all = get_total_number_of_transactions(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_the_number_of_unique_outcoming_addresses_result_all = get_the_number_of_unique_outcoming_addresses(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_the_number_of_unique_incoming_addresses_result_all = get_the_number_of_unique_incoming_addresses(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_the_total_number_of_incoming_transactions_result_all = get_the_total_number_of_incoming_transactions(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_the_total_number_of_outcoming_transactions_result_all = get_the_total_number_of_outcoming_transactions(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_the_proportion_of_unique_outcoming_address_transactions_result_all = get_the_proportion_of_unique_outcoming_address_transactions(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_the_proportion_of_unique_incoming_address_transactions_result_all = get_the_proportion_of_unique_incoming_address_transactions(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_proportion_of_outcoming_address_transactions_result_all = get_proportion_of_outcoming_address_transactions(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_proportion_of_incoming_address_transactions_result_all = get_proportion_of_incoming_address_transactions(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_minimum_value_in_Ether_ever_received_result_all = get_minimum_value_in_Ether_ever_received(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_maximum_value_in_Ether_ever_received_result_all = get_maximum_value_in_Ether_ever_received(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_avg_value_in_Ether_ever_received_result_all = get_avg_value_in_Ether_ever_received(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_minimum_value_in_Ether_ever_sent_result_all = get_minimum_value_in_Ether_ever_sent(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_maximum_value_in_Ether_ever_sent_result_all = get_maximum_value_in_Ether_ever_sent(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_avg_value_in_Ether_ever_sent_result_all = get_avg_value_in_Ether_ever_sent(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_total_value_in_Ether_ever_received_result_all = get_total_value_in_Ether_ever_received(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_total_value_in_Ether_ever_sent_result_all = get_total_value_in_Ether_ever_sent(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)

        get_the_number_of_transactions_per_day_result_all = get_the_number_of_transactions_per_day(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_the_number_of_incoming_transactions_per_day_result_all = get_the_number_of_incoming_transactions_per_day(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_the_number_of_outcoming_transactions_per_day_result_all = get_the_number_of_outcoming_transactions_per_day(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_the_number_of_incoming_transactions_per_hour_result_all = get_the_number_of_incoming_transactions_per_hour(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_the_number_of_outcoming_transactions_per_hour_result_all = get_the_number_of_outcoming_transactions_per_hour(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_the_number_of_incoming_amounts_per_day_result_all = get_the_number_of_incoming_amounts_per_day(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_the_number_of_outcoming_amounts_per_day_result_all = get_the_number_of_outcoming_amounts_per_day(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_the_total_number_of_amounts_outcoming_plus_incoming_all = get_the_total_number_of_amounts_outcoming_plus_incoming(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_the_number_of_incoming_amounts_per_hour_result_all = get_the_number_of_incoming_amounts_per_hour(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_the_number_of_outcoming_amounts_per_hour_result_all = get_the_number_of_outcoming_amounts_per_hour(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)

        get_the_number_of_transactions_per_hour_result_all = get_the_number_of_transactions_per_hour(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_the_number_of_amounts_per_day_result_all = get_the_number_of_amounts_per_day(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_the_number_of_amounts_per_hour_result_all = get_the_number_of_amounts_per_hour(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_reverted_numbers_result_all = get_reverted_numbers(apikey, row[0], time_window, {'result':merge_without_erc_list}, merged_list, current_time)

        write_list.append(str(get_average_time_between_incoming_transactions_result_all))
        write_list.append(str(get_average_time_between_outcoming_transactions_result_all))
        write_list.append(str(time_since_the_first_until_the_last_transaction_result_all))
        write_list.append(str(get_longest_interval_between_two_transactions_result_all))
        write_list.append(str(get_shortest_interval_between_two_transactions_result_all))
        write_list.append(str(get_total_number_of_transactions_result_all))
        write_list.append(str(get_the_number_of_unique_outcoming_addresses_result_all))
        write_list.append(str(get_the_number_of_unique_incoming_addresses_result_all))
        write_list.append(str(get_the_total_number_of_incoming_transactions_result_all))
        write_list.append(str(get_the_total_number_of_outcoming_transactions_result_all))
        write_list.append(str(get_the_proportion_of_unique_outcoming_address_transactions_result_all))
        write_list.append(str(get_the_proportion_of_unique_incoming_address_transactions_result_all))
        write_list.append(str(get_proportion_of_outcoming_address_transactions_result_all))
        write_list.append(str(get_proportion_of_incoming_address_transactions_result_all))
        write_list.append(str(get_minimum_value_in_Ether_ever_received_result_all))
        write_list.append(str(get_maximum_value_in_Ether_ever_received_result_all))
        write_list.append(str(get_avg_value_in_Ether_ever_received_result_all))
        write_list.append(str(get_minimum_value_in_Ether_ever_sent_result_all))
        write_list.append(str(get_maximum_value_in_Ether_ever_sent_result_all))
        write_list.append(str(get_avg_value_in_Ether_ever_sent_result_all))
        write_list.append(str(get_total_value_in_Ether_ever_received_result_all))
        write_list.append(str(get_total_value_in_Ether_ever_sent_result_all))
        # write_list.append(str(get_the_initial_amount_result))
        # write_list.append(str(get_the_final_amount_result))
        write_list.append(str(get_the_number_of_transactions_per_day_result_all))

        write_list.append(str(get_the_number_of_incoming_transactions_per_day_result_all))
        write_list.append(str(get_the_number_of_outcoming_transactions_per_day_result_all))
        write_list.append(str(get_the_number_of_incoming_transactions_per_hour_result_all))
        write_list.append(str(get_the_number_of_outcoming_transactions_per_hour_result_all))
        write_list.append(str(get_the_number_of_incoming_amounts_per_day_result_all))

        write_list.append(str(get_the_number_of_outcoming_amounts_per_day_result_all))
        write_list.append(str(get_the_total_number_of_amounts_outcoming_plus_incoming_all))
        write_list.append(str(get_the_number_of_incoming_amounts_per_hour_result_all))
        write_list.append(str(get_the_number_of_outcoming_amounts_per_hour_result_all))

        write_list.append(str(get_the_number_of_transactions_per_hour_result_all))
        write_list.append(str(get_the_number_of_amounts_per_day_result_all))
        write_list.append(str(get_the_number_of_amounts_per_hour_result_all))
        write_list.append(str(get_reverted_numbers_result_all))


        get_the_propotion_of_normal_transactions_of_all_result = get_the_propotion_of_single_transactions_of_all(apikey, row[0], time_window, normal_transcations, merged_list, current_time)
        get_the_propotion_of_normal_incoming_transactions_of_all_incoming_result = get_the_propotion_of_single_incoming_transactions_of_all_incoming(apikey, row[0], time_window, normal_transcations, merged_list, current_time)
        get_the_propotion_of_normal_incoming_transactions_of_all_transactions_result = get_the_propotion_of_single_incoming_transactions_of_all_transactions(apikey, row[0], time_window, normal_transcations, merged_list, current_time)
        get_the_propotion_of_normal_outcoming_transactions_of_all_outcoming_result = get_the_propotion_of_single_outcoming_transactions_of_all_outcoming(apikey, row[0], time_window, normal_transcations, merged_list, current_time)
        get_the_propotion_of_normal_outcoming_transactions_of_all_transactions_result = get_the_propotion_of_single_outcoming_transactions_of_all_transactions(apikey, row[0], time_window, normal_transcations, merged_list, current_time)


        get_the_propotion_of_internal_transactions_of_all_result_result = get_the_propotion_of_single_transactions_of_all(apikey, row[0], time_window, internal_transcations, merged_list, current_time)
        get_the_propotion_of_internal_incoming_transactions_of_all_incoming_result = get_the_propotion_of_single_incoming_transactions_of_all_incoming(apikey, row[0], time_window, internal_transcations, merged_list, current_time)
        get_the_propotion_of_internal_incoming_transactions_of_all_transactions_result = get_the_propotion_of_single_incoming_transactions_of_all_transactions(apikey, row[0], time_window, internal_transcations, merged_list, current_time)
        get_the_propotion_of_internal_outcoming_transactions_of_all_outcoming_result = get_the_propotion_of_single_outcoming_transactions_of_all_outcoming(apikey, row[0], time_window, internal_transcations, merged_list, current_time)
        get_the_propotion_of_internal_outcoming_transactions_of_all_transactions_result = get_the_propotion_of_single_outcoming_transactions_of_all_transactions(apikey, row[0], time_window, internal_transcations, merged_list, current_time)

        get_the_propotion_of_erc20_transactions_of_all_result_result = get_the_propotion_of_single_transactions_of_all(apikey, row[0], time_window, erc_transcations, merged_list, current_time)
        get_the_propotion_of_erc20_incoming_transactions_of_all_incoming_result = get_the_propotion_of_single_incoming_transactions_of_all_incoming(apikey, row[0], time_window, erc_transcations, merged_list, current_time)
        get_the_propotion_of_erc20_incoming_transactions_of_all_transactions_result = get_the_propotion_of_single_incoming_transactions_of_all_transactions(apikey, row[0], time_window, erc_transcations, merged_list, current_time)
        get_the_propotion_of_erc20_outcoming_transactions_of_all_outcoming_result = get_the_propotion_of_single_outcoming_transactions_of_all_outcoming(apikey, row[0], time_window, erc_transcations, merged_list, current_time)
        get_the_propotion_of_erc20_outcoming_transactions_of_all_transactions_result = get_the_propotion_of_single_outcoming_transactions_of_all_transactions(apikey, row[0], time_window, erc_transcations, merged_list, current_time)

        get_the_propotion_of_nft_transactions_of_all_result_result = get_the_propotion_of_single_transactions_of_all(apikey, row[0], time_window, nft_transcations, merged_list, current_time)
        get_the_propotion_of_nft_incoming_transactions_of_all_incoming_result = get_the_propotion_of_single_incoming_transactions_of_all_incoming(apikey, row[0], time_window, nft_transcations, merged_list, current_time)
        get_the_propotion_of_nft_incoming_transactions_of_all_transactions_result = get_the_propotion_of_single_incoming_transactions_of_all_transactions(apikey, row[0], time_window, nft_transcations, merged_list, current_time)
        get_the_propotion_of_nft_outcoming_transactions_of_all_outcoming_result = get_the_propotion_of_single_outcoming_transactions_of_all_outcoming(apikey, row[0], time_window, nft_transcations, merged_list, current_time)
        get_the_propotion_of_nft_outcoming_transactions_of_all_transactions_result = get_the_propotion_of_single_outcoming_transactions_of_all_transactions(apikey, row[0], time_window, nft_transcations, merged_list, current_time)

        get_the_propotion_of_erc1155_transactions_of_all_result_result = get_the_propotion_of_single_transactions_of_all(apikey, row[0], time_window, erc1155_transcations, merged_list, current_time)
        get_the_propotion_of_erc1155_incoming_transactions_of_all_incoming_result = get_the_propotion_of_single_incoming_transactions_of_all_incoming(apikey, row[0], time_window, erc1155_transcations, merged_list, current_time)
        get_the_propotion_of_erc1155_incoming_transactions_of_all_transactions_result = get_the_propotion_of_single_incoming_transactions_of_all_transactions(apikey, row[0], time_window, erc1155_transcations, merged_list, current_time)
        get_the_propotion_of_erc1155_outcoming_transactions_of_all_outcoming_result = get_the_propotion_of_single_outcoming_transactions_of_all_outcoming(apikey, row[0], time_window, erc1155_transcations, merged_list, current_time)
        get_the_propotion_of_erc1155_outcoming_transactions_of_all_transactions_result = get_the_propotion_of_single_outcoming_transactions_of_all_transactions(apikey, row[0], time_window, erc1155_transcations, merged_list, current_time)

        get_the_propotion_of_normal_ether_transfered_of_all_result = get_the_propotion_of_single_ether_transfered_of_all(apikey, row[0], time_window, normal_transcations, merged_list, current_time)
        get_the_propotion_of_normal_ether_sent_of_all_sent_result = get_the_propotion_of_single_ether_sent_of_all_sent(apikey, row[0], time_window, normal_transcations, merged_list, current_time)
        get_the_propotion_of_normal_ether_sent_of_all_touched_result = get_the_propotion_of_single_ether_sent_of_all_touched(apikey, row[0], time_window, normal_transcations, merged_list, current_time)
        get_the_propotion_of_normal_ether_received_of_all_sent_result = get_the_propotion_of_single_ether_received_of_all_received(apikey, row[0], time_window, normal_transcations, merged_list, current_time)
        get_the_propotion_of_normal_ether_received_of_all_touched_result = get_the_propotion_of_single_ether_received_of_all_touched(apikey, row[0], time_window, normal_transcations, merged_list, current_time)

        get_the_propotion_of_internal_ether_transfered_of_all_result = get_the_propotion_of_single_ether_transfered_of_all(apikey, row[0], time_window, internal_transcations, merged_list, current_time)
        get_the_propotion_of_internal_ether_sent_of_all_sent_result = get_the_propotion_of_single_ether_sent_of_all_sent(apikey, row[0], time_window, internal_transcations, merged_list, current_time)
        get_the_propotion_of_internal_ether_sent_of_all_touched_result = get_the_propotion_of_single_ether_sent_of_all_touched(apikey, row[0], time_window, internal_transcations, merged_list, current_time)
        get_the_propotion_of_internal_ether_received_of_all_sent_result = get_the_propotion_of_single_ether_received_of_all_received(apikey, row[0], time_window, internal_transcations, merged_list, current_time)
        get_the_propotion_of_internal_ether_received_of_all_touched_result = get_the_propotion_of_single_ether_received_of_all_touched(apikey, row[0], time_window, internal_transcations, merged_list, current_time)

        get_the_propotion_of_erc20_ether_transfered_of_all_result = get_the_propotion_of_single_ether_transfered_of_all(apikey, row[0], time_window, erc_transcations, merged_list, current_time)
        get_the_propotion_of_erc20_ether_sent_of_all_sent_result = get_the_propotion_of_single_ether_sent_of_all_sent(apikey, row[0], time_window, erc_transcations, merged_list, current_time)
        get_the_propotion_of_erc20_ether_sent_of_all_touched_result = get_the_propotion_of_single_ether_sent_of_all_touched(apikey, row[0], time_window, erc_transcations, merged_list, current_time)
        get_the_propotion_of_erc20_ether_received_of_all_sent_result = get_the_propotion_of_single_ether_received_of_all_received(apikey, row[0], time_window, erc_transcations, merged_list, current_time)
        get_the_propotion_of_erc20_ether_received_of_all_touched_result = get_the_propotion_of_single_ether_received_of_all_touched(apikey, row[0], time_window, erc_transcations, merged_list, current_time)

        get_the_propotion_of_nft_ether_transfered_of_all_result = get_the_propotion_of_single_ether_transfered_of_all(apikey, row[0], time_window, nft_transcations, merged_list, current_time)
        get_the_propotion_of_nft_ether_sent_of_all_sent_result = get_the_propotion_of_single_ether_sent_of_all_sent(apikey, row[0], time_window, nft_transcations, merged_list, current_time)
        get_the_propotion_of_nft_ether_sent_of_all_touched_result = get_the_propotion_of_single_ether_sent_of_all_touched(apikey, row[0], time_window, nft_transcations, merged_list, current_time)
        get_the_propotion_of_nft_ether_received_of_all_sent_result = get_the_propotion_of_single_ether_received_of_all_received(apikey, row[0], time_window, nft_transcations, merged_list, current_time)
        get_the_propotion_of_nft_ether_received_of_all_touched_result = get_the_propotion_of_single_ether_received_of_all_touched(apikey, row[0], time_window, nft_transcations, merged_list, current_time)

        get_the_propotion_of_erc1155_ether_transfered_of_all_result = get_the_propotion_of_single_ether_transfered_of_all(apikey, row[0], time_window, erc1155_transcations, merged_list, current_time)
        get_the_propotion_of_erc1155_ether_sent_of_all_sent_result = get_the_propotion_of_single_ether_sent_of_all_sent(apikey, row[0], time_window, erc1155_transcations, merged_list, current_time)
        get_the_propotion_of_erc1155_ether_sent_of_all_touched_result = get_the_propotion_of_single_ether_sent_of_all_touched(apikey, row[0], time_window, erc1155_transcations, merged_list, current_time)
        get_the_propotion_of_erc1155_ether_received_of_all_sent_result = get_the_propotion_of_single_ether_received_of_all_received(apikey, row[0], time_window, erc1155_transcations, merged_list, current_time)
        get_the_propotion_of_erc1155_ether_received_of_all_touched_result = get_the_propotion_of_single_ether_received_of_all_touched(apikey, row[0], time_window, erc1155_transcations, merged_list, current_time)

        write_list.append(str(get_the_propotion_of_normal_transactions_of_all_result))
        write_list.append(str(get_the_propotion_of_normal_incoming_transactions_of_all_incoming_result))
        write_list.append(str(get_the_propotion_of_normal_incoming_transactions_of_all_transactions_result))
        write_list.append(str(get_the_propotion_of_normal_outcoming_transactions_of_all_outcoming_result))
        write_list.append(str(get_the_propotion_of_normal_outcoming_transactions_of_all_transactions_result))

        write_list.append(str(get_the_propotion_of_internal_transactions_of_all_result_result))
        write_list.append(str(get_the_propotion_of_internal_incoming_transactions_of_all_incoming_result))
        write_list.append(str(get_the_propotion_of_internal_incoming_transactions_of_all_transactions_result))
        write_list.append(str(get_the_propotion_of_internal_outcoming_transactions_of_all_outcoming_result))
        write_list.append(str(get_the_propotion_of_internal_outcoming_transactions_of_all_transactions_result))

        write_list.append(str(get_the_propotion_of_erc20_transactions_of_all_result_result))
        write_list.append(str(get_the_propotion_of_erc20_incoming_transactions_of_all_incoming_result))
        write_list.append(str(get_the_propotion_of_erc20_incoming_transactions_of_all_transactions_result))
        write_list.append(str(get_the_propotion_of_erc20_outcoming_transactions_of_all_outcoming_result))
        write_list.append(str(get_the_propotion_of_erc20_outcoming_transactions_of_all_transactions_result))
        
        write_list.append(str(get_the_propotion_of_nft_transactions_of_all_result_result))
        write_list.append(str(get_the_propotion_of_nft_incoming_transactions_of_all_incoming_result))
        write_list.append(str(get_the_propotion_of_nft_incoming_transactions_of_all_transactions_result))
        write_list.append(str(get_the_propotion_of_nft_outcoming_transactions_of_all_outcoming_result))
        write_list.append(str(get_the_propotion_of_nft_outcoming_transactions_of_all_transactions_result))

        write_list.append(str(get_the_propotion_of_erc1155_transactions_of_all_result_result))
        write_list.append(str(get_the_propotion_of_erc1155_incoming_transactions_of_all_incoming_result))
        write_list.append(str(get_the_propotion_of_erc1155_incoming_transactions_of_all_transactions_result))
        write_list.append(str(get_the_propotion_of_erc1155_outcoming_transactions_of_all_outcoming_result))
        write_list.append(str(get_the_propotion_of_erc1155_outcoming_transactions_of_all_transactions_result))

        write_list.append(str(get_the_propotion_of_normal_ether_transfered_of_all_result))
        write_list.append(str(get_the_propotion_of_normal_ether_sent_of_all_sent_result))
        write_list.append(str(get_the_propotion_of_normal_ether_sent_of_all_touched_result))
        write_list.append(str(get_the_propotion_of_normal_ether_received_of_all_sent_result))
        write_list.append(str(get_the_propotion_of_normal_ether_received_of_all_touched_result))

        write_list.append(str(get_the_propotion_of_internal_ether_transfered_of_all_result))
        write_list.append(str(get_the_propotion_of_internal_ether_sent_of_all_sent_result))
        write_list.append(str(get_the_propotion_of_internal_ether_sent_of_all_touched_result))
        write_list.append(str(get_the_propotion_of_internal_ether_received_of_all_sent_result))
        write_list.append(str(get_the_propotion_of_internal_ether_received_of_all_touched_result))

        write_list.append(str(get_the_propotion_of_erc20_ether_transfered_of_all_result))
        write_list.append(str(get_the_propotion_of_erc20_ether_sent_of_all_sent_result))
        write_list.append(str(get_the_propotion_of_erc20_ether_sent_of_all_touched_result))
        write_list.append(str(get_the_propotion_of_erc20_ether_received_of_all_sent_result))
        write_list.append(str(get_the_propotion_of_erc20_ether_received_of_all_touched_result))
    
        write_list.append(str(get_the_propotion_of_nft_ether_transfered_of_all_result))
        write_list.append(str(get_the_propotion_of_nft_ether_sent_of_all_sent_result))
        write_list.append(str(get_the_propotion_of_nft_ether_sent_of_all_touched_result))
        write_list.append(str(get_the_propotion_of_nft_ether_received_of_all_sent_result))
        write_list.append(str(get_the_propotion_of_nft_ether_received_of_all_touched_result))
        
        write_list.append(str(get_the_propotion_of_erc1155_ether_transfered_of_all_result))
        write_list.append(str(get_the_propotion_of_erc1155_ether_sent_of_all_sent_result))
        write_list.append(str(get_the_propotion_of_erc1155_ether_sent_of_all_touched_result))
        write_list.append(str(get_the_propotion_of_erc1155_ether_received_of_all_sent_result))
        write_list.append(str(get_the_propotion_of_erc1155_ether_received_of_all_touched_result))

        only_incoming_result = only_incoming(row[0], time_window, normal_transcations, merged_list)
        only_outcoming_result = only_outcoming(row[0], time_window, normal_transcations, merged_list)
        get_maximum_number_for_same_incoming_address_result = get_maximum_number_for_same_incoming_address(row[0], time_window, normal_transcations, merged_list)
        get_maximum_number_for_same_outcoming_address_result = get_maximum_number_for_same_outcoming_address(row[0], time_window, normal_transcations, merged_list)
        get_maximum_number_for_same_touched_address_result = get_maximum_number_for_same_touched_address(row[0], time_window, normal_transcations, merged_list)
        get_minimum_number_for_same_incoming_address_result = get_minimum_number_for_same_incoming_address(row[0], time_window, normal_transcations, merged_list)
        get_minimum_number_for_same_outcoming_address_result = get_minimum_number_for_same_outcoming_address(row[0], time_window, normal_transcations, merged_list)
        get_minimum_number_for_same_touched_address_result = get_minimum_number_for_same_touched_address(row[0], time_window, normal_transcations, merged_list)
        how_many_address_with_a_single_transaction_for_incoming_result = how_many_address_with_a_single_transaction_for_incoming(row[0], time_window, normal_transcations, merged_list)
        how_many_address_with_a_single_transaction_for_outcoming_result = how_many_address_with_a_single_transaction_for_outcoming(row[0], time_window, normal_transcations, merged_list)
        how_many_address_with_a_single_transaction_for_all_result = how_many_address_with_a_single_transaction_for_all(row[0], time_window, normal_transcations, merged_list)
        incoming_address_with_a_single_transaction_out_of_all_unique_incoming_addresses_result = incoming_address_with_a_single_transaction_out_of_all_unique_incoming_addresses(row[0], time_window, normal_transcations, merged_list)
        incoming_address_with_a_single_transaction_out_of_all_unique_addresses_result = incoming_address_with_a_single_transaction_out_of_all_unique_addresses(row[0], time_window, normal_transcations, merged_list)
        outcoming_address_with_a_single_transaction_out_of_all_unique_outcoming_addresses_result = outcoming_address_with_a_single_transaction_out_of_all_unique_outcoming_addresses(row[0], time_window, normal_transcations, merged_list)
        outcoming_address_with_a_single_transaction_out_of_all_unique_addresses_result = outcoming_address_with_a_single_transaction_out_of_all_unique_addresses(row[0], time_window, normal_transcations, merged_list)
        all_address_with_a_single_transaction_out_of_all_unique_addresses_result = all_address_with_a_single_transaction_out_of_all_unique_addresses(row[0], time_window, normal_transcations, merged_list)
        the_maximum_repeated_Ether_value_in_incoming_amount_result = the_maximum_repeated_Ether_value_in_incoming_amount(row[0], time_window, normal_transcations, merged_list)
        the_minimum_repeated_Ether_value_in_incoming_amount_result = the_minimum_repeated_Ether_value_in_incoming_amount(row[0], time_window, normal_transcations, merged_list)
        the_maximum_repeated_Ether_value_in_outcoming_amount_result = the_maximum_repeated_Ether_value_in_outcoming_amount(row[0], time_window, normal_transcations, merged_list)
        the_minimum_repeated_Ether_value_in_outcoming_amount_result = the_minimum_repeated_Ether_value_in_outcoming_amount(row[0], time_window, normal_transcations, merged_list)
        the_maximum_repeated_Ether_value_in_all_amount_result = the_maximum_repeated_Ether_value_in_all_amount(row[0], time_window, normal_transcations, merged_list)
        the_minimum_repeated_Ether_value_in_all_amount_result = the_minimum_repeated_Ether_value_in_all_amount(row[0], time_window, normal_transcations, merged_list)
        the_maximum_repeated_Ether_value_in_incoming_times_result = the_maximum_repeated_Ether_value_in_incoming_times(row[0], time_window, normal_transcations, merged_list)
        the_minimum_repeated_Ether_value_in_incoming_times_result = the_minimum_repeated_Ether_value_in_incoming_times(row[0], time_window, normal_transcations, merged_list)
        the_maximum_repeated_Ether_value_in_outcoming_times_result = the_maximum_repeated_Ether_value_in_outcoming_times(row[0], time_window, normal_transcations, merged_list)
        the_minimum_repeated_Ether_value_in_outcoming_times_result = the_minimum_repeated_Ether_value_in_outcoming_times(row[0], time_window, normal_transcations, merged_list)
        the_maximum_repeated_Ether_value_in_all_times_result = the_maximum_repeated_Ether_value_in_all_times(row[0], time_window, normal_transcations, merged_list)
        the_minimum_repeated_Ether_value_in_all_times_result = the_minimum_repeated_Ether_value_in_all_times(row[0], time_window, normal_transcations, merged_list)

        write_list.append(str(only_incoming_result))
        write_list.append(str(only_outcoming_result))
        write_list.append(str(get_maximum_number_for_same_incoming_address_result))
        write_list.append(str(get_maximum_number_for_same_outcoming_address_result))
        write_list.append(str(get_maximum_number_for_same_touched_address_result))

        write_list.append(str(get_minimum_number_for_same_incoming_address_result))
        write_list.append(str(get_minimum_number_for_same_outcoming_address_result))
        write_list.append(str(get_minimum_number_for_same_touched_address_result))
        write_list.append(str(how_many_address_with_a_single_transaction_for_incoming_result))
        write_list.append(str(how_many_address_with_a_single_transaction_for_outcoming_result))

        write_list.append(str(how_many_address_with_a_single_transaction_for_all_result))
        write_list.append(str(incoming_address_with_a_single_transaction_out_of_all_unique_incoming_addresses_result))
        write_list.append(str(incoming_address_with_a_single_transaction_out_of_all_unique_addresses_result))
        write_list.append(str(outcoming_address_with_a_single_transaction_out_of_all_unique_outcoming_addresses_result))
        write_list.append(str(outcoming_address_with_a_single_transaction_out_of_all_unique_addresses_result))

        write_list.append(str(all_address_with_a_single_transaction_out_of_all_unique_addresses_result))
        write_list.append(str(the_maximum_repeated_Ether_value_in_incoming_amount_result))
        write_list.append(str(the_minimum_repeated_Ether_value_in_incoming_amount_result))
        write_list.append(str(the_maximum_repeated_Ether_value_in_outcoming_amount_result))
        write_list.append(str(the_minimum_repeated_Ether_value_in_outcoming_amount_result))

        write_list.append(str(the_maximum_repeated_Ether_value_in_all_amount_result))
        write_list.append(str(the_minimum_repeated_Ether_value_in_all_amount_result))
        write_list.append(str(the_maximum_repeated_Ether_value_in_incoming_times_result))
        write_list.append(str(the_minimum_repeated_Ether_value_in_incoming_times_result))
        write_list.append(str(the_maximum_repeated_Ether_value_in_outcoming_times_result))

        write_list.append(str(the_minimum_repeated_Ether_value_in_outcoming_times_result))
        write_list.append(str(the_maximum_repeated_Ether_value_in_all_times_result))
        write_list.append(str(the_minimum_repeated_Ether_value_in_all_times_result))

        get_the_total_number_of_incoming_transactions_result_all_2 = get_the_total_number_of_incoming_transactions(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_the_total_number_of_outcoming_transactions_result_all_2 = get_the_total_number_of_outcoming_transactions(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_the_number_of_unique_outcoming_addresses_result_all_2 = get_the_number_of_unique_outcoming_addresses(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_the_number_of_unique_incoming_addresses_result_all_2 = get_the_number_of_unique_incoming_addresses(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_total_value_in_Ether_ever_received_result_all_2 = get_total_value_in_Ether_ever_received(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_total_value_in_Ether_ever_sent_result_all_2 = get_total_value_in_Ether_ever_sent(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_the_number_of_incoming_transactions_per_month_result_all_2 = get_the_number_of_incoming_transactions_per_month(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_the_number_of_outcoming_transactions_per_month_result_all_2 = get_the_number_of_outcoming_transactions_per_month(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_the_number_of_incoming_amounts_per_month_result_all_2 = get_the_number_of_incoming_amounts_per_month(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_the_number_of_outcoming_amounts_per_month_result_all_2 = get_the_number_of_outcoming_amounts_per_month(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_average_time_between_incoming_transactions_result_all_2 = get_average_time_between_incoming_transactions(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_average_time_between_outcoming_transactions_result_all_2 = get_average_time_between_outcoming_transactions(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_standard_deviation_time_between_incoming_transactions_all_2 = get_standard_deviation_time_between_incoming_transactions(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_standard_deviation_time_between_outcoming_transactions_all_2 = get_standard_deviation_time_between_outcoming_transactions(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_the_total_number_of_incoming_transactions_result_all_malicious = get_the_total_number_of_incoming_transactions_malicious(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_the_total_number_of_outcoming_transactions_result_all_malicious = get_the_total_number_of_outcoming_transactions_malicious(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_the_number_of_unique_outcoming_addresses_result_all_malicious= get_the_number_of_unique_outcoming_addresses_malicious(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_the_number_of_unique_incoming_addresses_result_all_malicious = get_the_number_of_unique_incoming_addresses_malicious(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_total_value_in_Ether_ever_received_result_all_malicious = get_total_value_in_Ether_ever_received_malicious(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_total_value_in_Ether_ever_sent_result_all_malicious = get_total_value_in_Ether_ever_sent_malicious(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_fraction_of_incoming_malicious_transactions_to_all_transactions_result = get_fraction_of_incoming_malicious_transactions_to_all_transactions(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_fraction_of_outcoming_malicious_transactions_to_all_transactions_result = get_fraction_of_outcoming_malicious_transactions_to_all_transactions(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_fraction_of_incoming_malicious_addresses_to_all_address_result = get_fraction_of_incoming_malicious_addresses_to_all_address(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_fraction_of_outcoming_malicious_addresses_to_all_addresses_result = get_fraction_of_outcoming_malicious_addresses_to_all_addresses(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_fraction_of_incoming_malicious_amount_to_all_amount_result = get_fraction_of_incoming_malicious_amount_to_all_amount(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_fraction_of_outcoming_malicious_amount_to_all_amount_result = get_fraction_of_outcoming_malicious_amount_to_all_amount(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_average_time_between_incoming_transactions_result_all_malicious = get_average_time_between_incoming_transaction_malicious(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_average_time_between_outcoming_transactions_result_all_malicious = get_average_time_between_outcoming_transactions_malicious(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_standard_deviation_time_between_incoming_transactions_result_all_malicious = get_standard_deviation_time_between_incoming_transaction_malicious(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_standard_deviation_time_between_outcoming_transactions_result_all_malicious = get_standard_deviation_time_between_outcoming_transactions_malicious(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_number_of_months_account_is_active_result = get_number_of_months_account_is_active(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_number_of_transactions_associated_with_malicious_result = get_number_of_transactions_associated_with_malicious(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_number_of_transactions_associated_with_non_malicious_result = get_number_of_transactions_associated_with_non_malicious(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_number_of_self_transactions_result = get_number_of_self_transactions(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_number_of_other_transactions_result = get_number_of_other_transactions(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_normal_transactions_with_ether_value_zero_result = get_normal_transactions_with_ether_value_zero(apikey, row[0], time_window, normal_transcations, merged_list, current_time)
        get_maximum_value_in_Ether_ever_transferred_result = get_maximum_value_in_Ether_ever_transferred(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_minimum_value_in_Ether_ever_transferred_result = get_minimum_value_in_Ether_ever_transferred(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_total_value_in_Ether_result = get_total_value_in_Ether(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)
        get_number_of_addresses_related_result = get_number_of_addresses_related(apikey, row[0], time_window, {'result':merged_list}, merged_list, current_time)

        write_list.append(str(get_the_total_number_of_incoming_transactions_result_all_2)) 
        write_list.append(str(get_the_total_number_of_outcoming_transactions_result_all_2))
        write_list.append(str(get_the_number_of_unique_outcoming_addresses_result_all_2))
        write_list.append(str(get_the_number_of_unique_incoming_addresses_result_all_2)) 
        write_list.append(str(get_total_value_in_Ether_ever_received_result_all_2)) 
        write_list.append(str(get_total_value_in_Ether_ever_sent_result_all_2)) 
        write_list.append(str(get_the_number_of_incoming_transactions_per_month_result_all_2))
        write_list.append(str(get_the_number_of_outcoming_transactions_per_month_result_all_2))
        write_list.append(str(get_the_number_of_incoming_amounts_per_month_result_all_2))
        write_list.append(str(get_the_number_of_outcoming_amounts_per_month_result_all_2))
        write_list.append(str(get_average_time_between_incoming_transactions_result_all_2))
        write_list.append(str(get_average_time_between_outcoming_transactions_result_all_2))
        write_list.append(str(get_standard_deviation_time_between_incoming_transactions_all_2))
        write_list.append(str(get_standard_deviation_time_between_outcoming_transactions_all_2))
        write_list.append(str(get_the_total_number_of_incoming_transactions_result_all_malicious))
        write_list.append(str(get_the_total_number_of_outcoming_transactions_result_all_malicious))
        write_list.append(str(get_the_number_of_unique_outcoming_addresses_result_all_malicious))
        write_list.append(str(get_the_number_of_unique_incoming_addresses_result_all_malicious))
        write_list.append(str(get_total_value_in_Ether_ever_received_result_all_malicious))
        write_list.append(str(get_total_value_in_Ether_ever_sent_result_all_malicious))
        write_list.append(str(get_fraction_of_incoming_malicious_transactions_to_all_transactions_result))
        write_list.append(str(get_fraction_of_outcoming_malicious_transactions_to_all_transactions_result))
        write_list.append(str(get_fraction_of_incoming_malicious_addresses_to_all_address_result))
        write_list.append(str(get_fraction_of_outcoming_malicious_addresses_to_all_addresses_result)) 
        write_list.append(str(get_fraction_of_incoming_malicious_amount_to_all_amount_result))
        write_list.append(str(get_fraction_of_outcoming_malicious_amount_to_all_amount_result))
        write_list.append(str(get_average_time_between_incoming_transactions_result_all_malicious)) 
        write_list.append(str(get_average_time_between_outcoming_transactions_result_all_malicious))
        write_list.append(str(get_standard_deviation_time_between_incoming_transactions_result_all_malicious))
        write_list.append(str(get_standard_deviation_time_between_outcoming_transactions_result_all_malicious))
        write_list.append(str(get_number_of_months_account_is_active_result))
        write_list.append(str(get_number_of_transactions_associated_with_malicious_result))
        write_list.append(str(get_number_of_transactions_associated_with_non_malicious_result))
        write_list.append(str(get_number_of_self_transactions_result))
        write_list.append(str(get_number_of_other_transactions_result))
        write_list.append(str(get_normal_transactions_with_ether_value_zero_result))
        write_list.append(str(get_maximum_value_in_Ether_ever_transferred_result))
        write_list.append(str(get_minimum_value_in_Ether_ever_transferred_result))
        write_list.append(str(get_total_value_in_Ether_result))
        write_list.append(str(get_number_of_addresses_related_result))
    print(write_list)
    with open(output + "_result.csv", "a") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(write_list)

def get_number_of_addresses_related(apikey, address, time_window, transcations, merged_list, current_time):
    unique_list = []
    transcation_time_list_x = []
    for result in transcations['result']:
        transcation_time_list_x.append(result['timeStamp'])
    transcation_time_list_x = sorted(transcation_time_list_x)
    if transcation_time_list_x:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["from"].lower() == address.lower():
                    if result["to"] == "" and result["contractAddress"] != "":
                        if result["contractAddress"].lower() not in unique_list:
                            unique_list.append(result["contractAddress"].lower())
                    elif result["to"].lower() not in unique_list:
                        unique_list.append(result["to"].lower())
                else:
                    if result["from"].lower() not in unique_list:
                        unique_list.append(result["from"].lower())
        return len(unique_list)
    return -1

def get_total_value_in_Ether(apikey, address, time_window, transcations, merged_list, current_time):
    total_amount = 0
    count = 0
    transcation_time_list = []
    for result in transcations['result']:
        transcation_time_list.append(result['timeStamp'])
    transcation_time_list = sorted(transcation_time_list)
    if transcation_time_list:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                count = count + 1
                total_amount = total_amount + float(result['value'])
    if count != 0:
        return total_amount
    else:
        return -1

def get_minimum_value_in_Ether_ever_transferred(apikey, address, time_window, transcations, merged_list, current_time):
    first_flag = False
    min_amount = -1

    transcation_time_list = []
    for result in transcations['result']:
        transcation_time_list.append(result['timeStamp'])
    transcation_time_list = sorted(transcation_time_list)
    if transcation_time_list:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if first_flag == False:
                    min_amount = result['value']
                elif result['value'] < min_amount:
                    min_amount = result['value']
                    first_flag = True
    return min_amount

def get_maximum_value_in_Ether_ever_transferred(apikey, address, time_window, transcations, merged_list, current_time):
    first_flag = False
    max_amount = -1
    transcation_time_list = []
    for result in transcations['result']:
        transcation_time_list.append(result['timeStamp'])
    transcation_time_list = sorted(transcation_time_list)
    if transcation_time_list:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if first_flag == False:
                    max_amount = result['value']
                elif result['value'] < max_amount:
                    max_amount = result['value']
                    first_flag = True
    return max_amount

def get_normal_transactions_with_ether_value_zero(apikey, address, time_window, transcations, merged_list, current_time):
    total_amount = 0
    count = 0
    transcation_time_list = []
    for result in transcations['result']:
        transcation_time_list.append(result['timeStamp'])
    transcation_time_list = sorted(transcation_time_list)
    if transcation_time_list:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if float(result['value']) == 0:
                    count = count + 1
        return count
    return -1
    
def get_number_of_other_transactions(apikey, address, time_window, transcations, merged_list, current_time):
    addresses = []
    count = 0
    total = 0
    transcation_time_list_x = []
    for result in transcations['result']:
        transcation_time_list_x.append(result['timeStamp'])
    transcation_time_list_x = sorted(transcation_time_list_x)
    if transcation_time_list_x:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            total = total + 1
            if int(result['timeStamp']) < close_time:
                if result["to"].lower() == address.lower() or (result["to"] == "" and result["contractAddress"].lower() == address.lower()):
                    if result["from"].lower() == address.lower():
                        count = count + 1
        return total - count
    return -1

def get_number_of_transactions_associated_with_malicious(apikey, address, time_window, transcations, merged_list, current_time):
    addresses = []
    transcation_time_list_x = []
    for result in transcations['result']:
        transcation_time_list_x.append(result['timeStamp'])
    transcation_time_list_x = sorted(transcation_time_list_x)
    if transcation_time_list_x:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["to"].upper() in malicious_list or (result["to"] == "" and result["contractAddress"].upper() in malicious_list) or result["from"].upper() in malicious_list: 
                    addresses.append(result["to"].lower())
        return len(addresses)
    return -1

def get_number_of_transactions_associated_with_non_malicious(apikey, address, time_window, transcations, merged_list, current_time):
    addresses = []
    transcation_time_list_x = []
    for result in transcations['result']:
        transcation_time_list_x.append(result['timeStamp'])
    transcation_time_list_x = sorted(transcation_time_list_x)
    if transcation_time_list_x:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["to"].upper() not in malicious_list or (result["to"] == "" and result["contractAddress"].upper() not in malicious_list) or result["from"].upper() not in malicious_list: 
                    addresses.append(result["to"].lower())
        return len(addresses)
    return -1

def get_number_of_self_transactions(apikey, address, time_window, transcations, merged_list, current_time):
    addresses = []
    count = 0
    transcation_time_list_x = []
    for result in transcations['result']:
        transcation_time_list_x.append(result['timeStamp'])
    transcation_time_list_x = sorted(transcation_time_list_x)
    if transcation_time_list_x:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["to"].lower() == address.lower() or (result["to"] == "" and result["contractAddress"].lower() == address.lower()):
                    if result["from"].lower() == address.lower():
                        count = count + 1
        return count
    return -1

def get_number_of_months_account_is_active(apikey, address, time_window, transcations, merged_list, current_time):
    transcation_time_list_x = []
    for result in transcations['result']:
        transcation_time_list_x.append(result['timeStamp'])
    transcation_time_list_x = sorted(transcation_time_list_x)
    if transcation_time_list_x:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        timestamp = []
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                timestamp.append(result['timeStamp'])
        timestamp.sort()
        timezone = int(timestamp[0])
        count = 0
        while timezone < current_time:
            flag = False
            for each_time in timestamp:
                if timezone < int(each_time) and int(each_time) < timezone + 2592000:
                    flag = True
            if flag == True:
                count = count + 1
            timezone = timezone + 2592000
        return count
    return -1


def get_standard_deviation_time_between_outcoming_transactions_malicious(apikey, address, time_window, transcations, merged_list, current_time):
    transcation_time_list_x = []
    for result in transcations['result']:
        transcation_time_list_x.append(result['timeStamp'])
    transcation_time_list_x = sorted(transcation_time_list_x)
    if transcation_time_list_x:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        timestamp = []
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["from"].lower() == address.lower():
                    if result["to"].upper() in malicious_list or (result["to"] == "" and result["contractAddress"].upper() in malicious_list):
                        timestamp.append(result['timeStamp'])
        timestamp.sort()
        total_time = 0
        i = 0
        while (i+1) < len(timestamp):
            total_time = total_time + (int(timestamp[i+1]) - int(timestamp[i]))
            i = i + 1
        if len(timestamp) == 1:
            return 0
        elif i != 0:
            variance = calculate_variance(timestamp)
            return variance
    return -1

def get_standard_deviation_time_between_incoming_transaction_malicious(apikey, address, time_window, transcations, merged_list, current_time):
    transcation_time_list_x = []
    for result in transcations['result']:
        transcation_time_list_x.append(result['timeStamp'])
    transcation_time_list_x = sorted(transcation_time_list_x)
    if transcation_time_list_x:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        timestamp = []
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["to"].lower() == address.lower() or (result["to"] == "" and result["contractAddress"].lower() == address.lower()):
                    if result["from"].upper() in malicious_list:
                        timestamp.append(result['timeStamp'])
        timestamp.sort()
        total_time = 0
        i = 0
        while (i + 1) < len(timestamp):
            total_time = total_time + (int(timestamp[i + 1]) - int(timestamp[i]))
            i = i + 1
        if len(timestamp) == 1:
            return 0
        elif i != 0:
            variance = calculate_variance(timestamp)
            return variance
    return -1

def get_average_time_between_outcoming_transactions_malicious(apikey, address, time_window, transcations, merged_list, current_time):
    transcation_time_list_x = []
    for result in transcations['result']:
        transcation_time_list_x.append(result['timeStamp'])
    transcation_time_list_x = sorted(transcation_time_list_x)
    if transcation_time_list_x:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        timestamp = []
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["from"].lower() == address.lower():
                    if result["to"].upper() in malicious_list or (result["to"] == "" and result["contractAddress"].upper() in malicious_list):
                        timestamp.append(result['timeStamp'])
        timestamp.sort()
        total_time = 0
        i = 0
        while (i+1) < len(timestamp):
            total_time = total_time + (int(timestamp[i+1]) - int(timestamp[i]))
            i = i + 1
        if len(timestamp) == 1:
            return close_time - int(timestamp[0])
        elif i != 0:
            avg_time = total_time/i
            return avg_time
    return -1

def get_average_time_between_incoming_transaction_malicious(apikey, address, time_window, transcations, merged_list, current_time):
    transcation_time_list_x = []
    for result in transcations['result']:
        transcation_time_list_x.append(result['timeStamp'])
    transcation_time_list_x = sorted(transcation_time_list_x)
    if transcation_time_list_x:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        timestamp = []
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["to"].lower() == address.lower() or (result["to"] == "" and result["contractAddress"].lower() == address.lower()):
                    if result["from"].upper() in malicious_list:
                        timestamp.append(result['timeStamp'])
        timestamp.sort()
        total_time = 0
        i = 0
        while (i + 1) < len(timestamp):
            total_time = total_time + (int(timestamp[i + 1]) - int(timestamp[i]))
            i = i + 1
        if len(timestamp) == 1:
            return close_time - int(timestamp[0])
        elif i != 0:
            avg_time = total_time / i
            return avg_time
    return -1

def get_fraction_of_incoming_malicious_amount_to_all_amount(apikey, address, time_window, transcations, merged_list, current_time):
    malicious = get_total_value_in_Ether_ever_received_malicious(apikey, address, time_window, transcations, merged_list, current_time)
    all = get_the_total_number_of_amounts_outcoming_plus_incoming(apikey, address, time_window, transcations, merged_list, current_time)
    if all == 0 or all == -1:
        return -1
    elif malicious == -1:
        return 0
    else:
        result = malicious/all
        return result

def get_fraction_of_outcoming_malicious_amount_to_all_amount(apikey, address, time_window, transcations, merged_list, current_time):
    malicious = get_total_value_in_Ether_ever_sent_malicious(apikey, address, time_window, transcations, merged_list, current_time)
    all = get_the_total_number_of_amounts_outcoming_plus_incoming(apikey, address, time_window, transcations, merged_list, current_time)
    if all == 0 or all == -1:
        return -1
    elif malicious == -1:
        return 0
    else:
        result = malicious/all
        return result


def get_fraction_of_incoming_malicious_addresses_to_all_address(apikey, address, time_window, transcations, merged_list, current_time):
    malicious = get_the_number_of_unique_incoming_addresses_malicious(apikey, address, time_window, transcations, merged_list, current_time)
    unique_list = []
    transcation_time_list_x = []
    for result in transcations['result']:
        transcation_time_list_x.append(result['timeStamp'])
    transcation_time_list_x = sorted(transcation_time_list_x)
    if transcation_time_list_x:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["from"].lower() == address.lower():
                    if result["to"] == "" and result["contractAddress"] != "":
                        if result["contractAddress"].lower() not in unique_list:
                            unique_list.append(result["contractAddress"].lower())
                    elif result["to"].lower() not in unique_list:
                        unique_list.append(result["to"].lower())
                else:
                    if result["from"].lower() not in unique_list:
                        unique_list.append(result["from"].lower())
    all = len(unique_list)
    if all == 0 or all == -1:
        return -1
    elif malicious == -1:
        return 0
    else:
        result = malicious/all
        return result

def get_fraction_of_outcoming_malicious_addresses_to_all_addresses(apikey, address, time_window, transcations, merged_list, current_time):
    malicious = get_the_number_of_unique_outcoming_addresses_malicious(apikey, address, time_window, transcations, merged_list, current_time)
    unique_list = []
    transcation_time_list_x = []
    for result in transcations['result']:
        transcation_time_list_x.append(result['timeStamp'])
    transcation_time_list_x = sorted(transcation_time_list_x)
    if transcation_time_list_x:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["from"].lower() == address.lower():
                    if result["to"] == "" and result["contractAddress"] != "":
                        if result["contractAddress"].lower() not in unique_list:
                            unique_list.append(result["contractAddress"].lower())
                    elif result["to"].lower() not in unique_list:
                        unique_list.append(result["to"].lower())
                else:
                    if result["from"].lower() not in unique_list:
                        unique_list.append(result["from"].lower())
    all = len(unique_list)
    if all == 0 or all == -1:
        return -1
    elif malicious == -1:
        return 0
    else:
        result = malicious/all
        return result


def get_fraction_of_incoming_malicious_transactions_to_all_transactions(apikey, address, time_window, transcations, merged_list, current_time):
    malicious = get_the_total_number_of_incoming_transactions_malicious(apikey, address, time_window, transcations, merged_list, current_time)
    transcation_time_list_x = []
    all = -1
    for result in transcations['result']:
        transcation_time_list_x.append(result['timeStamp'])
    transcation_time_list_x = sorted(transcation_time_list_x)
    if transcation_time_list_x:
        all = 0
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                all = all + 1
    if all == 0 or all == -1:
        return -1
    elif malicious == -1:
        return 0
    else:
        result = malicious/all
        return result

def get_fraction_of_outcoming_malicious_transactions_to_all_transactions(apikey, address, time_window, transcations, merged_list, current_time):
    malicious = get_the_total_number_of_outcoming_transactions_malicious(apikey, address, time_window, transcations, merged_list, current_time)
    transcation_time_list_x = [] 
    all = -1
    for result in transcations['result']:
        transcation_time_list_x.append(result['timeStamp'])
    transcation_time_list_x = sorted(transcation_time_list_x)
    if transcation_time_list_x:
        all = 0
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                all = all + 1
    if all == 0 or all == -1:
        return -1
    elif malicious == -1:
        return 0
    else:
        result = malicious/all
        return result

def get_total_value_in_Ether_ever_received_malicious(apikey, address, time_window, transcations, merged_list, current_time):
    total_amount = 0
    count = 0
    transcation_time_list = []
    for result in transcations['result']:
        transcation_time_list.append(result['timeStamp'])
    transcation_time_list = sorted(transcation_time_list)
    if transcation_time_list:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["to"].lower() == address.lower() or (result["to"] == "" and result["contractAddress"].lower() == address.lower()):
                    if result["from"].upper() in malicious_list:
                        count = count + 1
                        total_amount = total_amount + float(result['value'])
    if count != 0:
        return total_amount
    else:
        return -1

def get_total_value_in_Ether_ever_sent_malicious(apikey, address, time_window, transcations, merged_list, current_time):
    total_amount = 0
    count = 0
    transcation_time_list = []
    for result in transcations['result']:
        transcation_time_list.append(result['timeStamp'])
    transcation_time_list = sorted(transcation_time_list)
    if transcation_time_list:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["from"].lower() == address.lower():
                    if result["to"].upper() in malicious_list or (result["to"] == "" and result["contractAddress"].upper() in malicious_list):
                        count = count + 1
                        total_amount = total_amount + float(result['value'])
    if count != 0:
        return total_amount
    else:
        return -1
    
def get_the_number_of_unique_incoming_addresses_malicious(apikey, address, time_window, transcations, merged_list, current_time):
    unique_list = []
    transcation_time_list_x = []
    for result in transcations['result']:
        transcation_time_list_x.append(result['timeStamp'])
    transcation_time_list_x = sorted(transcation_time_list_x)
    if transcation_time_list_x:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["to"].lower() == address.lower() or (result["to"] == "" and result["contractAddress"].lower() == address.lower()):
                    if result["from"].lower() not in unique_list:
                        if result["from"].upper() in malicious_list:
                            unique_list.append(result["from"].lower())
        return len(unique_list)
    return -1

def get_the_number_of_unique_outcoming_addresses_malicious(apikey, address, time_window, transcations, merged_list, current_time):
    unique_list = []
    transcation_time_list_x = []
    for result in transcations['result']:
        transcation_time_list_x.append(result['timeStamp'])
    transcation_time_list_x = sorted(transcation_time_list_x)
    if transcation_time_list_x:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["from"].lower() == address.lower():
                    if result["to"] == "" and result["contractAddress"] != "":
                        if result["contractAddress"].lower() not in unique_list:
                            if result["contractAddress"].upper() in malicious_list:
                                unique_list.append(result["contractAddress"].lower())
                    elif result["to"].lower() not in unique_list:
                        if result["to"].upper() in malicious_list:
                            unique_list.append(result["to"].lower())
        return len(unique_list)
    return -1

def get_the_total_number_of_outcoming_transactions_malicious(apikey, address, time_window, transcations, merged_list, current_time):
    addresses = []
    transcation_time_list_x = []
    for result in transcations['result']:
        transcation_time_list_x.append(result['timeStamp'])
    transcation_time_list_x = sorted(transcation_time_list_x)
    if transcation_time_list_x:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["from"].lower() == address.lower():
                    if result["to"].upper() in malicious_list or (result["to"] == "" and result["contractAddress"].upper() in malicious_list):
                        addresses.append(result["to"].lower())
        return len(addresses)
    return -1


def get_the_total_number_of_incoming_transactions_malicious(apikey, address, time_window, transcations, merged_list, current_time):
    addresses = []
    transcation_time_list_x = []
    for result in transcations['result']:
        transcation_time_list_x.append(result['timeStamp'])
    transcation_time_list_x = sorted(transcation_time_list_x)
    if transcation_time_list_x:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["to"].lower() == address.lower() or (result["to"] == "" and result["contractAddress"].lower() == address.lower()):
                    if result["from"].upper() in malicious_list:
                        addresses.append(result["to"].lower())
        return len(addresses)
    return -1

def calculate_variance(data):
    n = len(data)
    int_data = []
    for every_data in data:
        int_data.append(int(every_data))
    mean = sum(int_data) / n
    squared_diff = [(x - mean) ** 2 for x in int_data]
    variance = sum(squared_diff) / (n - 1)

    return variance


def get_standard_deviation_time_between_incoming_transactions(apikey, address, time_window, transcations, merged_list, current_time):
    transcation_time_list_x = []
    for result in transcations['result']:
        transcation_time_list_x.append(result['timeStamp'])
    transcation_time_list_x = sorted(transcation_time_list_x)
    if transcation_time_list_x:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        timestamp = []
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["to"].lower() == address.lower() or (result["to"] == "" and result["contractAddress"].lower() == address.lower()):
                    timestamp.append(result['timeStamp'])
        timestamp.sort()
        total_time = 0
        i = 0
        while (i + 1) < len(timestamp):
            total_time = total_time + (int(timestamp[i + 1]) - int(timestamp[i]))
            i = i + 1
        if len(timestamp) == 1:
            return 0
        elif i != 0:
            return calculate_variance(timestamp)
    return -1

def get_standard_deviation_time_between_outcoming_transactions(apikey, address, time_window, transcations, merged_list, current_time):
    transcation_time_list_x = []
    for result in transcations['result']:
        transcation_time_list_x.append(result['timeStamp'])
    transcation_time_list_x = sorted(transcation_time_list_x)
    if transcation_time_list_x:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        timestamp = []
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["from"].lower() == address.lower():
                    timestamp.append(result['timeStamp'])
        timestamp.sort()
        total_time = 0
        i = 0
        while (i+1) < len(timestamp):
            total_time = total_time + (int(timestamp[i+1]) - int(timestamp[i]))
            i = i + 1
        if len(timestamp) == 1:
            return 0
        elif i != 0:
            return calculate_variance(timestamp)
    return -1

def only_incoming(address, time_window, transcations, merged_list):
    incoming_count = 0
    outcoming_count = 0
    transcation_time_list = []
    for result in transcations['result']:
        transcation_time_list.append(result['timeStamp'])
    transcation_time_list = sorted(transcation_time_list)
    if transcation_time_list:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["from"].lower() == address.lower():
                    outcoming_count = outcoming_count + 1
                elif result["to"].lower() == address.lower() or (result["to"] == "" and result["contractAddress"].lower() == address.lower()):
                    incoming_count = incoming_count + 1

    if incoming_count != 0 and outcoming_count == 0:
        return 1
    elif incoming_count == 0 and outcoming_count != 0:
        return 0
    else:
        return -1

def only_outcoming(address, time_window, transcations, merged_list):
    incoming_count = 0
    outcoming_count = 0
    transcation_time_list = []
    for result in transcations['result']:
        transcation_time_list.append(result['timeStamp'])
    transcation_time_list = sorted(transcation_time_list)
    if transcation_time_list:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["from"].lower() == address.lower():
                    outcoming_count = outcoming_count + 1
                elif result["to"].lower() == address.lower() or (result["to"] == "" and result["contractAddress"].lower() == address.lower()):
                    incoming_count = incoming_count + 1

    if incoming_count != 0 and outcoming_count == 0:
        return 0
    elif incoming_count == 0 and outcoming_count != 0:
        return 1
    else:
        return -1
    
def get_maximum_number_for_same_incoming_address(address, time_window, transcations, merged_list):
    address_and_number = {}
    sorted_numbers = []
    transcation_time_list = []
    for result in transcations['result']:
        transcation_time_list.append(result['timeStamp'])
    transcation_time_list = sorted(transcation_time_list)
    if transcation_time_list:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["to"].lower() == address.lower() or (result["to"] == "" and result["contractAddress"].lower() == address.lower()):
                    if address.lower() not in address_and_number:
                        address_and_number[address.lower()] = 1
                    else:
                        address_and_number[address.lower()] = address_and_number[address.lower()] + 1
    if address_and_number:
        sorted_numbers = sorted(address_and_number.items(), key=lambda x: x[1], reverse=True)
        return sorted_numbers[0][1]
    else:
        return -1

def get_maximum_number_for_same_outcoming_address(address, time_window, transcations, merged_list):
    address_and_number = {}
    sorted_numbers = []
    transcation_time_list = []
    for result in transcations['result']:
        transcation_time_list.append(result['timeStamp'])
    transcation_time_list = sorted(transcation_time_list)
    if transcation_time_list:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["from"].lower() == address.lower():
                    if address.lower() not in address_and_number:
                        address_and_number[address.lower()] = 1
                    else:
                        address_and_number[address.lower()] = address_and_number[address.lower()] + 1
    if address_and_number:
        sorted_numbers = sorted(address_and_number.items(), key=lambda x: x[1], reverse=True)
        return sorted_numbers[0][1]
    else:
        return -1

def get_maximum_number_for_same_touched_address(address, time_window, transcations, merged_list):
    address_and_number = {}
    sorted_numbers = []
    transcation_time_list = []
    for result in transcations['result']:
        transcation_time_list.append(result['timeStamp'])
    transcation_time_list = sorted(transcation_time_list)
    if transcation_time_list:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["from"].lower() == address.lower() or result["to"].lower() == address.lower() or (result["to"] == "" and result["contractAddress"].lower() == address.lower()):
                    if address.lower() not in address_and_number:
                        address_and_number[address.lower()] = 1
                    else:
                        address_and_number[address.lower()] = address_and_number[address.lower()] + 1
    if address_and_number:
        sorted_numbers = sorted(address_and_number.items(), key=lambda x: x[1], reverse=True)
        return sorted_numbers[0][1]
    else:
        return -1

def get_minimum_number_for_same_incoming_address(address, time_window, transcations, merged_list):
    address_and_number = {}
    sorted_numbers = []
    transcation_time_list = []
    for result in transcations['result']:
        transcation_time_list.append(result['timeStamp'])
    transcation_time_list = sorted(transcation_time_list)
    if transcation_time_list:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["to"].lower() == address.lower() or (result["to"] == "" and result["contractAddress"].lower() == address.lower()):
                    if address.lower() not in address_and_number:
                        address_and_number[address.lower()] = 1
                    else:
                        address_and_number[address.lower()] = address_and_number[address.lower()] + 1
    if address_and_number:
        sorted_numbers = sorted(address_and_number.items(), key=lambda x: x[1], reverse=True)
        return sorted_numbers[-1][1]
    else:
        return -1

def get_minimum_number_for_same_outcoming_address(address, time_window, transcations, merged_list):
    address_and_number = {}
    sorted_numbers = []
    transcation_time_list = []
    for result in transcations['result']:
        transcation_time_list.append(result['timeStamp'])
    transcation_time_list = sorted(transcation_time_list)
    if transcation_time_list:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["from"].lower() == address.lower():
                    if address.lower() not in address_and_number:
                        address_and_number[address.lower()] = 1
                    else:
                        address_and_number[address.lower()] = address_and_number[address.lower()] + 1
    if address_and_number:
        sorted_numbers = sorted(address_and_number.items(), key=lambda x: x[1], reverse=True)
        return sorted_numbers[-1][1]
    else:
        return -1

def get_minimum_number_for_same_touched_address(address, time_window, transcations, merged_list):
    address_and_number = {}
    sorted_numbers = []
    transcation_time_list = []
    for result in transcations['result']:
        transcation_time_list.append(result['timeStamp'])
    transcation_time_list = sorted(transcation_time_list)
    if transcation_time_list:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["from"].lower() == address.lower() or result["to"].lower() == address.lower() or (result["to"] == "" and result["contractAddress"].lower() == address.lower()):
                    if address.lower() not in address_and_number:
                        address_and_number[address.lower()] = 1
                    else:
                        address_and_number[address.lower()] = address_and_number[address.lower()] + 1
    if address_and_number:
        sorted_numbers = sorted(address_and_number.items(), key=lambda x: x[1], reverse=True)
        return sorted_numbers[-1][1]
    else:
        return -1

def how_many_address_with_a_single_transaction_for_incoming(address, time_window, transcations, merged_list):
    address_and_number = {}
    no_more_than_one_number = 0
    transcation_time_list = []
    for result in transcations['result']:
        transcation_time_list.append(result['timeStamp'])
    transcation_time_list = sorted(transcation_time_list)
    if transcation_time_list:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["to"].lower() == address.lower() or (result["to"] == "" and result["contractAddress"].lower() == address.lower()):
                    if address.lower() not in address_and_number:
                        address_and_number[address.lower()] = 1
                    else:
                        address_and_number[address.lower()] = address_and_number[address.lower()] + 1
    if address_and_number:
        for key,value in address_and_number.items():
            if value == 1:
                no_more_than_one_number = no_more_than_one_number + 1
        return no_more_than_one_number
    else:
        return -1

def how_many_address_with_a_single_transaction_for_outcoming(address, time_window, transcations, merged_list):
    address_and_number = {}
    no_more_than_one_number = 0
    transcation_time_list = []
    for result in transcations['result']:
        transcation_time_list.append(result['timeStamp'])
    transcation_time_list = sorted(transcation_time_list)
    if transcation_time_list:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["from"].lower() == address.lower():
                    if address.lower() not in address_and_number:
                        address_and_number[address.lower()] = 1
                    else:
                        address_and_number[address.lower()] = address_and_number[address.lower()] + 1
    if address_and_number:
        for key,value in address_and_number.items():
            if value == 1:
                no_more_than_one_number = no_more_than_one_number + 1
        return no_more_than_one_number
    else:
        return -1

def how_many_address_with_a_single_transaction_for_all(address, time_window, transcations, merged_list):
    address_and_number = {}
    no_more_than_one_number = 0
    transcation_time_list = []
    for result in transcations['result']:
        transcation_time_list.append(result['timeStamp'])
    transcation_time_list = sorted(transcation_time_list)
    if transcation_time_list:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["from"].lower() == address.lower() or result["to"].lower() == address.lower() or (result["to"] == "" and result["contractAddress"].lower() == address.lower()):
                    if address.lower() not in address_and_number:
                        address_and_number[address.lower()] = 1
                    else:
                        address_and_number[address.lower()] = address_and_number[address.lower()] + 1
    if address_and_number:
        for key,value in address_and_number.items():
            if value == 1:
                no_more_than_one_number = no_more_than_one_number + 1
        return no_more_than_one_number
    else:
        return -1

def incoming_address_with_a_single_transaction_out_of_all_unique_incoming_addresses(address, time_window, transcations, merged_list):
    address_and_number = {}
    no_more_than_one_number = 0
    all_incoming_address_number = 0
    transcation_time_list = []
    for result in transcations['result']:
        transcation_time_list.append(result['timeStamp'])
    transcation_time_list = sorted(transcation_time_list)
    if transcation_time_list:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["to"].lower() == address.lower() or (result["to"] == "" and result["contractAddress"].lower() == address.lower()):
                    if address.lower() not in address_and_number:
                        address_and_number[address.lower()] = 1
                    else:
                        address_and_number[address.lower()] = address_and_number[address.lower()] + 1
    if address_and_number:
        for key,value in address_and_number.items():
            if value == 1:
                no_more_than_one_number = no_more_than_one_number + 1
            all_incoming_address_number = all_incoming_address_number + 1
        return no_more_than_one_number/all_incoming_address_number
    else:
        return -1

def incoming_address_with_a_single_transaction_out_of_all_unique_addresses(address, time_window, transcations, merged_list):
    address_and_number = {}
    no_more_than_one_number = 0
    all_incoming_address_number = 0
    all_addresses = []
    transcation_time_list = []
    for result in transcations['result']:
        transcation_time_list.append(result['timeStamp'])
    transcation_time_list = sorted(transcation_time_list)
    if transcation_time_list:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["to"].lower() == address.lower() or (result["to"] == "" and result["contractAddress"].lower() == address.lower()):
                    if address.lower() not in address_and_number:
                        address_and_number[address.lower()] = 1
                    else:
                        address_and_number[address.lower()] = address_and_number[address.lower()] + 1
                if result["from"].lower() == address.lower() or result["to"].lower() == address.lower() or (result["to"] == "" and result["contractAddress"].lower() == address.lower()):
                    if address.lower() not in all_addresses:
                        all_addresses.append(address.lower())
    if address_and_number:
        for key,value in address_and_number.items():
            if value == 1:
                no_more_than_one_number = no_more_than_one_number + 1
            all_incoming_address_number = all_incoming_address_number + 1
        return no_more_than_one_number/len(all_addresses)
    else:
        return -1

def outcoming_address_with_a_single_transaction_out_of_all_unique_outcoming_addresses(address, time_window, transcations, merged_list):
    address_and_number = {}
    no_more_than_one_number = 0
    all_incoming_address_number = 0
    transcation_time_list = []
    for result in transcations['result']:
        transcation_time_list.append(result['timeStamp'])
    transcation_time_list = sorted(transcation_time_list)
    if transcation_time_list:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["from"].lower() == address.lower():
                    if address.lower() not in address_and_number:
                        address_and_number[address.lower()] = 1
                    else:
                        address_and_number[address.lower()] = address_and_number[address.lower()] + 1
    if address_and_number:
        for key,value in address_and_number.items():
            if value == 1:
                no_more_than_one_number = no_more_than_one_number + 1
            all_incoming_address_number = all_incoming_address_number + 1
        return no_more_than_one_number/all_incoming_address_number
    else:
        return -1

def outcoming_address_with_a_single_transaction_out_of_all_unique_addresses(address, time_window, transcations, merged_list):
    address_and_number = {}
    no_more_than_one_number = 0
    all_incoming_address_number = 0
    all_addresses = []
    transcation_time_list = []
    for result in transcations['result']:
        transcation_time_list.append(result['timeStamp'])
    transcation_time_list = sorted(transcation_time_list)
    if transcation_time_list:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["from"].lower() == address.lower():
                    if address.lower() not in address_and_number:
                        address_and_number[address.lower()] = 1
                    else:
                        address_and_number[address.lower()] = address_and_number[address.lower()] + 1
                if result["from"].lower() == address.lower() or result["to"].lower() == address.lower() or (result["to"] == "" and result["contractAddress"].lower() == address.lower()):
                    if address.lower() not in all_addresses:
                        all_addresses.append(address.lower())
    if address_and_number:
        for key,value in address_and_number.items():
            if value == 1:
                no_more_than_one_number = no_more_than_one_number + 1
            all_incoming_address_number = all_incoming_address_number + 1
        return no_more_than_one_number/len(all_addresses)
    else:
        return -1

def all_address_with_a_single_transaction_out_of_all_unique_addresses(address, time_window, transcations, merged_list):
    address_and_number = {}
    no_more_than_one_number = 0
    all_incoming_address_number = 0
    all_addresses = []
    transcation_time_list = []
    for result in transcations['result']:
        transcation_time_list.append(result['timeStamp'])
    transcation_time_list = sorted(transcation_time_list)
    if transcation_time_list:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["from"].lower() == address.lower() or result["to"].lower() == address.lower() or (result["to"] == "" and result["contractAddress"].lower() == address.lower()):
                    if address.lower() not in all_addresses:
                        all_addresses.append(address.lower())
                    if address.lower() not in address_and_number:
                        address_and_number[address.lower()] = 1
                    else:
                        address_and_number[address.lower()] = address_and_number[address.lower()] + 1
    if address_and_number:
        for key,value in address_and_number.items():
            if value == 1:
                no_more_than_one_number = no_more_than_one_number + 1
            all_incoming_address_number = all_incoming_address_number + 1
        return no_more_than_one_number/len(all_addresses)
    else:
        return -1
    
def the_maximum_repeated_Ether_value_in_incoming_amount(address, time_window, transcations, merged_list):
    value_and_number = {}
    sorted_numbers = []
    transcation_time_list = []
    for result in transcations['result']:
        transcation_time_list.append(result['timeStamp'])
    transcation_time_list = sorted(transcation_time_list)
    if transcation_time_list:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["to"].lower() == address.lower() or (result["to"] == "" and result["contractAddress"].lower() == address.lower()):
                    if result['value'] not in value_and_number:
                        value_and_number[result['value']] = 1
                    else:
                        value_and_number[result['value']] = value_and_number[result['value']] + 1
    if value_and_number:
        sorted_numbers = sorted(value_and_number.items(), key=lambda x: x[1], reverse=True)
        print(sorted_numbers)
        for (key,value) in sorted_numbers:
            if value >= 2:
                return key
    return -1

def the_minimum_repeated_Ether_value_in_incoming_amount(address, time_window, transcations, merged_list):
    value_and_number = {}
    sorted_numbers = []
    transcation_time_list = []
    for result in transcations['result']:
        transcation_time_list.append(result['timeStamp'])
    transcation_time_list = sorted(transcation_time_list)
    if transcation_time_list:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["to"].lower() == address.lower() or (result["to"] == "" and result["contractAddress"].lower() == address.lower()):
                    if result['value'] not in value_and_number:
                        value_and_number[result['value']] = 1
                    else:
                        value_and_number[result['value']] = value_and_number[result['value']] + 1
    if value_and_number:
        sorted_numbers = sorted(value_and_number.items(), key=lambda x: x[1], reverse=False)
        for (key,value) in sorted_numbers:
            if value >= 2:
                return key
    return -1

def the_maximum_repeated_Ether_value_in_outcoming_amount(address, time_window, transcations, merged_list):
    value_and_number = {}
    sorted_numbers = []
    transcation_time_list = []
    for result in transcations['result']:
        transcation_time_list.append(result['timeStamp'])
    transcation_time_list = sorted(transcation_time_list)
    if transcation_time_list:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["from"].lower() == address.lower():
                    if result['value'] not in value_and_number:
                        value_and_number[result['value']] = 1
                    else:
                        value_and_number[result['value']] = value_and_number[result['value']] + 1
    if value_and_number:
        sorted_numbers = sorted(value_and_number.items(), key=lambda x: x[1], reverse=True)
        for (key,value) in sorted_numbers:
            if value >= 2:
                return key
    return -1

def the_minimum_repeated_Ether_value_in_outcoming_amount(address, time_window, transcations, merged_list):
    value_and_number = {}
    sorted_numbers = []
    transcation_time_list = []
    for result in transcations['result']:
        transcation_time_list.append(result['timeStamp'])
    transcation_time_list = sorted(transcation_time_list)
    if transcation_time_list:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["from"].lower() == address.lower():
                    if result['value'] not in value_and_number:
                        value_and_number[result['value']] = 1
                    else:
                        value_and_number[result['value']] = value_and_number[result['value']] + 1
    if value_and_number:
        sorted_numbers = sorted(value_and_number.items(), key=lambda x: x[1], reverse=False)
        for (key,value) in sorted_numbers:
            if value >= 2:
                return key
    return -1

def the_maximum_repeated_Ether_value_in_all_amount(address, time_window, transcations, merged_list):
    value_and_number = {}
    sorted_numbers = []
    transcation_time_list = []
    for result in transcations['result']:
        transcation_time_list.append(result['timeStamp'])
    transcation_time_list = sorted(transcation_time_list)
    if transcation_time_list:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["from"].lower() == address.lower() or result["to"].lower() == address.lower() or (result["to"] == "" and result["contractAddress"].lower() == address.lower()):
                    if result['value'] not in value_and_number:
                        value_and_number[result['value']] = 1
                    else:
                        value_and_number[result['value']] = value_and_number[result['value']] + 1
    if value_and_number:
        sorted_numbers = sorted(value_and_number.items(), key=lambda x: x[1], reverse=True)
        for (key,value) in sorted_numbers:
            if value >= 2:
                return key
    return -1

def the_minimum_repeated_Ether_value_in_all_amount(address, time_window, transcations, merged_list):
    value_and_number = {}
    sorted_numbers = []
    transcation_time_list = []
    for result in transcations['result']:
        transcation_time_list.append(result['timeStamp'])
    transcation_time_list = sorted(transcation_time_list)
    if transcation_time_list:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["from"].lower() == address.lower() or result["to"].lower() == address.lower() or (result["to"] == "" and result["contractAddress"].lower() == address.lower()):
                    if result['value'] not in value_and_number:
                        value_and_number[result['value']] = 1
                    else:
                        value_and_number[result['value']] = value_and_number[result['value']] + 1
    if value_and_number:
        sorted_numbers = sorted(value_and_number.items(), key=lambda x: x[1], reverse=False)
        for (key,value) in sorted_numbers:
            if value >= 2:
                return key
    return -1

def the_maximum_repeated_Ether_value_in_incoming_times(address, time_window, transcations, merged_list):
    value_and_number = {}
    sorted_numbers = []
    transcation_time_list = []
    for result in transcations['result']:
        transcation_time_list.append(result['timeStamp'])
    transcation_time_list = sorted(transcation_time_list)
    if transcation_time_list:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["to"].lower() == address.lower() or (result["to"] == "" and result["contractAddress"].lower() == address.lower()):
                    if result['value'] not in value_and_number:
                        value_and_number[result['value']] = 1
                    else:
                        value_and_number[result['value']] = value_and_number[result['value']] + 1
    if value_and_number:
        sorted_numbers = sorted(value_and_number.items(), key=lambda x: x[1], reverse=True)
        for (key,value) in sorted_numbers:
            if value >= 2:
                return value
    return -1

def the_minimum_repeated_Ether_value_in_incoming_times(address, time_window, transcations, merged_list):
    value_and_number = {}
    sorted_numbers = []
    transcation_time_list = []
    for result in transcations['result']:
        transcation_time_list.append(result['timeStamp'])
    transcation_time_list = sorted(transcation_time_list)
    if transcation_time_list:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["to"].lower() == address.lower() or (result["to"] == "" and result["contractAddress"].lower() == address.lower()):
                    if result['value'] not in value_and_number:
                        value_and_number[result['value']] = 1
                    else:
                        value_and_number[result['value']] = value_and_number[result['value']] + 1
    if value_and_number:
        sorted_numbers = sorted(value_and_number.items(), key=lambda x: x[1], reverse=False)
        for (key,value) in sorted_numbers:
            if value >= 2:
                return value
    return -1

def the_maximum_repeated_Ether_value_in_outcoming_times(address, time_window, transcations, merged_list):
    value_and_number = {}
    sorted_numbers = []
    transcation_time_list = []
    for result in transcations['result']:
        transcation_time_list.append(result['timeStamp'])
    transcation_time_list = sorted(transcation_time_list)
    if transcation_time_list:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["from"].lower() == address.lower():
                    if result['value'] not in value_and_number:
                        value_and_number[result['value']] = 1
                    else:
                        value_and_number[result['value']] = value_and_number[result['value']] + 1
    if value_and_number:
        sorted_numbers = sorted(value_and_number.items(), key=lambda x: x[1], reverse=True)
        for (key,value) in sorted_numbers:
            if value >= 2:
                return value
    return -1

def the_minimum_repeated_Ether_value_in_outcoming_times(address, time_window, transcations, merged_list):
    value_and_number = {}
    sorted_numbers = []
    transcation_time_list = []
    for result in transcations['result']:
        transcation_time_list.append(result['timeStamp'])
    transcation_time_list = sorted(transcation_time_list)
    if transcation_time_list:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["from"].lower() == address.lower():
                    if result['value'] not in value_and_number:
                        value_and_number[result['value']] = 1
                    else:
                        value_and_number[result['value']] = value_and_number[result['value']] + 1
    if value_and_number:
        sorted_numbers = sorted(value_and_number.items(), key=lambda x: x[1], reverse=False)
        for (key,value) in sorted_numbers:
            if value >= 2:
                return value
    return -1

def the_maximum_repeated_Ether_value_in_all_times(address, time_window, transcations, merged_list):
    value_and_number = {}
    sorted_numbers = []
    transcation_time_list = []
    for result in transcations['result']:
        transcation_time_list.append(result['timeStamp'])
    transcation_time_list = sorted(transcation_time_list)
    if transcation_time_list:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["from"].lower() == address.lower() or result["to"].lower() == address.lower() or (result["to"] == "" and result["contractAddress"].lower() == address.lower()):
                    if result['value'] not in value_and_number:
                        value_and_number[result['value']] = 1
                    else:
                        value_and_number[result['value']] = value_and_number[result['value']] + 1
    if value_and_number:
        sorted_numbers = sorted(value_and_number.items(), key=lambda x: x[1], reverse=True)
        for (key,value) in sorted_numbers:
            if value >= 2:
                return value
    return -1

def the_minimum_repeated_Ether_value_in_all_times(address, time_window, transcations, merged_list):
    value_and_number = {}
    sorted_numbers = []
    transcation_time_list = []
    for result in transcations['result']:
        transcation_time_list.append(result['timeStamp'])
    transcation_time_list = sorted(transcation_time_list)
    if transcation_time_list:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["from"].lower() == address.lower() or result["to"].lower() == address.lower() or (result["to"] == "" and result["contractAddress"].lower() == address.lower()):
                    if result['value'] not in value_and_number:
                        value_and_number[result['value']] = 1
                    else:
                        value_and_number[result['value']] = value_and_number[result['value']] + 1
    if value_and_number:
        sorted_numbers = sorted(value_and_number.items(), key=lambda x: x[1], reverse=False)
        for (key,value) in sorted_numbers:
            if value >= 2:
                return value
    return -1
    
def get_the_propotion_of_single_ether_transfered_of_all(apikey, address, time_window, transcations, merged_list, current_time):
    normal_number = get_the_total_number_of_amounts_outcoming_plus_incoming(apikey, address, time_window, transcations, merged_list, current_time)
    total_number = get_the_total_number_of_amounts_outcoming_plus_incoming(apikey, address, time_window, {'result':merged_list}, merged_list, current_time)
    result = -1
    if normal_number == -1 or total_number == -1:
        return result
    if total_number != 0:
        result = normal_number / total_number
    return result

def get_the_propotion_of_single_ether_sent_of_all_sent(apikey, address, time_window, transcations, merged_list, current_time):
    normal_number = get_total_value_in_Ether_ever_sent(apikey, address, time_window, transcations, merged_list, current_time)
    total_number = get_total_value_in_Ether_ever_sent(apikey, address, time_window, {'result':merged_list}, merged_list, current_time)
    result = -1
    if normal_number == -1 or total_number == -1:
        return result
    if total_number != 0:
        result = normal_number / total_number
    return result

def get_the_propotion_of_single_ether_sent_of_all_touched(apikey, address, time_window, transcations, merged_list, current_time):
    normal_number = get_total_value_in_Ether_ever_sent(apikey, address, time_window, transcations, merged_list, current_time)
    total_number = get_the_total_number_of_amounts_outcoming_plus_incoming(apikey, address, time_window, {'result':merged_list}, merged_list, current_time)
    result = -1
    if normal_number == -1 or total_number == -1:
        return result
    if total_number != 0:
        result = normal_number / total_number
    return result

def get_the_propotion_of_single_ether_received_of_all_received(apikey, address, time_window, transcations, merged_list, current_time):
    normal_number = get_total_value_in_Ether_ever_received(apikey, address, time_window, transcations, merged_list, current_time)
    total_number = get_total_value_in_Ether_ever_received(apikey, address, time_window, {'result':merged_list}, merged_list, current_time)
    result = -1
    if normal_number == -1 or total_number == -1:
        return result
    if total_number != 0:
        result = normal_number / total_number
    return result

def get_the_propotion_of_single_ether_received_of_all_touched(apikey, address, time_window, transcations, merged_list, current_time):
    normal_number = get_total_value_in_Ether_ever_received(apikey, address, time_window, transcations, merged_list, current_time)
    total_number = get_the_total_number_of_amounts_outcoming_plus_incoming(apikey, address, time_window, {'result':merged_list}, merged_list, current_time)
    result = -1
    if normal_number == -1 or total_number == -1:
        return result
    if total_number != 0:
        result = normal_number / total_number
    return result


def get_the_propotion_of_single_transactions_of_all(apikey, address, time_window, transcations, merged_list, current_time):
    normal_number = get_total_number_of_transactions(apikey, address, time_window, transcations, merged_list, current_time)
    total_number = get_total_number_of_transactions(apikey, address, time_window, {'result':merged_list}, merged_list, current_time)
    result = -1
    if normal_number == -1 or total_number == -1:
        return result
    if total_number != 0:
        result = normal_number/total_number
    return result

def get_the_propotion_of_single_incoming_transactions_of_all_incoming(apikey, address, time_window, transcations, merged_list, current_time):
    normal_number = get_the_total_number_of_incoming_transactions(apikey, address, time_window, transcations, merged_list, current_time)
    total_number = get_the_total_number_of_incoming_transactions(apikey, address, time_window, {'result':merged_list}, merged_list, current_time)
    result = -1
    if normal_number == -1 or total_number == -1:
        return result
    if total_number != 0:
        result = normal_number/total_number
    return result

def get_the_propotion_of_single_incoming_transactions_of_all_transactions(apikey, address, time_window, transcations, merged_list, current_time):
    normal_number = get_the_total_number_of_incoming_transactions(apikey, address, time_window, transcations, merged_list, current_time)
    total_number = get_total_number_of_transactions(apikey, address, time_window, {'result':merged_list}, merged_list, current_time)
    result = -1
    if normal_number == -1 or total_number == -1:
        return result
    if total_number != 0:
        result = normal_number/total_number
    return result

def get_the_propotion_of_single_outcoming_transactions_of_all_outcoming(apikey, address, time_window, transcations, merged_list, current_time):
    normal_number = get_the_total_number_of_outcoming_transactions(apikey, address, time_window, transcations, merged_list, current_time)
    total_number = get_the_total_number_of_outcoming_transactions(apikey, address, time_window, {'result':merged_list}, merged_list, current_time)
    result = -1
    if normal_number == -1 or total_number == -1:
        return result
    if total_number != 0:
        result = normal_number/total_number
    return result

def get_the_propotion_of_single_outcoming_transactions_of_all_transactions(apikey, address, time_window, transcations, merged_list, current_time):
    normal_number = get_the_total_number_of_outcoming_transactions(apikey, address, time_window, transcations, merged_list, current_time)
    total_number = get_total_number_of_transactions(apikey, address, time_window, {'result':merged_list}, merged_list, current_time)
    result = -1
    if normal_number == -1 or total_number == -1:
        return result
    if total_number != 0:
        result = normal_number/total_number
    return result

def merge_without_erc(normal_transaction, internal_transaction):
    merged_list = []
    for result in normal_transaction['result']:
        i = 0
        find_flag = False
        for merged_transaction in merged_list:
            if merged_transaction['hash'] == result['hash']:
                merged_list[i]['value'] = merged_list[i]['value'] + result['value']
                find_flag = True
            i = i + 1
        if find_flag == False:
            merged_list.append({'hash': result['hash'], 'timeStamp': result['timeStamp'], 'from': result['from'], 'to': result['to'], 'value': result['value'], 'isError': result['isError'], 'contractAddress': result['contractAddress']})
    for result in internal_transaction['result']:
        i = 0
        find_flag = False
        for merged_transaction in merged_list:
            if merged_transaction['hash'] == result['hash']:
                merged_list[i]['value'] = merged_list[i]['value'] + result['value']
                find_flag = True
            i = i + 1
        if find_flag == False:
            merged_list.append({'hash': result['hash'], 'timeStamp': result['timeStamp'], 'from': result['from'], 'to': result['to'], 'value': result['value'], 'isError': result['isError'], 'contractAddress': result['contractAddress']})
    merged_list = sorted(merged_list, key=lambda i: i['timeStamp'])
    return merged_list

def merge_transaction_list(normal_transaction, internal_transaction, erc_transaction, nft_transcations, erc1155_transcations):
    merged_list = []
    for result in normal_transaction['result']:
        i = 0
        find_flag = False
        for merged_transaction in merged_list:
            if merged_transaction['hash'] == result['hash']:
                merged_list[i]['value'] = merged_list[i]['value'] + result['value']
                find_flag = True
            i = i + 1
        if find_flag == False:
            merged_list.append({'hash': result['hash'], 'timeStamp': result['timeStamp'], 'from': result['from'], 'to': result['to'], 'value': result['value'], 'contractAddress': result['contractAddress']})
    for result in internal_transaction['result']:
        i = 0
        find_flag = False
        for merged_transaction in merged_list:
            if merged_transaction['hash'] == result['hash']:
                merged_list[i]['value'] = merged_list[i]['value'] + result['value']
                find_flag = True
            i = i + 1
        if find_flag == False:
            merged_list.append({'hash': result['hash'], 'timeStamp': result['timeStamp'], 'from': result['from'], 'to': result['to'], 'value': result['value'], 'contractAddress': result['contractAddress']})
    for result in erc_transaction['result']:
        i = 0
        find_flag = False
        for merged_transaction in merged_list:
            if merged_transaction['hash'] == result['hash']:
                merged_list[i]['value'] = merged_list[i]['value'] + result['value']
                find_flag = True
            i = i + 1
        if find_flag == False:
            merged_list.append({'hash': result['hash'], 'timeStamp': result['timeStamp'], 'from': result['from'], 'to': result['to'], 'value': result['value'], 'contractAddress': result['contractAddress']})
    for result in nft_transcations['result']:
        i = 0
        find_flag = False
        for merged_transaction in merged_list:
            if merged_transaction['hash'] == result['hash']:
                merged_list[i]['value'] = merged_list[i]['value'] + result['value']
                find_flag = True
            i = i + 1
        if find_flag == False:
            merged_list.append({'hash': result['hash'], 'timeStamp': result['timeStamp'], 'from': result['from'], 'to': result['to'], 'value': result['value'], 'contractAddress': result['contractAddress']})
    for result in erc1155_transcations['result']:
        i = 0
        find_flag = False
        for merged_transaction in merged_list:
            if merged_transaction['hash'] == result['hash']:
                merged_list[i]['value'] = merged_list[i]['value'] + result['value']
                find_flag = True
            i = i + 1
        if find_flag == False:
            merged_list.append({'hash': result['hash'], 'timeStamp': result['timeStamp'], 'from': result['from'], 'to': result['to'], 'value': result['value'], 'contractAddress': result['contractAddress']})
    merged_list = sorted(merged_list, key=lambda i: i['timeStamp'])
    return merged_list

def merge_normal_internal(normal_transaction):
    merged_list = []
    for result in normal_transaction['result']:
        if result['value']:
            formatted_value = int(result['value'])
        else:
            formatted_value = 0
        i = 0
        find_flag = False
        for merged_transaction in merged_list:
            if merged_transaction['hash'] == result['hash']:
                merged_list[i]['value'] = merged_list[i]['value'] + formatted_value
                find_flag = True
            i = i + 1
        if find_flag == False:
            merged_list.append({'hash': result['hash'], 'timeStamp': result['timeStamp'], 'from': result['from'], 'to': result['to'], 'value': formatted_value, 'isError': result['isError'], 'contractAddress': result['contractAddress']})
    return {'result': merged_list}

def merge_erc20(erc_transcations):
    merged_list = []
    for result in erc_transcations['result']:
        if result['value']:
            formatted_value = int(result['value'])
        else:
            formatted_value = 0
        if result['tokenDecimal']:
            formartted_tokendecimal = int(result['tokenDecimal'])
        else:
            formartted_tokendecimal = 0
        i = 0
        find_flag = False
        for merged_transaction in merged_list:
            if merged_transaction['hash'] == result['hash']:
                j = 0
                decimal = 1
                while j < formartted_tokendecimal:
                    decimal = decimal * 10
                    j = j + 1
                if formartted_tokendecimal != 0:
                    merged_list[i]['value'] = merged_list[i]['value'] + formatted_value / decimal * 1000000000000000000
                else:
                    merged_list[i]['value'] = merged_list[i]['value'] + 0
                find_flag = True
            i = i + 1
        if find_flag == False:
            j = 0
            decimal = 1
            while j < formartted_tokendecimal:
                decimal = decimal * 10
                j = j + 1
            if formartted_tokendecimal != 0:
                merged_list.append({'hash': result['hash'], 'timeStamp': result['timeStamp'], 'from': result['from'], 'to': result['to'], 'value': formatted_value / decimal * 1000000000000000000, 'contractAddress': result['contractAddress']})
            else:
                merged_list.append({'hash': result['hash'], 'timeStamp': result['timeStamp'], 'from': result['from'], 'to': result['to'], 'value': 0, 'contractAddress': result['contractAddress']})
    return {'result': merged_list}

def merge_nft(nft_transactions):
    merged_list = []
    for result in nft_transactions['result']:
        i = 0
        find_flag = False
        for merged_transaction in merged_list:
            if merged_transaction['hash'] == result['hash']:
                merged_list[i]['value'] = merged_list[i]['value'] + 1000000000000000000
                find_flag = True
            i = i + 1
        if find_flag == False:
            merged_list.append({'hash': result['hash'], 'timeStamp': result['timeStamp'], 'from': result['from'], 'to': result['to'], 'value': 1000000000000000000, 'contractAddress': result['contractAddress']})
    return {'result': merged_list}

def merge_1155(erc1155_transactions):
    merged_list = []
    for result in erc1155_transactions['result']:
        if result['tokenValue']:
            formatted_value = int(result['tokenValue'])
        else:
            formatted_value = 0
        i = 0
        find_flag = False
        for merged_transaction in merged_list:
            if merged_transaction['hash'] == result['hash']:
                merged_list[i]['value'] = merged_list[i]['value'] + formatted_value * 1000000000000000000
                find_flag = True
            i = i + 1
        if find_flag == False:
            merged_list.append({'hash': result['hash'], 'timeStamp': result['timeStamp'], 'from': result['from'], 'to': result['to'], 'value': formatted_value * 1000000000000000000, 'contractAddress': result['contractAddress']})
    return {'result': merged_list}

def get_minimum_value_in_Ether_ever_received(apikey, address, time_window, transcations, merged_list, current_time):
    first_flag = False
    min_amount = -1

    transcation_time_list = []
    for result in transcations['result']:
        transcation_time_list.append(result['timeStamp'])
    transcation_time_list = sorted(transcation_time_list)
    if transcation_time_list:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["to"].lower() == address.lower() or (result["to"] == "" and result["contractAddress"].lower() == address.lower()):
                    if first_flag == False:
                        min_amount = result['value']
                    elif result['value'] < min_amount:
                        min_amount = result['value']
                        first_flag = True
    return min_amount

def get_maximum_value_in_Ether_ever_received(apikey, address, time_window, transcations, merged_list, current_time):
    first_flag = False
    max_amount = -1
    transcation_time_list = []
    for result in transcations['result']:
        transcation_time_list.append(result['timeStamp'])
    transcation_time_list = sorted(transcation_time_list)
    if transcation_time_list:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["to"].lower() == address.lower() or (result["to"] == "" and result["contractAddress"].lower() == address.lower()):
                    if first_flag == False:
                        max_amount = result['value']
                    elif result['value'] < max_amount:
                        max_amount = result['value']
                        first_flag = True
    return max_amount

def get_avg_value_in_Ether_ever_received(apikey, address, time_window, transcations, merged_list, current_time):

    count = 0
    avg_amount = 0
    transcation_time_list = []
    for result in transcations['result']:
        transcation_time_list.append(result['timeStamp'])
    transcation_time_list = sorted(transcation_time_list)
    if transcation_time_list:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["to"].lower() == address.lower() or (result["to"] == "" and result["contractAddress"].lower() == address.lower()):
                    avg_amount = avg_amount + float(result['value'])
                    count = count + 1
    if count != 0:
        avg_amount = avg_amount/count
    else:
        avg_amount = -1
    return avg_amount

def get_minimum_value_in_Ether_ever_sent(apikey, address, time_window, transcations, merged_list, current_time):

    first_flag = False
    min_amount = -1
    transcation_time_list = []
    for result in transcations['result']:
        transcation_time_list.append(result['timeStamp'])
    transcation_time_list = sorted(transcation_time_list)
    if transcation_time_list:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["from"].lower() == address.lower():
                    if first_flag == False:
                        min_amount = result['value']
                    elif result['value'] < min_amount:
                        min_amount = result['value']
                        first_flag = True
    return min_amount

def get_maximum_value_in_Ether_ever_sent(apikey, address, time_window, transcations, merged_list, current_time):

    first_flag = False
    max_amount = -1
    transcation_time_list = []
    for result in transcations['result']:
        transcation_time_list.append(result['timeStamp'])
    transcation_time_list = sorted(transcation_time_list)
    if transcation_time_list:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["from"].lower() == address.lower():
                    if first_flag == False:
                        max_amount = result['value']
                    elif result['value'] < max_amount:
                        max_amount = result['value']
                        first_flag = True
    return max_amount

def get_avg_value_in_Ether_ever_sent(apikey, address, time_window, transcations, merged_list, current_time):
    count = 0
    avg_amount = 0
    transcation_time_list = []
    for result in transcations['result']:
        transcation_time_list.append(result['timeStamp'])
    transcation_time_list = sorted(transcation_time_list)
    if transcation_time_list:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["from"].lower() == address.lower():
                    avg_amount = avg_amount + float(result['value'])
                    count = count + 1
    if count != 0:
        avg_amount = avg_amount/count
    else:
        avg_amount = -1
    return avg_amount

def get_total_value_in_Ether_ever_received(apikey, address, time_window, transcations, merged_list, current_time):
    total_amount = 0
    count = 0
    transcation_time_list = []
    for result in transcations['result']:
        transcation_time_list.append(result['timeStamp'])
    transcation_time_list = sorted(transcation_time_list)
    if transcation_time_list:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["to"].lower() == address.lower() or (result["to"] == "" and result["contractAddress"].lower() == address.lower()):
                    count = count + 1
                    total_amount = total_amount + float(result['value'])
    if count != 0:
        return total_amount
    else:
        return -1

def get_total_value_in_Ether_ever_sent(apikey, address, time_window, transcations, merged_list, current_time):
    total_amount = 0
    count = 0
    transcation_time_list = []
    for result in transcations['result']:
        transcation_time_list.append(result['timeStamp'])
    transcation_time_list = sorted(transcation_time_list)
    if transcation_time_list:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["from"].lower() == address.lower():
                    count = count + 1
                    total_amount = total_amount + float(result['value'])
    if count != 0:
        return total_amount
    else:
        return -1

def get_the_number_of_transactions_per_day(apikey, address, time_window, transcations, merged_list, current_time):
    transcation_time_list = []
    for result in transcations['result']:
        transcation_time_list.append(result['timeStamp'])
    transcation_time_list = sorted(transcation_time_list)
    if transcation_time_list:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        transcation_list = []
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                transcation_list.append(result['timeStamp'])
        transcation_list = sorted(transcation_list)
        if len(transcation_list) > 1:
            if close_time < current_time:
                day = (close_time - int(merged_list[0]['timeStamp']))/86400
                if day == 0:
                    day = 1
                result = len(transcation_list)/day
                return result
            else:
                day = (current_time - int(merged_list[0]['timeStamp']))/86400
                if day == 0:
                    day = 1
                result = len(transcation_list)/day
                return result
    return -1

def get_the_number_of_incoming_transactions_per_day(apikey, address, time_window, transcations, merged_list, current_time):
    transcation_time_list_x = []
    for result in transcations['result']:
        transcation_time_list_x.append(result['timeStamp'])
    transcation_time_list_x = sorted(transcation_time_list_x)
    if transcation_time_list_x:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        transaction_list = []
        transaction_time_list = []
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["to"].lower() == address.lower() or (result["to"] == "" and result["contractAddress"].lower() == address.lower()):
                    transaction_list.append(result['timeStamp'])
                transaction_time_list.append(result['timeStamp'])
        transaction_time_list = sorted(transaction_time_list)
        if len(transaction_time_list) > 1:
            if close_time < current_time:
                day = (close_time - int(merged_list[0]['timeStamp'])) / 86400
                if day == 0:
                    day = 1
                result = len(transaction_list)/day
                return result
            else:
                day = (current_time - int(merged_list[0]['timeStamp'])) / 86400
                if day == 0:
                    day = 1
                result = len(transaction_list)/day
                return result
    return -1

def get_the_number_of_outcoming_transactions_per_day(apikey, address, time_window, transcations, merged_list, current_time):
    transcation_time_list_x = []
    for result in transcations['result']:
        transcation_time_list_x.append(result['timeStamp'])
    transcation_time_list_x = sorted(transcation_time_list_x)
    if transcation_time_list_x:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        transaction_list = []
        transaction_time_list = []
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["from"].lower() == address.lower():
                    transaction_list.append(result['timeStamp'])
                transaction_time_list.append(result['timeStamp'])
        transaction_time_list = sorted(transaction_time_list)
        if len(transaction_time_list) > 1:
            if close_time < current_time:
                day = (close_time - int(merged_list[0]['timeStamp'])) / 86400
                if day == 0:
                    day = 1
                result = len(transaction_list) / day
                return result
            else:
                day = (current_time - int(merged_list[0]['timeStamp'])) / 86400
                if day == 0:
                    day = 1
                result = len(transaction_list) / day
                return result
    return -1

def get_the_number_of_incoming_transactions_per_month(apikey, address, time_window, transcations, merged_list, current_time):
    transcation_time_list_x = []
    for result in transcations['result']:
        transcation_time_list_x.append(result['timeStamp'])
    transcation_time_list_x = sorted(transcation_time_list_x)
    if transcation_time_list_x:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        transaction_list = []
        transaction_time_list = []
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["to"].lower() == address.lower() or (result["to"] == "" and result["contractAddress"].lower() == address.lower()):
                    transaction_list.append(result['timeStamp'])
                transaction_time_list.append(result['timeStamp'])
        transaction_time_list = sorted(transaction_time_list)
        if len(transaction_time_list) > 1:
            if close_time < current_time:
                day = (close_time - int(merged_list[0]['timeStamp'])) / 2592000
                if day == 0:
                    day = 1
                result = len(transaction_list)/day
                return result
            else:
                day = (current_time - int(merged_list[0]['timeStamp'])) / 2592000
                if day == 0:
                    day = 1
                result = len(transaction_list)/day
                return result
    return -1

def get_the_number_of_outcoming_transactions_per_month(apikey, address, time_window, transcations, merged_list, current_time):
    transcation_time_list_x = []
    for result in transcations['result']:
        transcation_time_list_x.append(result['timeStamp'])
    transcation_time_list_x = sorted(transcation_time_list_x)
    if transcation_time_list_x:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        transaction_list = []
        transaction_time_list = []
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["from"].lower() == address.lower():
                    transaction_list.append(result['timeStamp'])
                transaction_time_list.append(result['timeStamp'])
        transaction_time_list = sorted(transaction_time_list)
        if len(transaction_time_list) > 1:
            if close_time < current_time:
                day = (close_time - int(merged_list[0]['timeStamp'])) / 2592000
                if day == 0:
                    day = 1
                result = len(transaction_list) / day
                return result
            else:
                day = (current_time - int(merged_list[0]['timeStamp'])) / 2592000
                if day == 0:
                    day = 1
                result = len(transaction_list) / day
                return result
    return -1

def get_the_number_of_transactions_per_hour(apikey, address, time_window, transcations, merged_list, current_time):
    transcation_time_list_x = []
    for result in transcations['result']:
        transcation_time_list_x.append(result['timeStamp'])
    transcation_time_list_x = sorted(transcation_time_list_x)
    if transcation_time_list_x:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        transcation_list = []
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                transcation_list.append(result['timeStamp'])
        transcation_list = sorted(transcation_list)
        if len(transcation_list) > 1:
            if close_time < current_time:
                day = (close_time - int(merged_list[0]['timeStamp']))/3600
                if day == 0:
                    day = 1
                result = len(transcation_list)/day
                return result
            else:
                day = (current_time - int(merged_list[0]['timeStamp']))/3600
                if day == 0:
                    day = 1
                result = len(transcation_list)/day
                return result
    return -1

def get_the_number_of_incoming_transactions_per_hour(apikey, address, time_window, transcations, merged_list, current_time):
    transcation_time_list_x = []
    for result in transcations['result']:
        transcation_time_list_x.append(result['timeStamp'])
    transcation_time_list_x = sorted(transcation_time_list_x)
    if transcation_time_list_x:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        transaction_list = []
        transaction_time_list = []
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["to"].lower() == address.lower() or (result["to"] == "" and result["contractAddress"].lower() == address.lower()):
                    transaction_list.append(result['timeStamp'])
                transaction_time_list.append(result['timeStamp'])
        transaction_time_list = sorted(transaction_time_list)
        if len(transaction_time_list) > 1:
            if close_time < current_time:
                day = (close_time - int(merged_list[0]['timeStamp'])) / 3600
                if day == 0:
                    day = 1
                result = len(transaction_list)/day
                return result
            else:
                day = (current_time - int(merged_list[0]['timeStamp'])) / 3600
                if day == 0:
                    day = 1
                result = len(transaction_list)/day
                return result
    return -1

def get_the_number_of_outcoming_transactions_per_hour(apikey, address, time_window, transcations, merged_list, current_time):
    transcation_time_list_x = []
    for result in transcations['result']:
        transcation_time_list_x.append(result['timeStamp'])
    transcation_time_list_x = sorted(transcation_time_list_x)
    if transcation_time_list_x:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        transaction_list = []
        transaction_time_list = []
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["from"].lower() == address.lower():
                    transaction_list.append(result['timeStamp'])
                transaction_time_list.append(result['timeStamp'])
        transaction_time_list = sorted(transaction_time_list)
        if len(transaction_time_list) > 1:
            if close_time < current_time:
                day = (close_time - int(merged_list[0]['timeStamp'])) / 3600
                if day == 0:
                    day = 1
                result = len(transaction_list) / day
                return result
            else:
                day = (current_time - int(merged_list[0]['timeStamp'])) / 3600
                if day == 0:
                    day = 1
                result = len(transaction_list) / day
                return result
    return -1

def get_the_number_of_amounts_per_day(apikey, address, time_window, transcations, merged_list, current_time):
    total_amount = 0
    transcation_time_list_x = []
    for result in transcations['result']:
        transcation_time_list_x.append(result['timeStamp'])
    transcation_time_list_x = sorted(transcation_time_list_x)
    if transcation_time_list_x:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        transcation_list = []
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                transcation_list.append(result['timeStamp'])
                total_amount = total_amount + float(result['value'])
        transcation_list = sorted(transcation_list)
        if len(transcation_list) > 1:
            if close_time < current_time:
                day = (close_time - int(merged_list[0]['timeStamp']))/86400
                if day == 0:
                    day = 1
                result = total_amount/day
                return result
            else:
                day = (current_time - int(merged_list[0]['timeStamp'])) / 86400
                if day == 0:
                    day = 1
                result = total_amount / day
                return result
    return -1

def get_the_number_of_incoming_amounts_per_day(apikey, address, time_window, transcations, merged_list, current_time):
    total_amount = 0
    transcation_time_list_x = []
    for result in transcations['result']:
        transcation_time_list_x.append(result['timeStamp'])
    transcation_time_list_x = sorted(transcation_time_list_x)
    if transcation_time_list_x:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        transcation_list = []
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                transcation_list.append(result['timeStamp'])
                if result["to"].lower() == address.lower() or (result["to"] == "" and result["contractAddress"].lower() == address.lower()):
                    total_amount = total_amount + float(result['value'])
        transcation_list = sorted(transcation_list)
        if len(transcation_list) > 1:
            if close_time < current_time:
                day = (close_time - int(merged_list[0]['timeStamp']))/86400
                if day == 0:
                    day = 1
                result = total_amount/day
                return result
        else:
            day = (current_time - int(merged_list[0]['timeStamp'])) / 86400
            if day == 0:
                day = 1
            result = total_amount / day
            return result
    return -1

def get_the_number_of_outcoming_amounts_per_day(apikey, address, time_window, transcations, merged_list, current_time):
    total_amount = 0
    transcation_time_list_x = []
    for result in transcations['result']:
        transcation_time_list_x.append(result['timeStamp'])
    transcation_time_list_x = sorted(transcation_time_list_x)
    if transcation_time_list_x:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        transcation_list = []
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                transcation_list.append(result['timeStamp'])
                if result["from"].lower() == address.lower():
                    total_amount = total_amount + float(result['value'])

        transcation_list = sorted(transcation_list)
        if len(transcation_list) > 1:
            if close_time < current_time:
                day = (close_time - int(merged_list[0]['timeStamp']))/86400
                if day == 0:
                    day = 1
                result = total_amount/day
                return result
        else:
            day = (current_time - int(merged_list[0]['timeStamp'])) / 86400
            if day == 0:
                day = 1
            result = total_amount / day
            return result

    return -1

def get_the_number_of_incoming_amounts_per_month(apikey, address, time_window, transcations, merged_list, current_time):
    total_amount = 0
    transcation_time_list_x = []
    for result in transcations['result']:
        transcation_time_list_x.append(result['timeStamp'])
    transcation_time_list_x = sorted(transcation_time_list_x)
    if transcation_time_list_x:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        transcation_list = []
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                transcation_list.append(result['timeStamp'])
                if result["to"].lower() == address.lower() or (result["to"] == "" and result["contractAddress"].lower() == address.lower()):
                    total_amount = total_amount + float(result['value'])
        transcation_list = sorted(transcation_list)
        if len(transcation_list) > 1:
            if close_time < current_time:
                day = (close_time - int(merged_list[0]['timeStamp']))/2592000
                if day == 0:
                    day = 1
                result = total_amount/day
                return result
        else:
            day = (current_time - int(merged_list[0]['timeStamp'])) / 2592000
            if day == 0:
                day = 1
            result = total_amount / day
            return result
    return -1

def get_the_number_of_outcoming_amounts_per_month(apikey, address, time_window, transcations, merged_list, current_time):
    total_amount = 0
    transcation_time_list_x = []
    for result in transcations['result']:
        transcation_time_list_x.append(result['timeStamp'])
    transcation_time_list_x = sorted(transcation_time_list_x)
    if transcation_time_list_x:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        transcation_list = []
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                transcation_list.append(result['timeStamp'])
                if result["from"].lower() == address.lower():
                    total_amount = total_amount + float(result['value'])

        transcation_list = sorted(transcation_list)
        if len(transcation_list) > 1:
            if close_time < current_time:
                day = (close_time - int(merged_list[0]['timeStamp']))/2592000
                if day == 0:
                    day = 1
                result = total_amount/day
                return result
        else:
            day = (current_time - int(merged_list[0]['timeStamp'])) / 2592000
            if day == 0:
                day = 1
            result = total_amount / day
            return result

    return -1

def get_the_number_of_amounts_per_hour(apikey, address, time_window, transcations, merged_list, current_time):
    total_amount = 0
    transcation_time_list_x = []
    for result in transcations['result']:
        transcation_time_list_x.append(result['timeStamp'])
    transcation_time_list_x = sorted(transcation_time_list_x)
    if transcation_time_list_x:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        transcation_list = []
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                transcation_list.append(result['timeStamp'])
                total_amount = total_amount + float(result['value'])
        transcation_list = sorted(transcation_list)
        if len(transcation_list) > 1:
            if close_time < current_time:
                day = (close_time - int(merged_list[0]['timeStamp']))/3600
                if day == 0:
                    day = 1
                result = total_amount/day
                return result
            else:
                day = (current_time - int(merged_list[0]['timeStamp'])) / 3600
                if day == 0:
                    day = 1
                result = total_amount / day
                return result
    return -1

def get_the_total_number_of_amounts_outcoming_plus_incoming(apikey, address, time_window, transcations, merged_list, current_time):
    total_amount = 0
    transcation_time_list_x = []
    for result in transcations['result']:
        transcation_time_list_x.append(result['timeStamp'])
    transcation_time_list_x = sorted(transcation_time_list_x)
    if transcation_time_list_x:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        zero_flag = True
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                total_amount = total_amount + float(result['value'])
                zero_flag = False
        if zero_flag == False:
            return total_amount
    return -1

def get_the_number_of_incoming_amounts_per_hour(apikey, address, time_window, transcations, merged_list, current_time):
    total_amount = 0
    transcation_time_list_x = []
    for result in transcations['result']:
        transcation_time_list_x.append(result['timeStamp'])
    transcation_time_list_x = sorted(transcation_time_list_x)
    if transcation_time_list_x:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        transcation_list = []
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                transcation_list.append(result['timeStamp'])
                if result["to"].lower() == address.lower() or (result["to"] == "" and result["contractAddress"].lower() == address.lower()):
                    total_amount = total_amount + float(result['value'])
        transcation_list = sorted(transcation_list)
        if len(transcation_list) > 1:
            if close_time < current_time:
                day = (close_time - int(merged_list[0]['timeStamp']))/3600
                if day == 0:
                    day = 1
                result = total_amount/day
                return result
        else:
            day = (current_time - int(merged_list[0]['timeStamp'])) /3600
            if day == 0:
                day = 1
            result = total_amount / day
            return result
    return -1

def get_the_number_of_outcoming_amounts_per_hour(apikey, address, time_window, transcations, merged_list, current_time):
    total_amount = 0
    transcation_time_list_x = []
    for result in transcations['result']:
        transcation_time_list_x.append(result['timeStamp'])
    transcation_time_list_x = sorted(transcation_time_list_x)
    if transcation_time_list_x:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        transcation_list = []
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                transcation_list.append(result['timeStamp'])
                if result["from"].lower() == address.lower():
                    total_amount = total_amount + float(result['value'])

        transcation_list = sorted(transcation_list)
        if len(transcation_list) > 1:
            if close_time < current_time:
                day = (close_time - int(merged_list[0]['timeStamp']))/3600
                if day == 0:
                    day = 1
                result = total_amount/day
                return result
        else:
            day = (current_time - int(merged_list[0]['timeStamp'])) /3600
            if day == 0:
                day = 1
            result = total_amount / day
            return result

    return -1

def get_reverted_numbers(apikey, address, time_window, transcations, merged_list, current_time):
    count = 0
    transcation_time_list_x = []
    for result in transcations['result']:
        transcation_time_list_x.append(result['timeStamp'])
    transcation_time_list_x = sorted(transcation_time_list_x)
    if transcation_time_list_x:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result['isError'] == '1':
                    count = count + 1
    return count


def get_proportion_of_incoming_address_transactions(apikey, address, time_window, transcations, merged_list, current_time):
    incoming = get_the_total_number_of_incoming_transactions(apikey, address, time_window, transcations, merged_list, current_time)
    total = get_total_number_of_transactions(apikey, address, time_window, transcations, merged_list, current_time)
    if incoming == -1 or total == -1:
        return -1
    if total != 0:
        result = incoming/total
    else:
        result = -1
    return result

def get_proportion_of_outcoming_address_transactions(apikey, address, time_window, transcations, merged_list, current_time):
    outcoming = get_the_total_number_of_outcoming_transactions(apikey, address, time_window, transcations, merged_list, current_time)
    total = get_total_number_of_transactions(apikey, address, time_window, transcations, merged_list, current_time)
    if outcoming == -1 or total == -1:
        return -1
    if total != 0:
        result = outcoming/total
    else:
        result = -1
    return result

def get_the_proportion_of_unique_incoming_address_transactions(apikey, address, time_window, transcations, merged_list, current_time):
    unique = get_the_number_of_unique_incoming_addresses(apikey, address, time_window, transcations, merged_list, current_time)
    total = get_the_total_number_of_incoming_transactions(apikey, address, time_window, transcations, merged_list, current_time)
    if unique == -1 or total == -1:
        return -1
    if total != 0:
        result = unique/total
    else:
        result = -1
    return result

def get_the_proportion_of_unique_outcoming_address_transactions(apikey, address, time_window, transcations, merged_list, current_time):
    unique = get_the_number_of_unique_outcoming_addresses(apikey, address, time_window, transcations, merged_list, current_time)
    total = get_the_total_number_of_outcoming_transactions(apikey, address, time_window, transcations, merged_list, current_time)
    if unique == -1 or total == -1:
        return -1
    if total != 0:
        result = unique/total
    else:
        result = -1
    return result

def get_the_total_number_of_outcoming_transactions(apikey, address, time_window, transcations, merged_list, current_time):
    addresses = []
    transcation_time_list_x = []
    for result in transcations['result']:
        transcation_time_list_x.append(result['timeStamp'])
    transcation_time_list_x = sorted(transcation_time_list_x)
    if transcation_time_list_x:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["from"].lower() == address.lower():
                    addresses.append(result["to"].lower())
        return len(addresses)
    return -1


def get_the_total_number_of_incoming_transactions(apikey, address, time_window, transcations, merged_list, current_time):
    addresses = []
    transcation_time_list_x = []
    for result in transcations['result']:
        transcation_time_list_x.append(result['timeStamp'])
    transcation_time_list_x = sorted(transcation_time_list_x)
    if transcation_time_list_x:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["to"].lower() == address.lower() or (result["to"] == "" and result["contractAddress"].lower() == address.lower()):
                    addresses.append(result["to"].lower())
        return len(addresses)
    return -1
    
def get_the_number_of_unique_incoming_addresses(apikey, address, time_window, transcations, merged_list, current_time):
    unique_list = []
    transcation_time_list_x = []
    for result in transcations['result']:
        transcation_time_list_x.append(result['timeStamp'])
    transcation_time_list_x = sorted(transcation_time_list_x)
    if transcation_time_list_x:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["to"].lower() == address.lower() or (result["to"] == "" and result["contractAddress"].lower() == address.lower()):
                    if result["from"].lower() not in unique_list:
                        unique_list.append(result["from"].lower())
        return len(unique_list)
    return -1

def get_the_number_of_unique_outcoming_addresses(apikey, address, time_window, transcations, merged_list, current_time):
    unique_list = []
    transcation_time_list_x = []
    for result in transcations['result']:
        transcation_time_list_x.append(result['timeStamp'])
    transcation_time_list_x = sorted(transcation_time_list_x)
    if transcation_time_list_x:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["from"].lower() == address.lower():
                    if result["to"] == "" and result["contractAddress"] != "":
                        if result["contractAddress"].lower() not in unique_list:
                            unique_list.append(result["contractAddress"].lower())
                    elif result["to"].lower() not in unique_list:
                        unique_list.append(result["to"].lower())
        return len(unique_list)
    return -1

def get_total_number_of_transactions(apikey, address, time_window, transcations, merged_list, current_time):
    transcation_time_list_x = []
    for result in transcations['result']:
        transcation_time_list_x.append(result['timeStamp'])
    transcation_time_list_x = sorted(transcation_time_list_x)
    if transcation_time_list_x:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        transcation_list = []
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                transcation_list.append(result)
        return len(transcation_list)
    return -1

def get_shortest_interval_between_two_transactions(apikey, address, time_window, transcations, merged_list, current_time):
    timestamp = []
    transcation_time_list_x = []
    for result in transcations['result']:
        transcation_time_list_x.append(result['timeStamp'])
    transcation_time_list_x = sorted(transcation_time_list_x)
    if transcation_time_list_x:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600

        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                timestamp.append(result['timeStamp'])
        i = 0
        shortest = None
        while (i+1) < len(timestamp):
            if shortest == None:
                shortest = int(timestamp[i+1]) - int(timestamp[i])
            elif shortest > int(timestamp[i+1]) - int(timestamp[i]):
                shortest = int(timestamp[i+1]) - int(timestamp[i])
            i = i + 1
        if shortest != None:
            return shortest
    return -1

def get_longest_interval_between_two_transactions(apikey, address, time_window, transcations, merged_list, current_time):
    transcation_time_list_x = []
    for result in transcations['result']:
        transcation_time_list_x.append(result['timeStamp'])
    transcation_time_list_x = sorted(transcation_time_list_x)
    if transcation_time_list_x:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        timestamp = []
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                timestamp.append(result['timeStamp'])
        i = 0
        longest = None
        while (i+1) < len(timestamp):
            if longest == None:
                longest = int(timestamp[i+1]) - int(timestamp[i])
            elif longest < int(timestamp[i+1]) - int(timestamp[i]):
                longest = int(timestamp[i+1]) - int(timestamp[i])
            i = i + 1
        if longest != None:
            return longest
    return -1


def time_since_the_first_until_the_last_transaction(apikey, address, time_window, transcations, merged_list, current_time):
    transcation_time_list_x = []
    for result in transcations['result']:
        transcation_time_list_x.append(result['timeStamp'])
    transcation_time_list_x = sorted(transcation_time_list_x)
    if transcation_time_list_x:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        timestamp = []
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                timestamp.append(result['timeStamp'])
        if len(timestamp) > 0:
            timestamp.sort()
            gap = int(timestamp[-1]) - int(timestamp[0])
            return gap
    return -1


def get_average_time_between_outcoming_transactions(apikey, address, time_window, transcations, merged_list, current_time):
    transcation_time_list_x = []
    for result in transcations['result']:
        transcation_time_list_x.append(result['timeStamp'])
    transcation_time_list_x = sorted(transcation_time_list_x)
    if transcation_time_list_x:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        timestamp = []
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["from"].lower() == address.lower():
                    timestamp.append(result['timeStamp'])
        timestamp.sort()
        total_time = 0
        i = 0
        while (i+1) < len(timestamp):
            total_time = total_time + (int(timestamp[i+1]) - int(timestamp[i]))
            i = i + 1
        if len(timestamp) == 1:
            return close_time - int(timestamp[0])
        elif i != 0:
            avg_time = total_time/i
            return avg_time
    return -1

def get_average_time_between_incoming_transactions(apikey, address, time_window, transcations, merged_list, current_time):
    transcation_time_list_x = []
    for result in transcations['result']:
        transcation_time_list_x.append(result['timeStamp'])
    transcation_time_list_x = sorted(transcation_time_list_x)
    if transcation_time_list_x:
        first_time = merged_list[0]['timeStamp']
        close_time = int(first_time) + time_window * 3600
        timestamp = []
        for result in transcations['result']:
            if int(result['timeStamp']) < close_time:
                if result["to"].lower() == address.lower() or (result["to"] == "" and result["contractAddress"].lower() == address.lower()):
                    timestamp.append(result['timeStamp'])
        timestamp.sort()
        total_time = 0
        i = 0
        while (i + 1) < len(timestamp):
            total_time = total_time + (int(timestamp[i + 1]) - int(timestamp[i]))
            i = i + 1
        if len(timestamp) == 1:
            return close_time - int(timestamp[0])
        elif i != 0:
            avg_time = total_time / i
            return avg_time
    return -1

def get_malicious_address():
    malicious_list = []
    with open('malicious.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            line = line.replace('\n', '')
            line = line.upper()
            malicious_list.append(line)
    return malicious_list


if __name__=='__main__':
    csv_address = output + '.csv'
    apikey = '8E8QHCXJS9F1GW7EUTHVV4RXX1IY1Z543D'
    write_list = []
    write_list.append('address')
    write_list.append('category')
    time_window_list = [350400]
    malicious_list = get_malicious_address()
    for time_hours in time_window_list:
        if time_hours >= 24:
            time_str = ' (' + str(time_hours/24) + 'days)'
        else:
            time_str = ' (' + str(time_hours) + 'hours)'
        write_list.append('average_time_between_incoming_transactions_normal' + time_str)
        write_list.append('average_time_between_outcoming_transactions_normal' + time_str)
        write_list.append('time_since_the_first_until_the_last_transaction_normal' + time_str)
        write_list.append('longest_interval_between_two_transactions_normal' + time_str)
        write_list.append('shortest_interval_between_two_transactions_normal' + time_str)
        write_list.append('total_number_of_transactions_normal' + time_str)
        write_list.append('the_number_of_unique_outcoming_addresses_normal' + time_str)
        write_list.append('the_number_of_unique_incoming_addresses_normal' + time_str)
        write_list.append('the_total_number_of_incoming_transactions_normal' + time_str)
        write_list.append('the_total_number_of_outcoming_transactions_normal' + time_str)
        write_list.append('the_proportion_of_unique_outcoming_address_transactions_normal' + time_str)
        write_list.append('the_proportion_of_unique_incoming_address_transactions_normal' + time_str)
        write_list.append('proportion_of_outcoming_address_transactions_normal' + time_str)
        write_list.append('proportion_of_incoming_address_transactions_normal' + time_str)
        write_list.append('minimum_value_in_Ether_ever_received_normal' + time_str)
        write_list.append('maximum_value_in_Ether_ever_received_normal' + time_str)
        write_list.append('avg_value_in_Ether_ever_received_normal' + time_str)
        write_list.append('minimum_value_in_Ether_ever_sent_normal' + time_str)
        write_list.append('maximum_value_in_Ether_ever_sent_normal' + time_str)
        write_list.append('avg_value_in_Ether_ever_sent_normal' + time_str)
        write_list.append('total_value_in_Ether_ever_received_normal' + time_str)
        write_list.append('total_value_in_Ether_ever_sent_normal' + time_str)
        write_list.append('the_number_of_transactions_per_day_normal' + time_str)
        write_list.append('the_number_of_incoming_transactions_per_day_normal' + time_str)
        write_list.append('the_number_of_outcoming_transactions_per_day_normal' + time_str)
        write_list.append('the_number_of_incoming_transactions_per_hour_normal' + time_str)
        write_list.append('the_number_of_outcoming_transactions_per_hour_normal' + time_str)
        write_list.append('the_number_of_incoming_amounts_per_day_normal' + time_str)
        write_list.append('the_number_of_outcoming_amounts_per_day_normal' + time_str)
        write_list.append('the_total_number_of_amounts_outcoming_plus_incoming_normal' + time_str)
        write_list.append('the_number_of_incoming_amounts_per_hour_normal' + time_str)
        write_list.append('the_number_of_outcoming_amounts_per_hour_normal' + time_str)
        write_list.append('the_number_of_transactions_per_hour_normal' + time_str)
        write_list.append('the_number_of_amounts_per_day_normal' + time_str)
        write_list.append('the_number_of_amounts_per_hour_normal' + time_str)
        write_list.append('reverted_numbers_normal' + time_str)

        write_list.append('average_time_between_incoming_transactions_internal' + time_str)
        write_list.append('average_time_between_outcoming_transactions_internal' + time_str)
        write_list.append('time_since_the_first_until_the_last_transaction_internal' + time_str)
        write_list.append('longest_interval_between_two_transactions_internal' + time_str)
        write_list.append('shortest_interval_between_two_transactions_internal' + time_str)
        write_list.append('total_number_of_transactions_internal' + time_str)
        write_list.append('the_number_of_unique_outcoming_addresses_internal' + time_str)
        write_list.append('the_number_of_unique_incoming_addresses_internal' + time_str)
        write_list.append('the_total_number_of_incoming_transactions_internal' + time_str)
        write_list.append('the_total_number_of_outcoming_transactions_internal' + time_str)
        write_list.append('the_proportion_of_unique_outcoming_address_transactions_internal' + time_str)
        write_list.append('the_proportion_of_unique_incoming_address_transactions_internal' + time_str)
        write_list.append('proportion_of_outcoming_address_transactions_internal' + time_str)
        write_list.append('proportion_of_incoming_address_transactions_internal' + time_str)
        write_list.append('minimum_value_in_Ether_ever_received_internal' + time_str)
        write_list.append('maximum_value_in_Ether_ever_received_internal' + time_str)
        write_list.append('avg_value_in_Ether_ever_received_internal' + time_str)
        write_list.append('minimum_value_in_Ether_ever_sent_internal' + time_str)
        write_list.append('maximum_value_in_Ether_ever_sent_internal' + time_str)
        write_list.append('avg_value_in_Ether_ever_sent_internal' + time_str)
        write_list.append('total_value_in_Ether_ever_received_internal' + time_str)
        write_list.append('total_value_in_Ether_ever_sent_internal' + time_str)
        write_list.append('the_number_of_transactions_per_day_internal' + time_str)
        write_list.append('the_number_of_incoming_transactions_per_day_internal' + time_str)
        write_list.append('the_number_of_outcoming_transactions_per_day_internal' + time_str)
        write_list.append('the_number_of_incoming_transactions_per_hour_internal' + time_str)
        write_list.append('the_number_of_outcoming_transactions_per_hour_internal' + time_str)
        write_list.append('the_number_of_incoming_amounts_per_day_internal' + time_str)
        write_list.append('the_number_of_outcoming_amounts_per_day_internal' + time_str)
        write_list.append('the_total_number_of_amounts_outcoming_plus_incoming_internal' + time_str)
        write_list.append('the_number_of_incoming_amounts_per_hour_internal' + time_str)
        write_list.append('the_number_of_outcoming_amounts_per_hour_internal' + time_str)
        write_list.append('the_number_of_transactions_per_hour_internal' + time_str)
        write_list.append('the_number_of_amounts_per_day_internal' + time_str)
        write_list.append('the_number_of_amounts_per_hour_internal' + time_str)
        write_list.append('reverted_numbers_internal' + time_str)

        write_list.append('average_time_between_incoming_transactions_erc20' + time_str)
        write_list.append('average_time_between_outcoming_transactions_erc20' + time_str)
        write_list.append('time_since_the_first_until_the_last_transaction_erc20' + time_str)
        write_list.append('longest_interval_between_two_transactions_erc20' + time_str)
        write_list.append('shortest_interval_between_two_transactions_erc20' + time_str)
        write_list.append('total_number_of_transactions_erc20' + time_str)
        write_list.append('the_number_of_unique_outcoming_addresses_erc20' + time_str)
        write_list.append('the_number_of_unique_incoming_addresses_erc20' + time_str)
        write_list.append('the_total_number_of_incoming_transactions_erc20' + time_str)
        write_list.append('the_total_number_of_outcoming_transactions_erc20' + time_str)
        write_list.append('the_proportion_of_unique_outcoming_address_transactions_erc20' + time_str)
        write_list.append('the_proportion_of_unique_incoming_address_transactions_erc20' + time_str)
        write_list.append('proportion_of_outcoming_address_transactions_erc20' + time_str)
        write_list.append('proportion_of_incoming_address_transactions_erc20' + time_str)
        write_list.append('minimum_value_in_Ether_ever_received_erc20' + time_str)
        write_list.append('maximum_value_in_Ether_ever_received_erc20' + time_str)
        write_list.append('avg_value_in_Ether_ever_received_erc20' + time_str)
        write_list.append('minimum_value_in_Ether_ever_sent_erc20' + time_str)
        write_list.append('maximum_value_in_Ether_ever_sent_erc20' + time_str)
        write_list.append('avg_value_in_Ether_ever_sent_erc20' + time_str)
        write_list.append('total_value_in_Ether_ever_received_erc20' + time_str)
        write_list.append('total_value_in_Ether_ever_sent_erc20' + time_str)
        write_list.append('the_number_of_transactions_per_day_erc20' + time_str)
        write_list.append('the_number_of_incoming_transactions_per_day_erc20' + time_str)
        write_list.append('the_number_of_outcoming_transactions_per_day_erc20' + time_str)
        write_list.append('the_number_of_incoming_transactions_per_hour_erc20' + time_str)
        write_list.append('the_number_of_outcoming_transactions_per_hour_erc20' + time_str)
        write_list.append('the_number_of_incoming_amounts_per_day_erc20' + time_str)
        write_list.append('the_number_of_outcoming_amounts_per_day_erc20' + time_str)
        write_list.append('the_total_number_of_amounts_outcoming_plus_incoming_erc20' + time_str)
        write_list.append('the_number_of_incoming_amounts_per_hour_erc20' + time_str)
        write_list.append('the_number_of_outcoming_amounts_per_hour_erc20' + time_str)
        write_list.append('the_number_of_transactions_per_hour_erc20' + time_str)
        write_list.append('the_number_of_amounts_per_day_erc20' + time_str)
        write_list.append('the_number_of_amounts_per_hour_erc20' + time_str)

        write_list.append('average_time_between_incoming_transactions_nft' + time_str)
        write_list.append('average_time_between_outcoming_transactions_nft' + time_str)
        write_list.append('time_since_the_first_until_the_last_transaction_nft' + time_str)
        write_list.append('longest_interval_between_two_transactions_nft' + time_str)
        write_list.append('shortest_interval_between_two_transactions_nft' + time_str)
        write_list.append('total_number_of_transactions_nft' + time_str)
        write_list.append('the_number_of_unique_outcoming_addresses_nft' + time_str)
        write_list.append('the_number_of_unique_incoming_addresses_nft' + time_str)
        write_list.append('the_total_number_of_incoming_transactions_nft' + time_str)
        write_list.append('the_total_number_of_outcoming_transactions_nft' + time_str)
        write_list.append('the_proportion_of_unique_outcoming_address_transactions_nft' + time_str)
        write_list.append('the_proportion_of_unique_incoming_address_transactions_nft' + time_str)
        write_list.append('proportion_of_outcoming_address_transactions_nft' + time_str)
        write_list.append('proportion_of_incoming_address_transactions_nft' + time_str)
        write_list.append('minimum_value_in_Ether_ever_received_nft' + time_str)
        write_list.append('maximum_value_in_Ether_ever_received_nft' + time_str)
        write_list.append('avg_value_in_Ether_ever_received_nft' + time_str)
        write_list.append('minimum_value_in_Ether_ever_sent_nft' + time_str)
        write_list.append('maximum_value_in_Ether_ever_sent_nft' + time_str)
        write_list.append('avg_value_in_Ether_ever_sent_nft' + time_str)
        write_list.append('total_value_in_Ether_ever_received_nft' + time_str)
        write_list.append('total_value_in_Ether_ever_sent_nft' + time_str)
        write_list.append('the_number_of_transactions_per_day_nft' + time_str)
        write_list.append('the_number_of_incoming_transactions_per_day_nft' + time_str)
        write_list.append('the_number_of_outcoming_transactions_per_day_nft' + time_str)
        write_list.append('the_number_of_incoming_transactions_per_hour_nft' + time_str)
        write_list.append('the_number_of_outcoming_transactions_per_hour_nft' + time_str)
        write_list.append('the_number_of_incoming_amounts_per_day_nft' + time_str)
        write_list.append('the_number_of_outcoming_amounts_per_day_nft' + time_str)
        write_list.append('the_total_number_of_amounts_outcoming_plus_incoming_nft' + time_str)
        write_list.append('the_number_of_incoming_amounts_per_hour_nft' + time_str)
        write_list.append('the_number_of_outcoming_amounts_per_hour_nft' + time_str)
        write_list.append('the_number_of_transactions_per_hour_nft' + time_str)
        write_list.append('the_number_of_amounts_per_day_nft' + time_str)
        write_list.append('the_number_of_amounts_per_hour_nft' + time_str)

        write_list.append('average_time_between_incoming_transactions_erc1155' + time_str)
        write_list.append('average_time_between_outcoming_transactions_erc1155' + time_str)
        write_list.append('time_since_the_first_until_the_last_transaction_erc1155' + time_str)
        write_list.append('longest_interval_between_two_transactions_erc1155' + time_str)
        write_list.append('shortest_interval_between_two_transactions_erc1155' + time_str)
        write_list.append('total_number_of_transactions_erc1155' + time_str)
        write_list.append('the_number_of_unique_outcoming_addresses_erc1155' + time_str)
        write_list.append('the_number_of_unique_incoming_addresses_erc1155' + time_str)
        write_list.append('the_total_number_of_incoming_transactions_erc1155' + time_str)
        write_list.append('the_total_number_of_outcoming_transactions_erc1155' + time_str)
        write_list.append('the_proportion_of_unique_outcoming_address_transactions_erc1155' + time_str)
        write_list.append('the_proportion_of_unique_incoming_address_transactions_erc1155' + time_str)
        write_list.append('proportion_of_outcoming_address_transactions_erc1155' + time_str)
        write_list.append('proportion_of_incoming_address_transactions_erc1155' + time_str)
        write_list.append('minimum_value_in_Ether_ever_received_erc1155' + time_str)
        write_list.append('maximum_value_in_Ether_ever_received_erc1155' + time_str)
        write_list.append('avg_value_in_Ether_ever_received_erc1155' + time_str)
        write_list.append('minimum_value_in_Ether_ever_sent_erc1155' + time_str)
        write_list.append('maximum_value_in_Ether_ever_sent_erc1155' + time_str)
        write_list.append('avg_value_in_Ether_ever_sent_erc1155' + time_str)
        write_list.append('total_value_in_Ether_ever_received_erc1155' + time_str)
        write_list.append('total_value_in_Ether_ever_sent_erc1155' + time_str)
        write_list.append('the_number_of_transactions_per_day_erc1155' + time_str)
        write_list.append('the_number_of_incoming_transactions_per_day_erc1155' + time_str)
        write_list.append('the_number_of_outcoming_transactions_per_day_erc1155' + time_str)
        write_list.append('the_number_of_incoming_transactions_per_hour_erc1155' + time_str)
        write_list.append('the_number_of_outcoming_transactions_per_hour_erc1155' + time_str)
        write_list.append('the_number_of_incoming_amounts_per_day_erc1155' + time_str)
        write_list.append('the_number_of_outcoming_amounts_per_day_erc1155' + time_str)
        write_list.append('the_total_number_of_amounts_outcoming_plus_incoming_erc1155' + time_str)
        write_list.append('the_number_of_incoming_amounts_per_hour_erc1155' + time_str)
        write_list.append('the_number_of_outcoming_amounts_per_hour_erc1155' + time_str)
        write_list.append('the_number_of_transactions_per_hour_erc1155' + time_str)
        write_list.append('the_number_of_amounts_per_day_erc1155' + time_str)
        write_list.append('the_number_of_amounts_per_hour_erc1155' + time_str)

        write_list.append('average_time_between_incoming_transactions_all' + time_str)
        write_list.append('average_time_between_outcoming_transactions_all' + time_str)
        write_list.append('time_since_the_first_until_the_last_transaction_all' + time_str)
        write_list.append('longest_interval_between_two_transactions_all' + time_str)
        write_list.append('shortest_interval_between_two_transactions_all' + time_str)
        write_list.append('total_number_of_transactions_all' + time_str)
        write_list.append('the_number_of_unique_outcoming_addresses_all' + time_str)
        write_list.append('the_number_of_unique_incoming_addresses_all' + time_str)
        write_list.append('the_total_number_of_incoming_transactions_all' + time_str)
        write_list.append('the_total_number_of_outcoming_transactions_all' + time_str)
        write_list.append('the_proportion_of_unique_outcoming_address_transactions_all' + time_str)
        write_list.append('the_proportion_of_unique_incoming_address_transactions_all' + time_str)
        write_list.append('proportion_of_outcoming_address_transactions_all' + time_str)
        write_list.append('proportion_of_incoming_address_transactions_all' + time_str)
        write_list.append('minimum_value_in_Ether_ever_received_all' + time_str)
        write_list.append('maximum_value_in_Ether_ever_received_all' + time_str)
        write_list.append('avg_value_in_Ether_ever_received_all' + time_str)
        write_list.append('minimum_value_in_Ether_ever_sent_all' + time_str)
        write_list.append('maximum_value_in_Ether_ever_sent_all' + time_str)
        write_list.append('avg_value_in_Ether_ever_sent_all' + time_str)
        write_list.append('total_value_in_Ether_ever_received_all' + time_str)
        write_list.append('total_value_in_Ether_ever_sent_all' + time_str)
        write_list.append('the_number_of_transactions_per_day_all' + time_str)
        write_list.append('the_number_of_incoming_transactions_per_day_all' + time_str)
        write_list.append('the_number_of_outcoming_transactions_per_day_all' + time_str)
        write_list.append('the_number_of_incoming_transactions_per_hour_all' + time_str)
        write_list.append('the_number_of_outcoming_transactions_per_hour_all' + time_str)
        write_list.append('the_number_of_incoming_amounts_per_day_all' + time_str)
        write_list.append('the_number_of_outcoming_amounts_per_day_all' + time_str)
        write_list.append('the_total_number_of_amounts_outcoming_plus_incoming_all' + time_str)
        write_list.append('the_number_of_incoming_amounts_per_hour_all' + time_str)
        write_list.append('the_number_of_outcoming_amounts_per_hour_all' + time_str)
        write_list.append('the_number_of_transactions_per_hour_all' + time_str)
        write_list.append('the_number_of_amounts_per_day_all' + time_str)
        write_list.append('the_number_of_amounts_per_hour_all' + time_str)
        write_list.append('reverted_numbers_all' + time_str)

        write_list.append('the_propotion_of_normal_transactions_of_all' + time_str)
        write_list.append('the_propotion_of_normal_incoming_transactions_of_all' + time_str)
        write_list.append('the_propotion_of_normal_incoming_transactions_of_all_transactions' + time_str)
        write_list.append('the_propotion_of_normal_outcoming_transactions_of_all' + time_str)
        write_list.append('the_propotion_of_normal_outcoming_transactions_of_all_transactions' + time_str)

        write_list.append('the_propotion_of_internal_transactions_of_all' + time_str)
        write_list.append('the_propotion_of_internal_incoming_transactions_of_all' + time_str)
        write_list.append('the_propotion_of_internal_incoming_transactions_of_all_transactions' + time_str)
        write_list.append('the_propotion_of_internal_outcoming_transactions_of_all' + time_str)
        write_list.append('the_propotion_of_internal_outcoming_transactions_of_all_transactions' + time_str)

        write_list.append('the_propotion_of_erc20_transactions_of_all' + time_str)
        write_list.append('the_propotion_of_erc20_incoming_transactions_of_all' + time_str)
        write_list.append('the_propotion_of_erc20_incoming_transactions_of_all_transactions' + time_str)
        write_list.append('the_propotion_of_erc20_outcoming_transactions_of_all' + time_str)
        write_list.append('the_propotion_of_erc20_outcoming_transactions_of_all_transactions' + time_str)

        write_list.append('the_propotion_of_nft_transactions_of_all' + time_str)
        write_list.append('the_propotion_of_nft_incoming_transactions_of_all' + time_str)
        write_list.append('the_propotion_of_nft_incoming_transactions_of_all_transactions' + time_str)
        write_list.append('the_propotion_of_nft_outcoming_transactions_of_all' + time_str)
        write_list.append('the_propotion_of_nft_outcoming_transactions_of_all_transactions' + time_str)

        write_list.append('the_propotion_of_erc1155_transactions_of_all' + time_str)
        write_list.append('the_propotion_of_erc1155_incoming_transactions_of_all' + time_str)
        write_list.append('the_propotion_of_erc1155_incoming_transactions_of_all_transactions' + time_str)
        write_list.append('the_propotion_of_erc1155_outcoming_transactions_of_all' + time_str)
        write_list.append('the_propotion_of_erc1155_outcoming_transactions_of_all_transactions' + time_str)

        write_list.append('the_propotion_of_normal_ether_transfered_of_all' + time_str)
        write_list.append('the_propotion_of_normal_ether_sent_of_all_sent' + time_str)
        write_list.append('the_propotion_of_normal_ether_sent_of_all_touched' + time_str)
        write_list.append('the_propotion_of_normal_ether_received_of_all_sent' + time_str)
        write_list.append('the_propotion_of_normal_ether_received_of_all_touched' + time_str)

        write_list.append('the_propotion_of_internal_ether_transfered_of_all' + time_str)
        write_list.append('the_propotion_of_internal_ether_sent_of_all_sent' + time_str)
        write_list.append('the_propotion_of_internal_ether_sent_of_all_touched' + time_str)
        write_list.append('the_propotion_of_internal_ether_received_of_all_sent' + time_str)
        write_list.append('the_propotion_of_internal_ether_received_of_all_touched' + time_str)

        write_list.append('the_propotion_of_erc20_ether_transfered_of_all' + time_str)
        write_list.append('the_propotion_of_erc20_ether_sent_of_all_sent' + time_str)
        write_list.append('the_propotion_of_erc20_ether_sent_of_all_touched' + time_str)
        write_list.append('the_propotion_of_erc20_ether_received_of_all_sent' + time_str)
        write_list.append('the_propotion_of_erc20_ether_received_of_all_touched' + time_str)
        
        write_list.append('the_propotion_of_nft_ether_transfered_of_all' + time_str)
        write_list.append('the_propotion_of_nft_ether_sent_of_all_sent' + time_str)
        write_list.append('the_propotion_of_nft_ether_sent_of_all_touched' + time_str)
        write_list.append('the_propotion_of_nft_ether_received_of_all_sent' + time_str)
        write_list.append('the_propotion_of_nft_ether_received_of_all_touched' + time_str)

        write_list.append('the_propotion_of_erc1155_ether_transfered_of_all' + time_str)
        write_list.append('the_propotion_of_erc1155_ether_sent_of_all_sent' + time_str)
        write_list.append('the_propotion_of_erc1155_ether_sent_of_all_touched' + time_str)
        write_list.append('the_propotion_of_erc1155_ether_received_of_all_sent' + time_str)
        write_list.append('the_propotion_of_erc1155_ether_received_of_all_touched' + time_str)

        write_list.append('only_incoming_result' + time_str)
        write_list.append('only_outcoming_result' + time_str)
        write_list.append('get_maximum_number_for_same_incoming_address_result' + time_str)
        write_list.append('get_maximum_number_for_same_outcoming_address_result' + time_str)
        write_list.append('get_maximum_number_for_same_touched_address_result' + time_str)

        write_list.append('get_minimum_number_for_same_incoming_address_result' + time_str)
        write_list.append('get_minimum_number_for_same_outcoming_address_result' + time_str)
        write_list.append('get_minimum_number_for_same_touched_address_result' + time_str)
        write_list.append('how_many_address_with_a_single_transaction_for_incoming_result' + time_str)
        write_list.append('how_many_address_with_a_single_transaction_for_outcoming_result' + time_str)

        write_list.append('how_many_address_with_a_single_transaction_for_all_result' + time_str)
        write_list.append('incoming_address_with_a_single_transaction_out_of_all_unique_incoming_addresses_result' + time_str)
        write_list.append('incoming_address_with_a_single_transaction_out_of_all_unique_addresses_result' + time_str)
        write_list.append('outcoming_address_with_a_single_transaction_out_of_all_unique_outcoming_addresses_result' + time_str)
        write_list.append('outcoming_address_with_a_single_transaction_out_of_all_unique_addresses_result' + time_str)

        write_list.append('all_address_with_a_single_transaction_out_of_all_unique_addresses_result' + time_str)
        write_list.append('the_maximum_repeated_Ether_value_in_incoming_amount_result' + time_str)
        write_list.append('the_minimum_repeated_Ether_value_in_incoming_amount_result' + time_str)
        write_list.append('the_maximum_repeated_Ether_value_in_outcoming_amount_result' + time_str)
        write_list.append('the_minimum_repeated_Ether_value_in_outcoming_amount_result' + time_str)

        write_list.append('the_maximum_repeated_Ether_value_in_all_amount_result' + time_str)
        write_list.append('the_minimum_repeated_Ether_value_in_all_amount_result' + time_str)
        write_list.append('the_maximum_repeated_Ether_value_in_incoming_times_result' + time_str)
        write_list.append('the_minimum_repeated_Ether_value_in_incoming_times_result' + time_str)
        write_list.append('the_maximum_repeated_Ether_value_in_outcoming_times_result' + time_str)

        write_list.append('the_minimum_repeated_Ether_value_in_outcoming_times_result' + time_str)
        write_list.append('the_maximum_repeated_Ether_value_in_all_times_result' + time_str)
        write_list.append('the_minimum_repeated_Ether_value_in_all_times_result' + time_str)

        write_list.append('get_the_total_number_of_incoming_transactions_result_all_2' + time_str)
        write_list.append('get_the_total_number_of_outcoming_transactions_result_all_2' + time_str)
        write_list.append('get_the_number_of_unique_outcoming_addresses_result_all_2' + time_str)
        write_list.append('get_the_number_of_unique_incoming_addresses_result_all_2' + time_str) 
        write_list.append('get_total_value_in_Ether_ever_received_result_all_2' + time_str) 
        write_list.append('get_total_value_in_Ether_ever_sent_result_all_2' + time_str) 
        write_list.append('get_the_number_of_incoming_transactions_per_month_result_all_2' + time_str)
        write_list.append('get_the_number_of_outcoming_transactions_per_month_result_all_2' + time_str)
        write_list.append('get_the_number_of_incoming_amounts_per_month_result_all_2' + time_str)
        write_list.append('get_the_number_of_outcoming_amounts_per_month_result_all_2' + time_str)
        write_list.append('get_average_time_between_incoming_transactions_result_all_2' + time_str)
        write_list.append('get_average_time_between_outcoming_transactions_result_all_2' + time_str)
        write_list.append('get_standard_deviation_time_between_incoming_transactions_all_2' + time_str)
        write_list.append('get_standard_deviation_time_between_outcoming_transactions_all_2' + time_str)
        write_list.append('get_the_total_number_of_incoming_transactions_result_all_malicious' + time_str)
        write_list.append('get_the_total_number_of_outcoming_transactions_result_all_malicious' + time_str)
        write_list.append('get_the_number_of_unique_outcoming_addresses_result_all_malicious' + time_str)
        write_list.append('get_the_number_of_unique_incoming_addresses_result_all_malicious' + time_str)
        write_list.append('get_total_value_in_Ether_ever_received_result_all_malicious' + time_str)
        write_list.append('get_total_value_in_Ether_ever_sent_result_all_malicious' + time_str)
        write_list.append('get_fraction_of_incoming_malicious_transactions_to_all_incoming_transactions_result' + time_str)
        write_list.append('get_fraction_of_outcoming_malicious_transactions_to_all_incoming_transactions_result' + time_str)
        write_list.append('get_fraction_of_incoming_malicious_addresses_to_all_address_result' + time_str)
        write_list.append('get_fraction_of_outcoming_malicious_addresses_to_all_addresses_result' + time_str) 
        write_list.append('get_fraction_of_incoming_malicious_amount_to_all_amount_result' + time_str)
        write_list.append('get_fraction_of_outcoming_malicious_amount_to_all_amount_result' + time_str)
        write_list.append('get_average_time_between_incoming_transactions_result_all_malicious' + time_str) 
        write_list.append('get_average_time_between_outcoming_transactions_result_all_malicious' + time_str)
        write_list.append('get_standard_deviation_time_between_incoming_transactions_result_all_malicious' + time_str)
        write_list.append('get_standard_deviation_time_between_outcoming_transactions_result_all_malicious' + time_str)
        write_list.append('get_number_of_months_account_is_active_result' + time_str)
        write_list.append('get_number_of_transactions_associated_with_malicious_result' + time_str)
        write_list.append('get_number_of_transactions_associated_with_non_malicious_result' + time_str)
        write_list.append('get_number_of_self_transactions_result' + time_str)
        write_list.append('get_number_of_other_transactions_result' + time_str)
        write_list.append('get_normal_transactions_with_ether_value_zero_result' + time_str)
        write_list.append('get_maximum_value_in_Ether_ever_transferred_result' + time_str)
        write_list.append('get_minimum_value_in_Ether_ever_transferred_result' + time_str)
        write_list.append('get_total_value_in_Ether_result' + time_str)
        write_list.append('get_number_of_addresses_related_result' + time_str)

    with open(output + "_result.csv", "a") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(write_list)
    csv_reader = get_csv(apikey, csv_address, time_window_list, malicious_list)