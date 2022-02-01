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
        
        if '__customer_name' in diz.keys():
            self.__customer_name = diz['__customer_name']

        if '__customer_surname' in diz.keys():
            self.__customer_surname = diz['__customer_surname']

        if '__idcard' in diz.keys():
            self.__idcard = diz['__idcard']

        if '__address' in diz.keys():
            addr = Address()
            self.__address = addr.set_json(diz['_Customer__address'])



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

    def set_json(self,jsonstr):
        diz = json.loads(jsonstr)
        if '__addr_line_1' in diz.keys():
            self.__addr_line_1 = diz['__addr_line_1']

        if '__addr_line_2' in diz.keys():
            self.__addr_line_2 = diz['__addr_line_2']

        if '__addr_line_3' in diz.keys():
            self.__addr_line_3 = diz['__addr_line_3']

        if '__city' in diz.keys():
            self.__city = diz['__city']
        
        if '__zip' in diz.keys():
            self.__zip = diz['__zip']

        if '__state_province_country' in diz.keys():
            self.__state_province_country = diz['__state_province_country']

        if '__country' in diz.keys():
            self.__country = diz['__country']
            
        if '__other_addr_details' in diz.keys():
            self.__other_addr_details = diz['__other_addr_details']


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