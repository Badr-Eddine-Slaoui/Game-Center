from sqlalchemy import Column, Integer, Float, String, Boolean
from  sqlalchemy.orm import  declarative_base
from bcrypt import gensalt, hashpw, checkpw

from Utils import print_formated_text, number_validation

Base = declarative_base()

class Player(Base):

    __tablename__ = "players"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(3), unique=True, nullable=False)
    password = Column(String, nullable=False)
    balance = Column(Float, default=0.0,)
    total_score = Column(Integer, default=0)
    is_logged = Column(Boolean, default=False)

    @staticmethod
    def login(session,username: str, password: str):
        player = session.query(Player).filter_by(username = username).first()
        if player:
            if checkpw(password=password.encode('utf-8'),hashed_password=player.password.encode('utf-8')):
                player.is_logged = True
                session.commit()
                session.refresh(player)
                return  player
        print_formated_text(messages="Username or password incorrect!!",option="capital")


    @staticmethod
    def register(session,username: str, password: str):
            salt = gensalt()
            hashed_password = hashpw(password=password.encode("utf-8"),salt=salt)
            new_player = Player(username=username,password=hashed_password)
            session.add(new_player)
            session.commit()
            session.refresh(new_player)
            return Player.login(session=session, username=username, password=password)


    @staticmethod
    def recharge_balance(session,player,prompt: str):
        player.balance = number_validation(prompt=prompt,min_val=5,max_val=1000000000)
        session.commit()
        session.refresh(player)
        return player


    @staticmethod
    def check_balance(session,player):
        balance = player.balance
        if balance < 5:
            prompt = f"Your balance run out you can't play{f' you only have {balance}$' if balance > 0 else ''}! Please recharge your balance (Between 5$ and 1B$): "
            player.recharge_balance(session=session,player=player,prompt=prompt)
