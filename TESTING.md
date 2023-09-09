# Code Buddy Testing

[Back to the README.md file](https://github.com/GenaGrig/genstar-fitness/blob/main/README.md)  

[View the live website here](https://genstar-fitness-and-gym-0d51dc3aa6d0.herokuapp.com/)  

## Table of Contents

1. [Testing User Stories](#testing-user-stories)
2. [Code Validation](#code-validation)
3. [Accessibility](#accessibility)
4. [Tools Testing](#tools-testing)
5. [Manual Testing](#manual-testing)

# Testing User Stories

### As a Site User I can navigate on web-site easily so that I can find neccessary information and links fast

* Easy understandable navigation bar was made with descriptive links
* Separate navigation bar was made for profile view containing only neccessary links for booking and checking profile

### As a Site User I can create account so that I can login and book workout, see all my passes and edit or delete them

* Registration form was updated for easy understanding and hints below each field
* After registration user gets redirected to profile page, where user can book workout and have all the CRUD features

### As a Site User I can find information about memberships so that I can choose one that suits me best

* Membership page contains all the neccessary information about available memberships and its preferences
* Right now "Buy membership" button does not work, because payment system can not be implemented at this stage

### As a Site User I can login to my account so that I can book/view/edit or delete workout or personal training

* CRUD functionality was implemented to give user ability to create booking, see all booked pases, edit and delete them

### As a Site User I can see all available workouts so that I can choose that one that suits me best!

* Workout page was made to list all available workouts to choose from
* Each workout has a little photo and description for understanding what it is about

### As a Site User I can see what preferences gives personal trainer so that I can understand how can he help me with my goals

* Personal trainer is extra feature that gives help to users who are new to a fitness club or workouts
* Contact form is added for users to contact personal trainers with personal questions and advices

### As a Site User I can see clubs contact information so that I can visit or contact them

* All contact information is available at contact page
* Google Maps API was embedded on page to show location of fitness club
* Contact form is added to provide users possibility to contact club reception with different questions

### As a Site User I can get a confirmation modal about deleting my booking so that I can not to delete my booking accidentally

* Extra feature as delete workout confirmation modal was implemented to secure that user will not delete workout accidentally
* Same feature was added for staff members on staff panel for the same reason 

### As a Site User I want to see my user panel so that I can see advanced information and booked workouts

* User panel contains general information about user, such as first and last name, user name and email address
* Below the user panel "My bookins" part contains all bookings made by user with buttons to edit or delete them

### As a Site Admin or Staff member I can use Staff panel so that I can see all bookings made by users

* Staff panel is available only for staff members and admins
* Staff panel contains all bookings made by all users

### As a Staff member I can use search panel so that I can sort out only one type of workout and see all bookings for it

* Staff panel contains Search panel that can filter workouts by different values, every value is searchable

### As a Site User I can have all CRUD functionality so that I can create, see, edit and delete my bookings

* Registered site users has access to CRUD functionality on their Profile page
* Booking can be added, seen in My Booking, edited and deleted in appropriate row with help of related icons

# Code Validation

