from Logic import logic
from frontend import frontend

"""This class is main
prams: no
this class include func:
constructor :empty
func run -the function that run app
"""


class main:
    """init the main
    :param self: object Main
    :type self: object
    :return: no
    :rtype: no
    """

    def __init__(self):
        pass

    """init the object
    :param:no!
    :return: no
    :rtype: no
    """

    @staticmethod
    def run():
        # run the object frontend
        c = frontend()
        # loop for run the object logic on terminal
        while True:
            name1 = input("Tap the name to change")
            name2 = input("enter new name")
            path = input("enter the path, for current routing, press enter")
            logicFromMain = logic(name1, name2, path)
            logicFromMain.rename()


# run main
if __name__ == '__main__':
    main = main()
    main.run()
