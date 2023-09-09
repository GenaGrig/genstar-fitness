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
    4. [Surface](#surface)
2. [Features](#features)
    1. [Main features](#main-features)
    2. [Home Page](#home-page)
    3. [Membership Page](#membership-page)
    4. [Workouts Page](#workouts-page)
    5. [PT Page](#personal-trainer-page)
    6. [Contact Page](#contact-page)
    7. [Terms of Use Page](#terms-of-use-page)
    8. [Profile Page](#profile-page)
    9. [Update Profile Page](#update-profile-page)
    10. [Booking Pages](#booking-pages)
    11. [Staff Panel Page](#staff-panel-page)
    12. [Authentication Pages](#authentication-pages)
3. [Technologies Used](#technologies-used)
    1. [Languages Used](#languages-used)
    2. [Libraries and Frameworks](#languages-and-frameworks)
    3. [Packages / Dependecies Installed](#packages--dependecies-installed)
    4. [Database Management](#database-management)
    5. [Tools and Programs](#tools-and-programs)
4. [Testing](#testing)
    1. [Go to TESTING.md](https://github.com/GenaGrig/genstar-fitness/blob/main/TESTING.md)
5. [Deployment](#deployment)
6. [Credits](#credits)
7. [Known Bugs](#known-bugs)
8. [Acknowledgements](#acknowledgements)

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

### Surface

#### Color palette

Color scheme of blue(#0126fa) for navigation bar background, light blue(#47a9ff) for footer and some container page elements background and white(#ffffff) for text color on a blue or light blue background. These colors are used througout the website and create together mild color palette for user eyes to make the UI and UX smoother.

![Screenshot of color palette for website](/media/screenshots/color-palette.PNG)

#### Fonts

No extra fonts we used on this website. All fonts are default by Bootstrap. There is no difficulties to read the text written used by this fonts.

[Back to top ⇧](#genstar-fitness)

# Features

### Main features

The website is made using the responsive design in mind, as not only desktop PC or laptop users will be visiting it. Website runs smoothly on tablettes and phones as well and supports differents screen sizes.

There are several main website elements that are presented on each page.

#### Navigation bar
* Main navigation bar
![Screenshot of main navigation bar](/media/screenshots/navigation-bar-main.PNG)

Main navigation bar contains all the neccessary buttons for user to get all the information about fitness club services, memberships and contacts. 

* User logged in navigation bar
![Screenshot of navigation bar when user logged in](/media/screenshots/navigation-bar-logged-in.PNG)

When user is authenticated, on main navigation bar adds three new buttons such as "Book Workout" - as direct link to booking service, "My Profile" - page where user can see all his bookings, edit or delete them; edit profile; make new bookings and "Logout" to logout from account.

* Navigation bar on user profile / booking page
![Screenshot of navigation bar on user profile/booking page](/media/screenshots/navigation-bar-booking.PNG)

This is navigation bar which is shown when user clicks on "Book Workout" or "My Profile" buttons after user gets authenticated. On this navbar you can see "Staff Panel" button, which is only available to users which have roles as admins or staff members. This button opens a page where staff members or admins can see all the bookings made by users, filter them or delete. More about this button you can find in [THIS](#staff-panel-page) section.

#### Footer

Footer contains information about:
- fitness club opening hours, reception opening hours (when the personal of the club are available on site)
- contact information such as address, phone and email
- social network links, such as Twitter, Instagram and Facebook

#### Flash messages

Flash messages is a very helpful and good for UX tool that flashes when user make some active action such as creating new account or making a new booking. Some other functions when message pops up are - edit profile, edit or delete booking, login and logout.

![Screenshot of flash message after account creation](/media/screenshots/flash-message-new-account.PNG)
![Screenshot of flash message after new booking](/media/screenshots/flash-message-booking.PNG)

### Mobile menu
Menu main | Menu auth | Menu profile |
--- | --- | --- |
![Desktop Home Page image](/media/screenshots/mobile/main-menu-mobile-res.jpg) | ![Mobile Home Page image ](/media/screenshots/mobile/main-menu-auth-mobile-res.jpg) | ![Mobile Home Page image ](/media/screenshots/mobile/profile-page-menu-mobile-res.jpg)


[Back to top ⇧](#genstar-fitness)

### Main page
Desktop | Mobile |
--- | --- |
![Desktop Home Page image](/media/screenshots/desktop/main-page-desktop.png) | ![Mobile Home Page image ](/media/screenshots/mobile/main-page-mobile-res.jpg) |

Main page has one major element which is carousel which contains 3 slides with photos and captions with informative text on them to give to users some basic information about fitness club. It does not scroll automatically, only when user scrolls for the first time, slides start to scroll. But when the mouse is over the slide, automatic scroll stops. 

### Membership page
Desktop | Mobile |
--- | --- |
![Desktop Membership Page image](/media/screenshots/desktop/membership-page-desktop.png) | ![Mobile Membership Page image ](/media/screenshots/mobile/membership-page-mobile-res.jpg) |

Membership page has information about different membership types and which preferences each type gives. There are three types of membership, such as Standart, Student and All Inclusive, each with its own benefits. The button "Buy membership" shold link to checkout page, but for now it is disabled, as payment option is not neccessary in this project. 
* As a future option, membership role will affect booking opportunities, as some membership roles contains exclusive offers
* As a future change, workouts can book only fitness club members (now it can do everyone, who has an active account) or those who have free pass or onetime payment

### Workouts page
Desktop | Mobile |
--- | --- |
![Desktop Workouts Page image](/media/screenshots/desktop/workouts-page-desktop.png) | ![Mobile Workouts Page image ](/media/screenshots/mobile/workouts-page-mobile-res.jpg) |

Workouts page contains all available at the moment workouts that can be booked after user is logged in. The main section is made with a Bootstrap component called 'Accordion'. Each workout in accordion list opens one at a time, closing the previously opened to save space on different screen sizes, espesially phones and skip extra scrolling. As a future option a small book active workout button can be added below each workout description.  

### PT page
Desktop | Mobile |
--- | --- |
![Desktop Personal Trainer Page image](/media/screenshots/desktop/personal-trainer-page-desktop.png) | ![Mobile Personal Trainer Page image ](/media/screenshots/mobile/personal-trainer-page-mobile-res.jpg) |

Personal trainers page has general infromation about who are personal trainers and with what questions they can help with. Page contains a contact form for the questions regarding personal training, where user can choose a category that suits to users question or leave it as general question. Right now form does not work as planned and it will be fixed in future releases. 

### Contact page
Desktop | Mobile |
--- | --- |
![Desktop Contact Page image](/media/screenshots/desktop/contact-page-desktop.PNG) | ![Mobile Contact Page image ](/media/screenshots/mobile/contact-page-mobile-res.jpg) |

Contact page contains two general elements, Google map and contact form. It contains also a general contact information, but as it duplicates with footer, it is made just for good looking symmetry. 

Google maps API is responsive and change its size according to screen size. Two containers with contact information and form are also responsive and all elements on a page has a column structure on small screen sizes. 

### Terms of Use pages

This section is neccessary, because fitness club needs to protect its rights on a website and information its contains. The first document 'Terms and Conditions' contains general rules and regulations for the use of Genstar Fitness's website. By accessing the website user accepts terms and conditions automatically, otherwise user needs to leave website.

Privacy Policy/GDPR is a document that secures visitors privacy. As the website collects and stores users information, this document provides description of which information is collected and how it is used. 

#### Terms and Conditions
Desktop | Mobile |
--- | --- |
![Desktop Terms and Conditions Page image](/media/screenshots/desktop/terms-and-conditions-desktop.png) | ![Mobile Terms and Conditions Page image ](/media/screenshots/mobile/terms-and-conditions-mobile-res.jpg) |

#### Privacy Policy/GDPR
Desktop | Mobile |
--- | --- |
![Desktop Privacy Policy Page image](/media/screenshots/desktop/private-policy-desktop.png) | ![Mobile Privacy Policy Page image ](/media/screenshots/mobile/privacy-policy-mobile-res.jpg) |

### Profile page
Desktop | Mobile |
--- | --- |
![Desktop User Profile Page image](/media/screenshots/desktop/user-profile-page-desktop.png) | ![Mobile User Profile Page image ](/media/screenshots/mobile/user-profile-new.jpg) |

User profile page consists of two major parts - User Info and My Bookings.
* User Info contains infromation about user as first and last name, username and email. There is an Edit Profile button which allows users to change their data. By default first and last name are empty, so user needs to enter them by editing profile. As a future feature more fileds to user profile will be added. 

* My Bookings part allows user to see all reserved bookings and edit or delete them. Here all the CRUD functionality is implemented. User can create a booking, see all bookings made, update bookings and delete them. Edit and delete buttons are shown as icons, because this design is much more comfortable on small screens, such as phones. 

#### Delete Workout Confirmation Modal

Desktop | Mobile |
--- | --- |
![Desktop Delete Booking Confirmation Modal image](/media/screenshots/desktop/confirm-delete-modal-desktop.PNG) | ![Mobile Delete Booking Confirmation Modal image ](/media/screenshots/mobile/delete-booking-confirmation-mobile-res.jpg) |

This is an extended feature for user convenience and to be sure that user will not delete booking accidentally. The same feature is realised on staff panel for the same reason.

### Update profile page
Desktop | Mobile |
--- | --- |
![Desktop Update Profile Page image](/media/screenshots/desktop/update-profile-form-desktop.PNG) | ![Mobile Update Profile Page image ](/media/screenshots/mobile/update-profile-mobile-res.jpg) |

This page allows user to update profile and change such information as first and last name (empty by default), username and email. As a future feature change of password and some extra fields can be added.

### Booking pages
Desktop | Mobile |
--- | --- |
![Desktop Booking Page image](/media/screenshots/desktop/booking-page-desktop.PNG) | ![Mobile Booking Page image ](/media/screenshots/mobile/booking-page-mobile-res.jpg) |

On this booking page user selects workout type and date in pop-up calender. When done, user need to click on continue to proceed to next page or back to return to user profile page. 

Desktop | Mobile |
--- | --- |
![Desktop Booking Time Page image](/media/screenshots/desktop/booking-time-page-desktop.PNG) | ![Mobile Booking Time Page image ](/media/screenshots/mobile/booking-time-select-mobile-res.jpg) |

On this page user need to select time for chosen workout. When done, user clicks on "Book Workout" to confirm and save booking, or "Back" to go back to previous page and change workout or date.

* This booking section has a lot of improvement possibilities that can be added in the future. For example:
    * Schedule for each workout with exakt dates and time which repeates every week
    * Make all booking process on a single page to reduce clicking and pages count
    * Add workout booking for non-member of fitness club as a free pass or onetime payment (requires payment system and functionality)

### Staff panel page
Desktop | Mobile |
--- | --- |
![Desktop Staff Panel Page image](/media/screenshots/desktop/staff-panel-page-desktop.png) | ![Mobile Staff Panel Page image ](/media/screenshots/mobile/staff-panel-new.jpg) |

Staff panel is made only for admins and staff members. On this panel staff members can see all the bookings made by users and filter them by different values. 


### Authentication pages

#### Register New Account

Desktop | Mobile |
--- | --- |
![Desktop Register Account image](/media/screenshots/desktop/register-account-page-desktop.PNG) | ![Mobile Register Account Page image ](/media/screenshots/mobile/register-accont-mobile-res.jpg) |

Register New Account form contains three required fields that should be filled to register new user and save users' information to database. Each field has a little description below, to help the user enter correct information and avoid mistakes. After this procedure, user is available to log in to website at anytime. After registration user is redirected to users' profile page directly, without need to sign in. If user already has an account and opened register account page by mistake, there is a direct link to sing in page in header or on navigation bar.

#### Sign In page

Desktop | Mobile |
--- | --- |
![Desktop Sign In Page image](/media/screenshots/desktop/sign-ip-desktop.PNG) | ![Mobile Sign In Page image ](/media/screenshots/mobile/sign-in-page-mobile-res.jpg) |

Sign In page has just to field to be filled as Username and Password, which user entered when registered new account. There is a checkbox "Remember me" to store user infromation as cookie. Below that there is a "Forgot password" link, that redirects user to a password reset page, where user needs to enter email address and get a link to change password. 

#### Sign Out

Desktop | Mobile |
--- | --- |
![Desktop Sign Out Page image](/media/screenshots/desktop/sign-out-page-desktop.png) | ![Mobile Sign Out Page image ](/media/screenshots/mobile/sign-out-page-mobile-res.jpg) |

Sign Out page is quite simple and contains only one button - "Sign Out". At this stage action can be reverted and user can go back to other pages without signing out. As a feature feature this page can be changed to modal with same functionality.

### Future features

Some features where mentioned directly in page description, but lets summarize them in this section:

* Membership. Membership role will affect booking opportunities, as some membership roles contains exclusive offers
* Membership. Workouts can be booked only by fitness club members (now it can do everyone, who has an active account) or those who have free pass or onetime payment (requires payment system on a website)
* Workout. Schedule for each workout with fixed days and times
* Personal Trainer. Possibility to book a personal trainer session both free and for a fixed price
* Personal Trainer and Contact pages contact forms should send messages to user emails
* Update profile should be able to change password. Several field with information should be available to update, such as address, city, country and telephone number
* Booking. All booking process on one page
* Booking. Booking for non-members for free (testing pass) or fixed price
* Register form with more information, such as first and last name and telephone number
* Sign out function as a modal, to skip the separate sign out page. 

[Back to top ⇧](#genstar-fitness)

# Technologies Used

### Languages Used

* [HTML5](https://en.wikipedia.org/wiki/HTML)
* [CSS3](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))


### Libraries and Frameworks

* [Django](https://www.djangoproject.com/)   
    * Django was used as web framework.
   
* [Bootstrap 5](https://getbootstrap.com/)  
    * Bootstrap 5 was used throughout the website to help with styling and responsiveness.

* [Font Awesome](https://fontawesome.com)  
    * Font Awesome was used throughout the website to add icons for aesthetic and UX purposes. 


### Packages / Dependecies Installed

* [Django Allauth](https://django-allauth.readthedocs.io/en/latest/)  
    * Django Allauth was used for user authentication, registration, and account management.

* [Django Crispy Form](https://django-crispy-forms.readthedocs.io/en/latest/)   
    * Django Crispy Form was used to control the rendering of the forms. 
 
* [Gunicorn](https://gunicorn.org/)  
    * Gunicorn was used as Python WSGI HTTP Server for UNIX to support the deployment of Django application.  

* [Cloudinary](https://cloudinary.com/)
    * Cloudinary has been used as image management solution

### Database Management
* [ElephantSQL](https://www.elephantsql.com/)   
    * ElephantSQL as a Service database was used in production, as a service based on PostgreSQL.


### Tools and Programs

* [Git](https://git-scm.com)  
    * Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub. 

* [GitPod](https://gitpod.io/)
     * GitPod was used for writing code, committing, and then pushing to GitHub.

* [GitHub](https://github.com)  
    * GitHub was used to store the projects code after being pushed from Git. 

* [Heroku](https://www.heroku.com)   
    * Heroku was used to deploy the website.

* [Am I Responsive](ami.responsivedesign.is)  
    * Am I Responsive was used to preview the website across a variety of popular devices.

* [Coolors](https://coolors.co)  
    * Coolors was used to create a color scheme for the website.

* [Chrome DevTools](https://developer.chrome.com/docs/devtools/)
    * Chrome DevTools was used during development process for code review and to test responsiveness.

* [W3C Markup Validator](https://validator.w3.org/)
    * W3C Markup Validator was used to validate the HTML code.

* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
    * W3C CSS Validator was used to validate the CSS code.

* [JSHint](https://jshint.com/) 
    * The JSHints JavaScript Code Quality Tool was used to validate the site's JavaScript code.

* [Google Maps](https://www.google.com/maps)
    * Google maps API to embed google map with location on a website.

* [Terms and Conditions generator](https://www.termsandconditionsgenerator.com)
    * Terms and Conditions generator was used to create an agreement between website and user for protection of GenStar Fitness website rights

* [Privacy Policy generator](https://www.termsfeed.com/privacy-policy-generator/)
    * Privacy Policy generator was used to create a document describing which information GenStar Fitness website collects and stores and how it secures users privacy

[Back to top ⇧](#genstar-fitness)

# Testing

The testing is available in separate file [TESTING.md](https://github.com/GenaGrig/genstar-fitness/blob/main/TESTING.md)

# Deployment

This project was developed using a [GitPod](https://gitpod.io/) workspace. The code was commited to [Git](https://git-scm.com/) and pushed to [GitHub](https://github.com/") using the terminal.

### Deploying on Heroku
To deploy this page to Heroku from its GitHub repository, the following steps were taken:

1. Create the Heroku App:
    - Select "Create new app" in Heroku.
    - Choose a name for your app and select the location.

2. Attach the Postgres database:
    - Open [ElephantSQL](https://www.elephantsql.com/) website and create free account
    - Click on green button Create New Instance
    - Select Name of the project and plan Tiny Turtle (Free), click on continue
    - Select your region, click on Review
    - Check all information and click on Create instance
    - Click on your instance in the list to open its details
    - Copy database URL in URL field
    - Open your Heroku project
    - Open Settings tab and click on Reveal Config Vars
    - In a field Key add DATABASE_URL
    - In a field VALUE add postgres url from ElephantSql created instance
    - Click on ADD to finish the process

3. Prepare the environment and settings.py file:
    * In the Settings tab, click on Reveal Config Vars and copy the url next to DATABASE_URL.
    * In your GitPod workspace, create an env.py file in the main directory. 
    * Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.
    * Add the SECRET_KEY value to the Config Vars in Heroku.
    * Update the settings.py file to import the env file and add the SECRETKEY and DATABASE_URL file paths.
    * Update the Config Vars with the Cloudinary url, adding into the settings.py file also.
    * In settings.py add the following sections:
        * Cloudinary to the INSTALLED_APPS list
        * STATICFILE_STORAGE
        * STATICFILES_DIRS
        * STATIC_ROOT
        * MEDIA_URL
        * DEFAULT_FILE_STORAGE
        * TEMPLATES_DIR
        * Update DIRS in TEMPLATES with TEMPLATES_DIR
        * Update ALLOWED_HOSTS with ['app_name.heroku.com', 'localhost']

4. Store Static and Media files in Cloudinary and Deploy to Heroku:
    - Create three directories in the main directory; media, static and templates.
    - Create a file named "Procfile" in the main directory and add the following:
        - web: gunicorn project-name.wsgi
    - Go to Deploy tab on Heroku and connect to the GitHub, then to the required repository.
    Click on Delpoy Branch and wait for the build to load. When the build is complete, the app can be opened through Heroku.

### Forking the Repository
By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log into [GitHub](https://github.com/login) or [create an account](https://github.com/join).
2. Locate the [GitHub Repository](https://github.com/GenaGrig/genstar-fitness.git).
3. At the top of the repository, on the right side of the page, select "Fork"
4. You should now have a copy of the original repository in your GitHub account.

### Creating a Clone
How to run this project locally:
1. Install the [GitPod Browser](https://www.gitpod.io/docs/browser-extension/ "Link to Gitpod Browser extension download") Extension for Chrome.
2. After installation, restart the browser.
3. Log into [GitHub](https://github.com/login "Link to GitHub login page") or [create an account](https://github.com/join "Link to GitHub create account page").
2. Locate the [GitHub Repository](https://github.com/GenaGrig/genstar-fitness.git).
5. Click the green "GitPod" button in the top right corner of the repository.
This will trigger a new gitPod workspace to be created from the code in github where you can work locally.

How to run this project within a local IDE, such as VSCode:

1. Log into [GitHub](https://github.com/login) or [create an account](https://github.com/join).
2. Locate the [GitHub Repository](https://github.com/GenaGrig/genstar-fitness.git).
3. Under the repository name, click "Clone or download".
4. In the Clone with HTTPs section, copy the clone URL for the repository.
5. In your local IDE open the terminal.
6. Change the current working directory to the location where you want the cloned directory to be made.
7. Type 'git clone', and then paste the URL you copied in Step 3.
```
git clone https://github.com/GenaGrig/genstar-fitness.git
```
8. Press Enter. Your local clone will be created.

Further reading and troubleshooting on cloning a repository from GitHub [here](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

[Back to top ⇧](#genstar-fitness)

# Credits

This resources were used as a help to create [GenStar Fitness](https://genstar-fitness-and-gym-0d51dc3aa6d0.herokuapp.com/) website:

### Content
* Website content was written by the developer
* README file was written with help of following documents:
    * Code Institute [README template](https://github.com/Code-Institute-Solutions/readme-template)
    * GitHubs [Basic writing and formatting syntax](https://docs.github.com/ru/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#headings)
    * Hints and some structure of README files from existing projects from other CI students

### Media

* [New register user form tutorial](https://www.youtube.com/watch?v=JeTGxvFnAaU&list=TLPQMDYwODIwMjOuesC_k1wr0A&index=1)
* [Update user profile tutorial](https://www.youtube.com/watch?v=F5kTZdi_c5k)
* [Fix problem with updating user profile, username already exists](https://www.appsloveworld.com/django/100/94/django-user-account-update-ignore-user-with-this-username-already-exists)
* [Booking system tutorial](https://blog.devgenius.io/django-tutorial-on-how-to-create-a-booking-system-for-a-health-clinic-9b1920fc2b78)
* [Booking system tutorial video guide](https://youtu.be/s5xbtuo9pR0?si=x7hmhprUzVnpzoAJ)
* [404 image was taken here](https://pxhere.com/ru/photo/1380359)

### Code

* [Code Institutes' Slack channel](www.slack.com) was used to get help from its students in resolving code problems and questions
* [Bootstrap 5](https://getbootstrap.com/) website was used very often to fix the problems with different elements and get resposive design work
* Some of code functions was written with help of [GitHub Copilot](https://github.com/features/copilot)

[Back to top ⇧](#genstar-fitness)

# Known Bugs

* Booking of workouts is available to everyone who has registered account, membership role does not work and affect booking opportunities for now

# Acknowledgements

* I want to thank my mentor Marcel Mulders for very good feedback and very useful advices that made my project complete and interesting. Very good ideas from my mentor that was implemented and made project look more solid.
* I want to thank members in our Code Institute Slack community for giving feedback and showing their own projects that was inspiring in different ways.

[Back to top ⇧](#genstar-fitness)