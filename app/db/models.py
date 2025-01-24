from sqlalchemy import Column, Integer, String, select
from db.database import Base, async_session_maker, engine

class Users(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, nullable=False)
    api_token = Column(String, nullable=False)
    
async def init_db():
    '''
    Инициализирует базу данных, создавая таблицы на основе моделей SQLAlchemy.
    '''
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        
async def find_by_telegram_id(user_id: int):
    '''
    Ищет пользователя в базе данных по его Telegram ID.
    '''
    async with async_session_maker() as session:
        query = select(Users).filter_by(telegram_id = user_id)
        result = await session.execute(query)
        return result.scalar_one_or_none()
    
async def find_by_api_token(user_id: str):
    '''
    Ищет пользователя в базе данных по его API токену.
    '''
    async with async_session_maker() as session:
        query = select(Users).filter_by(api_token = user_id)
        result = await session.execute(query)
        return result.scalar_one_or_none()
# async def init_db():
#     Base.metadata.create_all(bind=engine)