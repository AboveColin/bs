import init as init
if init.args.sql:
    import sql.sql as SQL

def next_page(n, max):
    get_T_info(n)
    init.driver.find_element_by_id(init.E5).click()
    return n-1

def get_T_info(x):
    if x == init.last_page + 1:
        for x in range(1, init.total_pages_rest+1):
            x = str(x).zfill(2) 
            A_Name = init.driver.find_element_by_id(init.E4_1 + x + init.E4_2).text
            T_name = init.driver.find_element_by_id(init.E4_1 + x + init.E4_3).text

            if init.args.save:
                init.f.write(A_Name + ' - ' + T_name + '\n')
                print(A_Name + ' - ' + T_name)
            else:
                print(A_Name + ' - ' + T_name)
            
            if init.args.sql:
                save_data_sql(A_Name, T_name)

    else:
        for x in range(1, 11):
            if x < 10:
                x = str(x).zfill(2)
            A_Name = init.driver.find_element_by_id(init.E4_1 + str(x) + init.E4_2).text
            T_name = init.driver.find_element_by_id(init.E4_1 + str(x) + init.E4_3).text

            if init.args.save:
                init.f.write(A_Name + ' - ' + T_name + '\n')
                print(A_Name + ' - ' + T_name)
            else:
                print(A_Name + ' - ' + T_name)

            if init.args.sql:
                save_data_sql(A_Name, T_name)

def print_pages():
    for x in range(2, init.last_page + 2):
        if init.args.list:
            next_page(x, init.total_pages)
        else:
            print()
            print('========================')
            print('==========' + str(next_page(x, init.total_pages)) + '/'+str(init.last_page)+'==========')

if init.args.sql:
    def save_data_sql(A_name, T_name):
        A_name = A_name.replace("'", "").replace('"', "").split('; ')
        T_name = T_name.replace("'", "").replace('"', "")
        SQL.insert_to_db(T_name, A_name)

if init.args.discord_webhook:
    def discord_notification(Title, Artist_Array):
        url = init.Webhook_URL

        data = {}
        
        data["content"] = ""
        data["username"] = init.name

        
        data["embeds"] = []
        embed = {}
        
        embed["description"] = str(Title)
        embed["title"] = str(Artist_Array[0]) + " - " + str(Title)
        data["embeds"].append(embed)

        result = init.requests.post(url, data=init.json.dumps(data), headers={"Content-Type": "application/json"})

        try:
            result.raise_for_status()
        except init.requests.exceptions.HTTPError as err:
            print(err)
 
