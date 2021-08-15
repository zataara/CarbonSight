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
                - User will sign up on Synctify. 
            - Genres
            - Artists
            - Tracks
    - Sensitive Information
        - Spotifty User information
            - Name
            - Email
            - Location
    - Potential Issues
    - User Flow
        - Register
            - User agrees to share certain information with other users based on preferences.
        - Login
        - Gather Preferences
            - Manually through Spotify's general API
                - Have the user add a few Genre's they are interested in. Then display top artists in those genres. The user can then add the artists that are displayed or search for more. At any time the user can move on to the home page. The gathering prefrences page will not be shown again to the user.
        - Home Page
            - Find other users based on similarities in likes
                - Only using artists to match others. Artists are shown in a heirarchical structure and user can adjust heirarchy and search for more artists in search bar. 
            - Top of page is Nav bar for site.
            - Center of page is 'tinder like' matching that shows you a card with username, profile image, and short list of highest weighted artist similarities
                - User will be given two options: Connect, or Continue.
                    - Continue: the preference is recorded and user will not be shown the same possible connection again.
                    - Connect: the connection is then appended to the list on right side of page.
                        - If both users choose to connect, a 'gold' banner appears around that connection in list and contact info becomes visible.
            - Bottom of page is Spotify music player that plays through liked tracks of current user?
            - Right side of page is editable list of connections to other users.
            - Left side of page is an editable, heirarchical tree of liked Artists. 


            Notes:
            Shorter updates - more feedback between points
            Have a northstar for this project
            Normalize the ratings for each user
            Keep track of how many people total have seen a specific user
                give higher weight to users who have been seen less
            Research matching algorithms
                Look for simple alternatives
                Or use a library
                


        
   
    


