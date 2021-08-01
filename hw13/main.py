from pymongo import MongoClient

import company_data

client = MongoClient('localhost', 27017)
print(client.list_database_names())
db = client["product"]
print(client.list_database_names())
product_list = db.product_list
markup_list = db.markup_list
commission_list = db.commission_list
user_list = db.user_list
x = product_list.find_one({"type": '1'})
print(x)


# product_list_id = product_list.insert_many(company_data.product_list)
# markup_list_id = markup_list.insert_many(company_data.markup_list)
# commission_list_id = commission_list.insert_many(company_data.commission_list)
# user_list_id = user_list.insert_many(company_data.user_list)

def calculate_markup_percent(type, count):
    product = product_list.find_one({"type": type})
    markup = markup_list.find_one({"product_type": type})
    if count == 1:
        final_markup = markup['upper_cost']
    elif count >= markup['lower_count']:
        final_markup = markup['lower_cost']
    else:
        final_markup = count * ((markup['upper_cost'] - markup['lower_cost']) / markup['lower_count']) + markup[
            'lower_cost']
    return final_markup


def calculate_product_price(product_type, count, userid=0):
    product = product_list.find_one({'type': product_type})
    print(product['commission_groups'])
    user = commission_list.find_one({'users': userid})
    print(user['group_name'])
    if userid == 0:
        pass
    else:
        # commission = commission_list.findone()
        pass


print(calculate_markup_percent('1', 5))
print(calculate_product_price('1', 2, 1001))
