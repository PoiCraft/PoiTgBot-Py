from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

BOT_TOKEN = ''
REQUEST_KWARGS = {
    # "USERNAME:PASSWORD@" is optional, if you need authentication:
    'proxy_url': 'http://127.0.0.1:7890/',
}
DB_HOST = '1.1.1.1'
DB_USER = 'potbot'
DB_PASS = 'wdnmdcnmlgb'
DB_NAME = 'cao'

engine = create_engine(
    'mysql+pymysql://%s:%s@%s/%s' % (DB_USER, DB_PASS, DB_HOST, DB_NAME), echo=True)

SESSION = sessionmaker(bind=engine)
