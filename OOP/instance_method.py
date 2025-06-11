class Company:
    company_name = "BD Soldiers"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def display(self):
        print(f"Company Name: {self.company_name} \n Employee Name: {self.name} \n Salary: {self.salary}")

    @classmethod
    def change_company_name(cls, name):
        cls.company_name = name


employee1 = Company("John Doe", 50000)
employee1.display()
#employee1.change_company_name("Tech Innovators")
Company.change_company_name("Tech Innovators")
employee1.display()