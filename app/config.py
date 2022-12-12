from urllib.parse import quote

database_name = 'clinicdb'
database_password = 'Admin@123'

SECRET_KEY = "cdc03376a9f235f53369da5a163d347ca3bd5d9755cf1df6924b68eace7359e3"
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:%s@localhost/%s?charset=utf8mb4' % (quote(database_password),database_name)
SQLALCHEMY_TRACK_MODIFICATIONS = True
PRESCRIPTION = 'prescription'

