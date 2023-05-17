# Movie-Data | SqlAlchemy-ORM-Python

## ORM
SQLAlchemy is famous for its object-relational mapper (ORM),where classes can be mapped to the database, 
thereby allowing the object model and database schema to develop in a cleanly decoupled way from the beginning.

### Documentation : https://docs.sqlalchemy.org/en/20/orm/
## SHOW DATA :
print("-----------ALL MOVIES NAME-----------\n")
mv=select(Movie)           # show all movieset

for i in sess1.scalars(mv):
    print(i.title,i.release_yr,i.rating,"/10")
print("\n")
print("+" *40)    

mv=select(Movie).where(Movie.title.in_(["The Godfather", "Psycho"])) #using where cluse  
for t in sess1.scalars(mv):
    print(t)
print("\n")
print("+" *40)   

##OUTPUT :
![image](https://github.com/RinaProg/SqlAlchemy-ORM-Python/assets/122221586/0e2cef5f-1122-4147-bcd2-e456f53bd79b)
![image](https://github.com/RinaProg/SqlAlchemy-ORM-Python/assets/122221586/3804216f-0a85-4773-8dd5-90d0f621be8e)


## 
