import configparser

######create an object of RawConfigparser()######
config = configparser.RawConfigParser()

##### Access/Read the config.ini file  #####
config.read("C:/Users/kruthi.p/PycharmProjects/EOTS_Automation_2021/Configurations/config.ini")

##### Fetch the data from config.ini#######

class ReadConfig:

##### Extract the Value of EOTS URL and store in url variable #####
    @staticmethod
    def getApplicationURL():
        url = config.get('common info','EOTS_URL')
        return url

##### Extract the Value of SISA Manager email ID and store in sisa_manager variable #####
    @staticmethod
    def sisaManager():
        sisa_manager = config.get('common info','USERNAME_SISAMANAGER')
        return sisa_manager


##### Extract the Value of Login password  and store in password variable #####
    @staticmethod
    def password():
        password = config.get('common info','PASSWORD')
        return password