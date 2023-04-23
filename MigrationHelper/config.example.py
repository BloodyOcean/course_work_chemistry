
CONFIG = {
    'connectionStrings': {
        'sourceConnection': 'mssql+pyodbc://<server>/<db>?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server',
        'destinationConnection': 'mysql+pymysql://<user>:<pass>@<host>:<port>/<db>'
    }
}
