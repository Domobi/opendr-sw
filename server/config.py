UPLOAD_FOLDER = '/home/edb/test_html_server/app/uploaded_imgs/img/'
UPLOAD_FOLDER2 = '/home/edb/test_html_server/app/uploaded_imgs/thumb/'

class Config(object):
    DEBUG = False

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_SSL = False
    SECRET_KEY= '\x9ek\xdbS7\xc0k$\xac\x96\x03W\x84\xb7\x1b\xec\xa0\xe0\xe32\\\x06\x9d'
    # change email information as needed
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'theia.api'
    MAIL_PASSWORD = 'medialabcc'
    DEFAULT_MAIL_SENDER = 'theia.api@gmail.com'
    SECURITY_TOKEN_AUTHENTICATION_KEY = 'token'
    WTF_CSRF_ENABLED = False # apparently necessary for token auth
    
    MONGO_DBNAME = 'eye-learning-files'
    MONGODB_SETTINGS = {
    'db': 'eye-learning-files'
    }

    UPLOAD_FOLDER = UPLOAD_FOLDER
    UPLOAD_FOLDER2 = UPLOAD_FOLDER2
