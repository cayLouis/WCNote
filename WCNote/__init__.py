import pymysql
import threading
from message.wechatpy import get_token, create_menu
pymysql.install_as_MySQLdb()
bg_thread = threading.Thread(target=get_token)
bg_thread.start()
create_menu()
