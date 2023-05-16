from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column,Integer,String
import pymysql
pymysql.install_as_MySQLdb()

con=create_engine("mysql://root@localhost/orm" , echo=True)
session=sessionmaker(bind=con)
sess1=session()

Base=declarative_base()
  
class Movie(Base):
    __tablename__='movies'

    m_id=Column(Integer,primary_key=True)
    title=Column(String(60),nullable=False)
    release_yr=Column(Integer,nullable=False)
    rating=Column(Integer,nullable=False)

    def __repr__(self):
        return f"<movie name={self.title} release year={self.release_yr} and rating={self.rating} >"

# new=Movie(m_id=1,title="The Godfather",release_yr=1972,rating=9)
# # print(new)
# sess1.add(new)
# sess1.commit()


Base.metadata.create_all(con)    
