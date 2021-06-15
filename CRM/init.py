from crm.data import New, Old
from getting_input import customer, product, username, passwd


class Run:

    def login(self):
        while True:
            u_name = "user"
            pswd = "user123"
            u = username()
            pwd = passwd()
            if u_name == u and pswd == pwd:
                self.b = customer()
                if self.b == '1':
                    self.p = product()
                    if self.p:
                        obj = New()
                        obj.place_order()
                        break
                elif self.b == '2':
                    ob = Old()
                    ob.validation()
                    break
            else:
                print('invalid username or password')
                continue



