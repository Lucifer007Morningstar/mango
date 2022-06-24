# import configparser
#
# config=configparser.ConfigParser()
# config.read(".\\configurations\\config.ini")
#
# class ConfigReader():
#     @staticmethod
#     def GetAppliactionURL():
#         url=config.get('common info','baseurl')
#         return url
#     @staticmethod
#     def GetUsername():
#         username=config.get('common info','username')
#         return username
#     @staticmethod
#     def GetPassword():
#         password=config.get('common info','password')
#         return password
#
#

import configparser

config = configparser.ConfigParser()
config.read(".\\Configurations\\config.ini")


class ConfigReader():
    @staticmethod
    def GetApplicationURL():
        url = config.get('common info','baseurl')
        return url

    @staticmethod
    def GetUsername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def GetPassword():
        password = config.get('common info', 'password')
        return password
