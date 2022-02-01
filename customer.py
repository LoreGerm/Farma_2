import json


class Customer:
    __customer_name = ''
    __customer_surname = ''
    __idcard = ''
    __address = None

    def __init__(self):
        pass

    def get_customer_name(self):
        return self.__customer_name

    def get_customer_surname(self):
        return self.__customer_surname

    def get_customer_address(self):
        return self.__address

    def get_idcard(self):
        return self.__idcard

    def set_customer_name(self,customer_name):
        self.__customer_name = customer_name

    def set_customer_surname(self,customer_surname):
        self.__customer_surname = customer_surname

    def set_customer_address(self,customer_address):
        self.__address = customer_address

    def set_customer_idcard(self,idcard):
        self.__idcard = idcard

    def get_json(self):
        addr = {}
        cust = {}

        for c in self.__dict__:
            cust[c] = self.__dict__[c]

        for a in self.__address.__dict__:
            addr[a] = self.__address.__dict__[a]

        cust['_Customer__address'] = addr
        return json.dumps(cust)

    def set_json(self,jsonstr):
        diz = json.loads(jsonstr)
        
        if '_Customer__customer_name' in diz.keys():
            self.__customer_name = diz['_Customer__customer_name']

        if '_Customer__customer_surname' in diz.keys():
            self.__customer_surname = diz['_Customer__customer_surname']

        if '_Customer__idcard' in diz.keys():
            self.__idcard = diz['_Customer__idcard']

        if '_Customer__address' in diz.keys():
            addr = Address()
            self.__address = addr.set_address(diz['_Customer__address'])



class Address:
    __addr_line_1 = ''
    __addr_line_2 = ''
    __addr_line_3 = ''
    __city = ''
    __zip = ''
    __state_province_country = ''
    __country = ''
    __other_addr_details = ''

    def __init__(self):
        pass

    def set_address(self,jsonstr):
        diz = jsonstr
        if '_Address__addr_line_1' in diz.keys():
            self.__addr_line_1 = diz['_Address__addr_line_1']

        if '_Address__addr_line_2' in diz.keys():
            self.__addr_line_2 = diz['_Address__addr_line_2']

        if '_Address__addr_line_3' in diz.keys():
            self.__addr_line_3 = diz['_Address__addr_line_3']

        if '_Address__city' in diz.keys():
            self.__city = diz['_Address__city']
        
        if '_Address__zip' in diz.keys():
            self.__zip = diz['_Address__zip']

        if '_Address__state_province_country' in diz.keys():
            self.__state_province_country = diz['_Address__state_province_country']

        if '_Address__country' in diz.keys():
            self.__country = diz['_Address__country']
            
        if '_Address__other_addr_details' in diz.keys():
            self.__other_addr_details = diz['_Address__other_addr_details']


    def get_addr_line_1(self):
        return self.__addr_line_1

    def get_addr_line_2(self):
        return self.__addr_line_2

    def get_addr_line_3(self):
        return self.__addr_line_3

    def get_city(self):
        return self.__city

    def get_zip(self):
        return self.__zip

    def get_state_country_prov(self):
        return self.__state_province_country

    def get_country(self):
        return self.__country

    def get_other_details(self):
        return self.__other_addr_details

    #setter
    def set_addr_line_1(self,addr_line_1):
        self.__addr_line_1 = addr_line_1

    def set_addr_line_2(self,addr_line_2):
        self.__addr_line_2 = addr_line_2

    def set_addr_line_3(self,addr_line_3):
        self.__addr_line_3 = addr_line_3

    def set_city(self,city):
        self.__city = city

    def set_zip(self,zip):
        self.__zip = zip

    def set_state_country_prov(self,state_province_country):
        self.__state_province_country = state_province_country

    def set_country(self,country):
        self.__country = country

    def set_other_details(self,details):
       self.__other_addr_details = details