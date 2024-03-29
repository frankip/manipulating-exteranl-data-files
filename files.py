import json
import pickle
import sqlite3

def database_connection():
    """ A database connetion """
    with sqlite3.connect('data.db') as sql_conn:
        return sql_conn


def fetch_data_from_sql():
    """fetching all data from the sql db"""
    connection = database_connection()
    cursor = connection.cursor()

    # query ALL DATA FROM mockdata DB;"
    query = "select * from MOCK_DATA"
    dat = cursor.execute(query).fetchall()
    return dat


def load_data_from_csv_file():
    """ load data from a csv file"""
    with open('DATA.csv', 'r') as files: #load and open file returns file object
        # use the readline methods to read the file object and assign it file_contents
        file_contents = files.readlines()[1:] # readlines returns the whole line
        for contents in file_contents: # loop through the  rows in the file contents 

            # print(row) #print each row from the file contents

            # sample return
            # 1,http://dummyimage.com/121x100.png/cc0000/ffffff,Iago,Itschakov,iitschakov0@soup.io,Marketing,14

            row = contents.split(',')
            new_contact = Employee(row[0], row[1], row[2],row[3], row[4], row[5], row[6])
            new_contact.save()


def write_to_csv_file(payload):
    """ writing data to the csv file """
    with open('DATA.csv', 'a') as files: # note that mode is "a" for append to file
        # sample csv input data
        #payload  = "1,http://dummyimage.com/121x100.png/cc0000/ffffff,Iago,Itschakov,iitschakov0@soup.io,Marketing,14"
        files.write(payload) # append the new data to the bottom of the csv file
        files.write('\n') # add a new line after appending data

        Employee.fetch_data()


# def delete_row_from_file(emp):
#     with open('DATA.csv', 'ar') as files:
#         print(emp.get_full_name())
#         data_content = files.readlines()[1:]
#         # for i in range(len(data_content)):
#         print(data_content)


class Employee():
    employees_list = list()
    
    def __init__(self, id, image, first_name, last_name, email, department,leave_days):
        self.id = id
        self.image= image
        self.first_name = first_name
        self.last_name = last_name
        self.email =  email
        self.department = department
        self.leave_name = leave_days

        def __str__(self):
            return self.first_name

    def get_full_name(self):
        """ return the full names """
        return f"{self.first_name}  {self.last_name}"

    def save(self):
        """
            the method saves the contact object into the contact list
        """
        self.employees_list.append(self)

    def add_new(self,employee):
        id = len(self.employees_list)+1
        employee.id = str(id)
        pylod = ",".join(employee.__dict__.values())
        return write_to_csv_file(pylod)
    
    @classmethod   
    def update(cls, value):
        """
            the method saves the contact object into the contact list
        """
        for contact in range(len(cls.employees_list)):
            if cls.employees_list[contact].email == value:
                print("s")
                cls.employees_list[contact].email = "jleallu@state.tx"
                return cls.employees_list[contact].get_full_name()

    @staticmethod
    def fetch_data_from_csv():
        '''
        method that returns the contact list
        '''
        return [cont.get_full_name() for cont in Employee.employees_list]

    @staticmethod
    def fetch_data_from_sql():
        '''
        method that returns the contact list
        '''
        return fetch_data_from_sql()

    @classmethod
    def check_existing(cls,email):
        '''
        Method that checks if a contact exists from the contact list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for contact in cls.contact_list:
            if contact.email == email:
                return contact.get_full_name()

        return False

    @classmethod
    def find_by_email(cls,email):
        '''
        Method that takes in a number and returns a contact that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            Contact of person that matches the number.
        '''
        emp = cls.check_existing(email)
        if emp:
            return emp
        return False


    @classmethod
    def delete_employee(cls,email):

        '''
        delete_contact method deletes a saved employee from employee list
        '''
        for employee in cls.employees_list:
            if employee.email == email:
                print("--->", employee.get_full_name())
                # delete_row_from_file(employee)
                Employee.employees_list.remove(employee)
                return cls.fetch_data()

        return False

if __name__=='__main__':
    load_data_from_csv_file()
    new_emp = Employee('2','http://dummyimage.com/208x100.png/cc0000/ffffff','Rori','Kingerby','rkingerby1@feedburner.com','Training','13')
    # new_emp.add_new(new_emp)
    # print( Employee.update('rkingerby1@feedburner.com'))
    # Employee.update_db()
    # print(Employee.delete_employee("rkingerby1@feedburner.com"))
    print(Employee.fetch_data())