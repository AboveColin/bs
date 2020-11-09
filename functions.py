import init as init

def next_page(n, max):
    get_T_info(n)
    init.driver.find_element_by_id(init.E5).click()
    return n-1

def get_T_info(x):
    if x == init.total_pages + 2:
        for x in range(1, init.last_page):
            x = str(x).zfill(2) 
            A_Name = init.driver.find_element_by_id(init.E4_1 + x + init.E4_2).text
            T_name = init.driver.find_element_by_id(init.E4_1 + x + init.E4_3).text

            print(A_Name + ' - ' + T_name)
    else:
        for x in range(1, 11):
            if x < 10:
                x = str(x).zfill(2)
            A_Name = init.driver.find_element_by_id(init.E4_1 + str(x) + init.E4_2).text
            T_name = init.driver.find_element_by_id(init.E4_1 + str(x) + init.E4_3).text

            print(A_Name + ' - ' + T_name)

def print_pages():
    for x in range(2, init.last_page + 2):
        if init.args.list == True:
            next_page(x, init.total_pages)
        else:
            print()
            print('========================')
            print('==========' + str(next_page(x, init.total_pages)) + '/'+str(init.last_page)+'==========')
