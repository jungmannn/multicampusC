import pymysql as sql


def searchInPlaystore(info):
    db_session   = None
    rows = None # 영향을 받은 로의 수
    try:    
        db_session = sql.connect( host='python-db.c98cjif9str0.ap-northeast-2.rds.amazonaws.com',
                                user='root',
                                password='12341234',
                                db='python_db',
                                charset='utf8',
                                cursorclass=sql.cursors.DictCursor)
        
        with db_session.cursor() as cursor:
            sql_str = '''
                select Rating, App, `Type`, Category, `Content Rating`
                from tbl_playstore
                where Rating >= %s and `Type` = %s and `Category` = %s and `Content Rating` = %s;
            '''
            cursor.execute( sql_str, (info.get('points'), info.get('type'), info.get('category'), info.get('rating')))
            rows = cursor.fetchall()
            
    except Exception as e:
        print( e )
    finally:
        if db_session:
            db_session.close()
            print('디비접속해제성공')
        return rows
def searchInAppstore(info):
    db_session   = None
    rows = None # 영향을 받은 로의 수
    try:    
        db_session = sql.connect( host='python-db.c98cjif9str0.ap-northeast-2.rds.amazonaws.com',
                                user='root',
                                password='12341234',
                                db='python_db',
                                charset='utf8',
                                cursorclass=sql.cursors.DictCursor)
        
        with db_session.cursor() as cursor:
            sql_str = '''
                select track_name, price, user_rating, prime_genre, cont_rating
                from tbl_appstore
                where price <= %s and user_rating >= %s and prime_genre = %s and cont_rating = %s;
            '''
            cursor.execute( sql_str, (info.get('type'), info.get('points'), info.get('category'),info.get('rating')))
            rows = cursor.fetchall()
            
    except Exception as e:
        print( e )
    finally:
        if db_session:
            db_session.close()
            print('디비접속해제성공')
        return rows

# 자료실 데이터 추가
# data = dict()
# data['name']    = '김정현'
# data['email'] = 'task11naver'
# data['phone']   = '01056289304'
# data['message']     = '정말 멋져요'
# if insertBbsData( data ):print('등록성공')
# else:print('등록실패')

# info = dict()
# info['points']    = '4.0'
# info['type'] = 'Free'
# info['category']   = 'BEAUTY'
# info['rating']     = 'Everyone'

# print(searchInPlaystore(info))

# info = dict()
# info['type']    = '0'
# info['points'] = '3.5'
# info['category']   = 'Games'
# info['rating']     = '4+'

# print(searchInAppstore(info))