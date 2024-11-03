from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.exc import IntegrityError
from contextlib import contextmanager

from Utils import print_formated_text


class Database:
    db_url = "mysql+pymysql://root@localhost/game_center"
    def __init__(self):
        self.engine = create_engine(Database.db_url)
        self.session = scoped_session(session_factory=sessionmaker(bind=self.engine))

    @contextmanager
    def get_session(self):
        session = self.session()
        try:
            yield session
            session.commit()
        except IntegrityError:
            print_formated_text(messages=f"This Username is already taken!!")
        except Exception as e:
            session.rollback()
            print(f"Err: {e}")
        finally:
            session.close()