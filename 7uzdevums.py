"""
Uzrakstiet programmu Python, lai aprēķinātu 
četru ievadīto skaitļu summu.
Ja ievadītās vērtības ir vienādas, atgrieziet summu,
divkāršojot un paņemot tās absolūto vērtību.
"""
from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print(delta.days)