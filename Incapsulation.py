class Person:
    def __init__(self, name, job, company, salary, bankAccNum):
        self.name = name
        self.job = job
        self.company = company
        self._salary = salary
        self.__bankAccNum = bankAccNum

    def print_name(self):
        print(self.name)

    def print_job(self):
        print(self.job)

    def print_company(self):
        print(self.company)
    
    def print__salary(self):
        print(self._salary)

    def print_secret(self):
        print(self.__bankAccNum)

    def __backNum(self):
        print('pyk')
