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

<movie name=The Godfather release year=1972 and rating=9 >
<movie name=Psycho release year=1960 and rating=8 >
```
## START WITH :
```python
print("-------------MOVIE NAME START WITH '...'-------------\n")
mv=select(Movie).where(Movie.title.startswith("Toy"))
for s in sess1.scalars(mv):
    print(s)
print("\n")
print("+" *40) 

```
##OUTPUT :
```
<movie name=Toy Story 3 release year=2010 and rating=8 >
```
## USING FILTER :
```python
print("--------------USING FILTER---------------\n")
mv=sess1.query(Movie).filter(Movie.title=="Psycho").first()
print("Release year =",mv.release_yr)
print("Rating =",mv.rating)
print("\n")
print("+" *40)
```
## OUTPUT :
```
Release year = 1960
Rating = 8
```
## COUNT :
```python
print("---------------USING COUNT----------------\n")
mv_count=sess1.query(Movie).filter(or_(Movie.title=="Psycho",Movie.title=="Inception")).count()
print("No. of movies= ",mv_count)
print("\n")
print("+" *40)
```
## OUTPUT :
```
No. of movies=  2
```
## SORT METHOD :
```python
print("-----------------SORTED BY MOVIES NAME(ASCENDNG ORDER)------------------\n")
mv=select(Movie).order_by(Movie.title.asc())
for a in sess1.scalars(mv):
    print(a)
print("\n")
print("+" *40)

print("-----------------SORTED BY RATING(DESCENDING ORDER)-------------------\n")
mv=select(Movie).order_by(Movie.rating.desc())
for d in sess1.scalars(mv):
    print(d)
print("\n")
print("+" *40)
```
## OUTPUT :
```
-----------------SORTED BY MOVIES NAME(ASCENDNG ORDER)------------------
<movie name=The Godfather release year=1972 and rating=9 >
<movie name=The Dark Knight release year=2008 and rating=9 >
<movie name=The Godfather Part II release year=1974 and rating=9 >
<movie name=Inception release year=2010 and rating=8 >
<movie name=The Matrix release year=1999 and rating=8 >
<movie name=Psycho release year=1960 and rating=8 >
<movie name=Avengers(Infinity War) release year=2018 and rating=8 >
<movie name=Toy Story 3 release year=2010 and rating=8 >
<movie name=Citizen Kane release year=1941 and rating=8 >

-----------------SORTED BY RATING(DESCENDING ORDER)--------------------
<movie name=The Godfather release year=1972 and rating=9 >
<movie name=The Dark Knight release year=2008 and rating=9 >
<movie name=The Godfather Part II release year=1974 and rating=9 >
<movie name=Inception release year=2010 and rating=8 >
<movie name=The Matrix release year=1999 and rating=8 >
<movie name=Psycho release year=1960 and rating=8 >
<movie name=Avengers(Infinity War) release year=2018 and rating=8 >
<movie name=Toy Story 3 release year=2010 and rating=8 >
<movie name=Citizen Kane release year=1941 and rating=8 >
```
