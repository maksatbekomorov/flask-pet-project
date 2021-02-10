class ListCreator():
    def __init__(self):
        self.lst = [['column_name_0', 'column_type_0']]
        self.col_name = 'column_name_'
        self.col_type = 'column_type_'

    def add_element(self):
        temp1 = [self.col_name, self.col_type]
        temp = []

        for i in temp1:
            temp.append(i+str(len(self.lst)))

        self.lst.append(temp)
        return self.lst

    def del_element(self):
        if len(self.lst) != 1:
            self.lst.pop()
            return self.lst
        else:
            return self.lst


mass = ListCreator()
