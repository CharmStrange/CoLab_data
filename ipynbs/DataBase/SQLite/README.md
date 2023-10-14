# Python & Sqlite3 
파이썬으로 SQLite3를 사용하기 위한 설명서, SQLite3는 가벼운 로컬 환경에서 사용하기 좋다.

> ### [File](PySqlite3.ipynb)

> ```Python
> import sqlite3
> ```

> `sqlite3.connect()` : 이 메소드는 데이터베이스 파일 이름을 인수로 받아 연결을 설정하고, 연결 객체를 반환한다.
> ```python
> conn = sqlite3.connect('mydatabase.db')
> ```

> `conn.cursor()` : 연결이 설정된 데이터베이스의 SQL 쿼리를 실행하고 결과를 처리하는 데 사용하는 커서를 생성한다.
> ```Python
> cursor = conn.cursor()
> ```

> `cursor.execute()` : 쿼리 문자열을 인수로 받아 데이터베이스에서 SQL 쿼리를 실행한다.
> ```Python
> cursor.execute("... 쿼리문 ...")
> ```

> `cursor.executemany()` : 여러 개의 SQL 쿼리를 한 번에 실행하는 메소드로, 주로 INSERT 작업과 같이 여러 레코드를 동시에 삽입할 때 사용한다.
> ```Python
> data = [('JohnDoe', 'johndoe@example.com'), ('JaneSmith', 'janesmith@example.com')]
> cursor.executemany("INSERT INTO users (username, email) VALUES (?, ?)", data)
> ```

> `conn.commit()` : 데이터베이스에 대한 변경 사항을 확정한다. (데이터베이스에 대한 모든 변경 작업 후에 호출)
> ```Python
> conn.commit()
> ```

> `cursor.fetchall()` : SQL 쿼리의 결과로 반환된 모든 행의 결과 집합을 리스트로 얻을 수 있게 하는 메소드.
> ```Python
> cursor.execute("SELECT * FROM users")
> rows = cursor.fetchall()
> for row in rows:
>    print(row)
> ```

> `cursor.fetchone()` : SQL 쿼리의 결과로 반환된 첫 번째 행을 가져오는데, 여러 번 실행하면 각 호출에 가져온 행의 다음 행을 연속하여 가져온다.
> ```Python
> cursor.execute("SELECT * FROM users")
> first_row = cursor.fetchone()
> print(first_row)
> ```

> `cursor.fetchmany()` : SQL 쿼리의 결과로 반환된 행 중 일부를 가져오는 함수로, 정수 인자를 주어 : fetchmany(n) 최대 n개의 행을 가져온다.
> ```Python
> cursor.execute("SELECT * FROM users")
> some_rows = cursor.fetchmany(2)  # 최대 2개의 행을 가져옴
> ```

> `cursor.close()` : 커서와 연결을 끊는다(작업 종료를 선언).
> 
> `conn.close()` : 데이터베이스와 연결을 끊는다(작업 완전 종료 선언).
