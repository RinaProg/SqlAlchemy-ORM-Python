# Movie-Data | SqlAlchemy-ORM-Python

## ORM
SQLAlchemy is famous for its object-relational mapper (ORM),where classes can be mapped to the database, 
thereby allowing the object model and database schema to develop in a cleanly decoupled way from the beginning.

### Documentation : https://docs.sqlalchemy.org/en/20/orm/
## SHOW DATA :
 
```python
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
```
    
##OUTPUT :
```
The Godfather 1972 9 /10  
The Dark Knight 2008 9 /10
The Godfather Part II 1974 9 /10
Inception 2010 8 /10 
The Matrix 1999 8 /10
Psycho 1960 8 /10
Avengers(Infinity War) 2018 8 /10
Toy Story 3 2010 8 /10 
Citizen Kane 1941 8 /10

```

<p><img src="https://github.com/RinaProg/SqlAlchemy-ORM-Python/assets/122221586/0e2cef5f-1122-4147-bcd2-e456f53bd79b" width="420" height="350">&nbsp;&nbsp;
<p><img src="https://github.com/RinaProg/SqlAlchemy-ORM-Python/assets/122221586/3804216f-0a85-4773-8dd5-90d0f621be8e" width="500" height="250">&nbsp;&nbsp;</P>



## 
