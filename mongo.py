from pymongo import MongoClient
import certifi
from pprint import pprint

"""This class is used logically to rename files from mongoDB
prams: file name you want to rename,The name you want to change to,the link to mongoDB
this class include func:
constructor to first initialization NameForChange ,NewName and db
func rename -the function that renames the files
"""


class mongoLogic:
    """init the object
    :param self: object mongoLogic
    :type self: object
    :param name1: file full name you want to rename
    :type name1: string
    :param name2: The full name you want to change to
    :type name2: string
    :param link: Link to a particular database
    :type link: string
    :return: no
    :rtype: no
    """

    def __init__(self, name1, name2, link):
        # CONNECT TO DB
        ca = certifi.where()
        # If the link is empty you will use the myDB (of the project routing)
        if link:
            link_to_DB = link
        else:
            link_to_DB = 'mongodb+srv://hadasa:-cfiChT-wY8pxnc@clusterhadasaomesi.m4era.mongodb.net' \
                         '/ClusterHadasaOmesi?retryWrites=true&w=majority '
        client = MongoClient(link_to_DB, tlsCAFile=ca)
        # connect to projectPython collection
        self.db = client.projectPython
        # init the params class
        self._NameForChange = name1
        self._NewName = name2

    """function that renames the files from DB
    :param self: object Logic
    :type self: object
    :return: Answer whether the change was successful or not
    :rtype: string
    """

    def rename(self):
        try:
            # pprint(self.db.file.find())
            oldName = {"name": self._NameForChange}
            newValues = {"$set": {"name": self._NewName}}
            # Rename and update the full file names in the database
            x = self.db.file.update_many(oldName, newValues)
            return "Succeeded!"
        # If an error occurred by passing the error to the function reader
        except Exception as e:
            return e
