# Genstar Fitness

Genstar Fitness is a web site for a local fitness club and gym with full functionality to its user, allowing to get all neccessarey infromation about fitness services, prices and additional services. Web site allows for user to create account, login and logout, change users information and most importantly book different workouts, see them in convenient form, edit and delete them.

The main idea of the site is to give to the users first impresions of a Genstar Fitness and convenient user-friendly platform, where they can easily manage their workout bookings.
Staff members can see all the workouts that will help to plan their schedule.

You can visit the deployed website here - [Genstar Fitness](https://genstar-fitness-and-gym-0d51dc3aa6d0.herokuapp.com/).

Github repository you can find here - [Github repo](https://github.com/GenaGrig/genstar-fitness.git).

## Table of contents

1. [User Experience (UX)](#user-experience-ux)
    1. [Strategy](#strategy)
        1. [Project Goals](#project-goals)
        2. [User Stories](#user-stories)
        3. [Strategy Table](#strategy-table)
    2. [Scope](#scope)
    3. [Structure](#structure)
    4. [Skeleton](#skeleton)
    5. [Surface](#surface)
2. [Features](#features)
    1. [General](#general)
    2. [Home Page](#home-page)
    3. [Membership Page](#membership-page)
    4. [Workouts Page](#workouts-page)
    5. [PT Page](#personal-trainer-page)
    6. [Terms of Use Page](#terms-of-use-page)
    7. [Profile Page](#profile-page)
    8. [Booking Pages](#booking-pages)
    9. [Staff Panel Page](#delete-reply-page)
    10. [Authentication Pages](#authentication-pages)
3. [Technologies Used](#technologies-used)
    1. [Languages Used](#languages-used)
    2. [Libraries and Frameworks](#languages-and-frameworks)
    3. [Packages / Dependecies Installed](#packages--dependecies-installed)
    4. [Database Management](#database-management)
    5. [Tools and Programs](#tools-and-programs)
4. [Testing](#testing)
    1. [Go to TESTING.md]()
5. [Deployment](#deployment)
6. [Finished Product](#finished-product)
7. [Credits](#credits)
8. [Known Bugs](#known-bugs)
9. [Acknowledgements](#acknowledgements)

***

# User Experience (UX)

### Strategy

#### Project goals

* Website uses modern techniques and frameworks to be attractive to user
* Color palette and constrast is used in such way that site elements do not stick out or disappear behind
* Responsive design makes the website accessible on differents devices and screen sizes
* Navigation panel is easy to use and names are descriptive
* Structure of website is easy to understand and navigate
* Site users are able to register an account to use extra services
* Site users are able to login to their accounts to use extra services
* Site users are able to logout from their accounts to secure their private information and bookings
* Site users can book workouts and track(see through), edit or delete them
* Site users are able to edit their profiles after creating account
* Website uses pop-up messages that follows actions made by the users

#### User Stories

* As a Site User I can navigate on web-site easily so that I can find neccessary information and links fast
* As a Site User I can create account so that I can login and book workout, see all my passes and edit or delete them
* As a Site User I can find information about memberships so that I can choose one that suits me best
* As a Site User I can login to my account so that I can book/view/edit or delete workout or personal training
* As a Site User I can see all available workouts so that I can choose that one that suits me best!
* As a Site User I can see what preferences gives personal trainer so that I can understand how can he help me with my goals
* As a Site User I can see clubs contact information so that I can visit or contact them
* As a Site User I can get a confirmation modal about deleting my booking so that I can not to delete my booking accidentally
* As a Site User I want to see my user panel so that I can see advanced information and booked workouts
* As a Site Admin or Staff member I can use Staff panel so that I can see all bookings made by users
* As a Staff member I can use search panel so that I can sort out only one type of workout and see all bookings for it
* As a Site User I can have all CRUD functionality so that I can create, see, edit and delete my bookings

At the start of the project user stories looked like this:
![Screenshot of user stories at the start on GitHub](/media/screenshots/user-stories-to-do.PNG)

#### Strategy Table

Opportunity / Problem | Importance | Viability / Feasibility
--- | --- | ---
Responsive design | 5 | 5
Account registration | 5 | 5
Ability to buy membership | 1 | 0
Social media signup | 1 | 0
Book, edit and delete workouts| 5 | 5
Ability to search/filter for bookings | 3 | 2
Delete booking confirmation | 4 | 3
**Total** | **24** | **20**

### Scope

Based on stategy table, not all the features will be implemented in the first deployment of the project and some of the features will not be implemented at all, because of their difficulties at this stage. The main goal was to make a MVP or minimum viable product, so the user can have fully functional web site and make all the neccessary manipulations mentioned in user stories.

#### Features that will not be implemented at this stage
* Social media signup
* Ability to buy membership

### Structure

![Structure of the Genstar Fitness website](/media/screenshots/genstar-fitness-structure.png)

https://www.appsloveworld.com/django/100/94/django-user-account-update-ignore-user-with-this-username-already-exists - fix problem with update user profile, username already exist
https://www.youtube.com/watch?v=F5kTZdi_c5k - update user profiles
https://www.youtube.com/watch?v=JeTGxvFnAaU&list=TLPQMDYwODIwMjOuesC_k1wr0A&index=1 - register users
https://blog.devgenius.io/django-tutorial-on-how-to-create-a-booking-system-for-a-health-clinic-9b1920fc2b78 - booking system tutorial
