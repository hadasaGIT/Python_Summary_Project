import os as os

"""This class is used logically to rename local files
prams: file name you want to rename,The name you want to change to,Routing to a directory where you want to rename files
this class include func:
constructor to first initialization NameForChange ,NewName and path,
func rename -the function that renames the files
"""


class logic:
    """init the object
    :param self: object Logic
    :type self: object
    :param name1: file name you want to rename
    :type name1: string
    :param name2: The name you want to change to
    :type name2: string
    :param path: Routing to a directory where you want to rename files
    :type path: string
    :return: no
    :rtype: no
    """

    def __init__(self, name1, name2, path):
        self._NameForChange = name1
        self._NewName = name2
        self.path = str(path)
        # print(path)
        # print(self.path)

    """function that renames the files
    :param self: object Logic
    :type self: object
    :return: count -number of files modified
    :rtype: int
    """

    def rename(self):
        # init count
        count = 0
        # If the routing is empty you will use the current (of the project routing)
        if self.path != '':
            cc = os.listdir(self.path)
            os.chdir(path=self.path)
            print(os.getcwd())
        else:
            cc = os.listdir()
        print(os.listdir)
        # Loop on all files in the directory
        for i in cc:
            # For each file renamed by the replace function that replaces a specified phrase with another specified phrase.
            if i != i.replace(self._NameForChange, self._NewName):
                count += 1
                os.rename(i, i.replace(self._NameForChange, self._NewName))
        return count
