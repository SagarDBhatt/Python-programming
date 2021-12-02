from datetime import date


def letterTemp(name, date):
    letter = ''' Dear ''' + name + '''

                            You are selected!

                            ''' + date + '''
    '''
    print(letter)


if __name__ == "__main__":
    name = input("Enter Name = ")
    dateStr = date.today().strftime("%m/%d/%Y")
    letterTemp(name, dateStr)
