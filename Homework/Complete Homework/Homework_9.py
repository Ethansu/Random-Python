class Employee():
    def __init__ (self, fname = "John", mname = "No middle name", lname = "Doe", annual_salary = 1000000, age = 25, company = 'Microsoft', u = 'Massachusetts Institute of Technology'):
        self.fname = fname
        self.mname = mname
        self.lname = lname
        self.annual_salary = annual_salary
        self.age = age
        self.company = company
        self.u = u        

    
    def give_raise(self, giveraise = 5000):
        annualsalary = int (giveraise) + int (self.annual_salary)
#        print ("Frist Name: " + self.fname)
#        print ("Middle Name: " + self.mname)
#        print ("Last name: " + self.lname)
#        print ("Annual Salary: $" + str (annualsalary))
#        print ("Age: " + str (self.age))
#        print ("Company: " + self.company)
#        print ("Universty: " + str (self.u))
        return annualsalary
    
    
    
 
employee = Employee ()
employee.give_raise ()