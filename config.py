import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "OlTj3C_63Vqc_M5E-_FpS3l_BDLNFDRUh1"

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'udacitystoragesk'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or '/hHNcgGZpxx3WHJpscSa2GBECOA6eN3bgWV5RprwaqFuD3jBjiS9SFNTlRr2PmuXRgeE1zmxfvErzk9ehIuh6g=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'udacitycontainersk'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'udacity-server-sk.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'udacity_db_sk'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'udacity_admin_sk'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'UdaAdm@1234'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = "OlTj3C_63Vqc_M5E-_FpS3l_BDLNFDRUh1"
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    AUTHORITY = "https://login.microsoftonline.com/6548a394-f479-40e4-85f0-8c725e1a1ae1"  # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    CLIENT_ID = "f7a4a3b9-e369-4698-9e50-a40c901f5367"

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session
