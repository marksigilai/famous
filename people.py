#class for each famous person
class Person:
    #each famous person will have a name, birthdate and information
    def __init__(self, name, birthdate, information):
        self.name = name
        self.birthdate = birthdate
        self.information = information
        self.index = 0
    #getters and setters for all the attributes for each famous person
    def get_birthdate(self):
        return self.birthdate

    def get_name(self):
        return self.name

    def get_information(self):
        return self.information

    def set_birthdate(self, birthdate):
        self.birthdate = birthdate

    def set_name(self, name):
        self.name = name

    def set_index(self, index):
        self.index = index

    def get_index(self):
        return self.index

    def set_information(self, information):
        self.information = information
    #tosrint method that will be used to print to html
    def to_string(self):
        return str(self.get_name()) + ' born in ' + str(self.get_birthdate()) + ' is an ' + str(self.get_information()) + ' with ' + str(self.get_index()) +' all-time wikipedia views'




