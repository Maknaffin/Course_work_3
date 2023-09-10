from utils import load_list_operations, final_information, list_operation, sort_list_executed, \
    sort_list_date, last_five_operations


all_list_operations = load_list_operations('../operations.json')
operation_list = list_operation(all_list_operations)
list_executed = sort_list_executed(operation_list)
list_date = sort_list_date(list_executed)
five_operations = last_five_operations(list_date)
list_final_information = final_information(five_operations)

for operation in list_final_information:
    print(operation)