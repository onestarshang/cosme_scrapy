# -*- coding: utf8 -*-

from datetime import datetime, timedelta, date
import MySQLdb as mdb

from settings import HOST, DB, USER, PWD


DATE_RAW_FORMAT = '%Y/%m/%d'
DATE_DISPLAY_FORMAT = '%Y-%m-%d'


def day2str(day, format=DATE_RAW_FORMAT):
        return day.strftime(format)


def str2day(day, format=DATE_RAW_FORMAT):
    return datetime.strptime(day, format)


#-----mysql connect-----
def connectdb():
    conn =  mdb.connect(HOST, USER, PWD, DB, charset='utf8')
    curs = conn.cursor()
    return curs , conn


def disconnectdb(_curs,_conn):
    try :
        _curs.close()
    except BaseException , e :
        pass

    try :
        _conn.close()
    except BaseException , e :
        pass


def rundb(sql, vals=[] , db_conf={}, result=True):
    try :
        curs , conn = connectdb()
        curs.execute(sql , vals)
        conn.commit()
        r = None
        if result :
            r = curs.fetchall()
        return r
    except BaseException , e :
        print e
        print sql
        r = None
    finally:
        disconnectdb(curs, conn)
        return r
