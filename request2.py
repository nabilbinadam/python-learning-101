

data={
  "band": {
    "name": "The Example Band",
    "genre": "Rock",
    "founded": 2005,
    "members": [
      {
        "name": "John Doe",
        "role": "Lead Vocals",
        "age": 35
      },
      {
        "name": "Jane Smith",
        "role": "Guitarist",
        "age": 32
      },
      {
        "name": "Mike Johnson",
        "role": "Bassist",
        "age": 30
      },
      {
        "name": "Emily Davis",
        "role": "Drummer",
        "age": 28
      }
    ],
    "albums": [
      {
        "title": "First Album",
        "release_year": 2006,
        "tracks": 10
      },
      {
        "title": "Second Album",
        "release_year": 2009,
        "tracks": 12
      },
      {
        "title": "Greatest Hits",
        "release_year": 2015,
        "tracks": 15
      }
    ],
    "website": "http://www.exampleband.com",
    "bio": "The Example Band is known for their energetic performances and thought-provoking lyrics."
  }
}

bandname= [member["name"]for member in data["band"]["members"]]

print (bandname)