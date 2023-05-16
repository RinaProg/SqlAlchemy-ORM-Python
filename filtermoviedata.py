from movies import Movie,sess1
from sqlalchemy import select
from sqlalchemy import or_


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

print("-------------MOVIE NAME START WITH 'TOY'-------------\n")
mv=select(Movie).where(Movie.title.startswith("Toy"))
for s in sess1.scalars(mv):
    print(s)
print("\n")
print("+" *40) 

print("----------------MOVIES RELEASE AFTER '2008'----------------\n")
mv=select(Movie).where(Movie.release_yr>2008)
for r in sess1.scalars(mv):
    print(r)
print("\n")
print("+" *40)    

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

print("--------------USING FILTER---------------\n")
mv=sess1.query(Movie).filter(Movie.title=="Psycho").first()
print(mv.release_yr,mv.rating)
print("\n")
print("+" *40)

mv=sess1.query(Movie).filter(or_(Movie.title=="Psycho",Movie.title=="Inception"))
for f in mv:
   print(f.release_yr,f.rating)
print("\n")
print("+" *40)

print("---------------USING COUNT----------------\n")
mv_count=sess1.query(Movie).filter(or_(Movie.title=="Psycho",Movie.title=="Inception")).count()
print("No. of movies= ",mv_count)
print("\n")
print("+" *40)

# print("-----------------UPDATE MOVIE---------------\n")
# mv=sess1.query(Movie).filter(Movie.title=="Interstellar").first()
# mv.title="The Matrix"
# sess1.commit()
# print("\n")
# print("+" *40)

print("-----------------DELETE MOVIE---------------\n")
mv=sess1.query(Movie).filter(Movie.title=="The Great Escape").first()
sess1.delete(mv)
sess1.commit()
print("\n")
print("+" *40)