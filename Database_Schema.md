Tables
- Users
    - Username (primary key)
    - First Name
    - Last Name
    - Followers (foreign key)
    - Artists (foreign key)

- Artists
    - id (primary key - taken from api)
    - Genre (foreign key - taken from api)
    - Username (foreign key)


- Genres
    - id (primary key)
    - Artists (foreign key)


- Followers
    - Username (primary key)
    - Following (foreign key)
