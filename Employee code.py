#inmporting the Faker Library module

!pip install Faker

from faker import Faker
import pandas as pd

fake=Faker(locale="en_IN")

def create_employee(num_employees):
  employee_list=[]

  for i in range(1,num_employees):
    employee={}
    employee['first name ']=fake.first_name()
    employee['last name ']=fake.last_name()
    employee['job title ']=fake.job()
    employee['department ']=fake.random_element(elements=['Sales','Marketing','Engineering','Human Resources'])
    employee['salary']=fake.random_int(min=30000,max=120000)
    employee['date of birth ']=fake.date_of_birth(minimum_age=18,maximum_age=46)
    employee['sex']=fake.random_element(elements=['Male','Female'])
    employee['hire date ']=fake.date_between(start_date='-5y',end_date='today')
    employee['company']=fake.company()
    employee['email']=fake.email()
    employee['phone']=fake.phone_number()
    employee['address']=fake.address()
    employee['city']=fake.city()
    employee['state']=fake.state()


    employee_list.append(employee)

  print(f"created {num_employees} employees")
  return employee_list


#Enter the number of required empolyee count
num_employees = int(input("Enter the number of employees: "))
employee_list = create_employee(num_employees)


#convertng the dataframe into the excel data
df=pd.DataFrame(employee_list)
df.to_excel('employees.xlsx',index=False)
print(df)

#Downloading the employee dattset using the colob 
from google.colab import files
files.download('employees.xlsx')


Note: The download code can be implement in only the colob repository for the download.
