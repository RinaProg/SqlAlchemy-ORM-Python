from movies import Movie,sess1

movieset=[
    {
        "title": "The Dark Knight",
        "release_yr":"2008",
        "rating":"9"
        
    },
    {
        "title":"The Godfather Part II",
        "release_yr":"1974",
        "rating":"9"
        
    },
    {
        "title":"Inception",
        "release_yr":"2010",
        "rating":"8"
        
    },
    {
        "title":"The Matrix",
        "release_yr":"1999",
        "rating":"8"	
        
    },
    {
        "title":"Psycho",
        "release_yr":"1960",
        "rating":"8"
        
    },
    {
        "title":"Avengers(Infinity War)" ,
        "release_yr":"2018",
        "rating":"8"
        
    },
    {
        "title":"Toy Story 3",
        "release_yr":"2010",
        "rating":"8"
        
    },
    {
        "title":"Citizen Kane" ,
        "release_yr":"1941",
        "rating":"8"
        
    },
    {
        "title":"The Great Escape",
        "release_yr":"1963",
        "rating":"8"
        
    },
]

for i in movieset:
    mv=Movie(title=i["title"],release_yr=i["release_yr"],rating=i["rating"] )
    sess1.add(mv)
    sess1.commit()