class DbPropertyUtil:
    @staticmethod
    def getConnectionString():
        server = r'LAPTOP-VHF8SO2V'
        database = 'petpals'  

        return (
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={server};'
            f'DATABASE={database};'
            f'Trusted_Connection=yes;'      
        )


