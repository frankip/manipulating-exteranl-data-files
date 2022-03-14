import json
import pickle

def load_data_from_csv_file():
    # import file
    # with open('MOCK_DATA.json', 'r') as files:

    # create a generator expressions
    contents = (row for row in open('MOCK_DATA.csv', 'r'))
    # print(contents)

    # iterate through the generator to get each line
    contents_list = (lines.rstrip().split(',') for lines in contents)
    cols= next(contents_list)
    # print("content list", list(contents_list)[0])

    company_dicts = (dict(zip(cols, data)) for data in contents_list)
   

    # while True:

        # yield company_dicts
        # print("----------------------------------->")
        # 
        # read through the contents
        # data_content = files.readlines()

        # # iterate thtough the content
        # for emp in data_content:
        #     yield emp
        # #     # print(f'{"emp"}----> {json.loads(emp)}')
        # #     print('emp is ', json.dumps(emp))


        # print("the data is ", next(company_dicts))
    return company_dicts
        

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

    @classmethod
    def fetch_data(self):
        data = load_data_from_csv_file()
        for row in data:
            Employee.employees_list.append(row)

        print(self.employees_list[0])
        return self.employees_list




if __name__=='__main__':
    Employee.fetch_data()