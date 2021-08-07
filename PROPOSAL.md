# Synctify

## Synctify is an app that connects users together based on their tastes in music.

Goal: to make it easier to find, interact and grow your social circle through music.

Demographic: Everyone! Who doesn't enjoy music?


- Project Outline
     - APIs
        - Spotify - general api (no authorizeation)
    - Database Schema
        - Tables
            - Users
                - User will sign up on Synctify. After creating an account they will be given the option to connect to their Spotify account. If they choose to do so, all their music preferences will be imported automatically. If they choose not, Synctify will still connect them to Spotify's API and they will manually choose Genres, Artists and Tracks that they like.
                    - Users will be able to follow other users that they connect with. One way connections will have different priviledges that two way connections. 
            - Genres
            - Artists
            - Tracks
    - Sensitive Information
        - Spotifty User information
            - Name
            - Email
            - Location
    - Potential Issues
        - Having two distinct methods for gathering preferences from a user and storing in Syncitfy's db. Automatically gathering music preferences will be easy. Coding the flow of figuring out a user's interests manually is going to be difficult. 
    - User Flow
        - Register
            - User agrees to share certain information with other users based on preferences.
        - Login
        - Gather Preferences
            - Automatically through Spotify with OAuth
                - Simple
            - Manually through Spotify's general API
                - Complex: Show the user genre's first? Then Artists? Then Tracks? Honestly not sure how this flow is going to work. 
        - Home Page
            - Find other users based on similarities in likes
                - ~Tracks hold highest weight~
                - Artists hold next highest weight
                - ~Genre's hold lowest weight~
                - As application scales, location begins holding a certain amount of weight.
            - Top of page is Nav bar for site.
            - Center of page is 'tinder like' matching that shows you a card with username, profile image, and short list of highest weighted similarities.
                - User will be given two options: Connect, or Continue.
                    - Continue: the preference is recorded and user will not be shown the same possible connection again.
                    - Connect: the connection is then appended to the list on right side of page.
                        - If both users choose to connect, a 'gold' banner appears around that connection in list and contact info becomes visible.
            - Bottom of page is Spotify music player that plays through liked tracks of current user.
            - Right side of page is editable list of connections to other users.
            - Left side of page is an editable, node-style list of Genres, Artists, and Tracks. Tracks will have a small play button that will send them to player on the bottom of the page. Editing this list will NOT create POST requests to Spotify. 


            Shorter updates - more feedback between points
            Have a northstar for this project
            Normalize the ratings for each user
            Keep track of how many people total have seen a specific user
                give higher weight to users who have been seen less
            Research matching algorithms
                Look for simple alternatives
                Or use a library
                


        
   
    


