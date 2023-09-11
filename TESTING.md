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

### HTML

[The W3C Markup Validator](https://validator.w3.org) was used to check HTML side of a webpage. Following errors were found:


* Index page errors

![HTML Validator index page check errors](/media/screenshots/testing/html-index-check-errors.PNG)

* Index page errors fixed
    * Errors were fixed by changing failed tags to correct and deleting failed attribute

![HTML Validator index page check fixed](/media/screenshots/testing/html-index-check-fixed.PNG)

* Contact page errors

![Contact page errors](/media/screenshots/testing/html-contact-check-errors.PNG)

* Contact page errors fixed
    * Error was fixed by deleting wrong attribute

![Contact page errors fixed](/media/screenshots/testing/html-contact-check-fix.PNG)

#### All other pages were error free. Some pages html validator was unable to check, giving following error:

![Checking page error 500](/media/screenshots/testing/checking-page-error-500.PNG)

### CSS

For check of CSS in a project [The W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) was used.

There are 4 css files in my project, main is style.css, containing all general styling for the project and overriding most of Bootstrap default css. Booking.css, membership.css and workout.css were made to override default Bootstrap css in specific files, as there were problem with css override when adding to main style.css file. All attempts to join all css files in one were not successfull, as design broke and only discard of changes helped to restore it.

Each file was checked manually in [The W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) and no errors were found.

![No errors in CSS files](/media/screenshots/testing/css-check.PNG)

### Python

Pylint was used continuously during the development process to analyze the Python code for programming errors.

[CI Python Linter](https://pep8ci.herokuapp.com) was used to validate the Python code to validate the Python code for PEP8 requirements. Results are in a table below:


| Location | Errors / Warnings | Code Reviewed |
| --- | --- | --- |
| ./fitness/admin.py | No errors / warnings |![admin.py code reviewed image](/media/screenshots/testing/fitness-admin-py-clean.PNG) |
| ./fitness/apps.py | No errors / warnings |![apps.py code reviewed image](/media/screenshots/testing/fitness-apps-py-clean.PNG) |
| ./fitness/forms.py | ![forms.py errors/warnings image](/media/screenshots/testing/fitness-forms-py-errors.PNG) | ![forms.py code reviewed image](/media/screenshots/testing/booking-forms-py-clear.PNG) |
| ./fitness/models.py | ![models.py errors/warnings image](/media/screenshots/testing/fitness-models-py-errors.PNG) | ![models.py code reviewed image](/media/screenshots/testing/fitness-models-py-clean.PNG) |
| ./fitness/urls.py | No errors / warnings | ![urls.py code reviewed image](/media/screenshots/testing/fitness-urls-py-clean.PNG) |
| ./fitness/views.py | ![views.py errors/warnings image](/media/screenshots/testing/fitness-views-py-errors.PNG) | ![views.py code reviewed image](/media/screenshots/testing/fitness-views-py-clean.PNG) |
| ./booking/admin.py | No errors / warnings |![admin.py code reviewed image](/media/screenshots/testing/booking-admin-py-clear.PNG) |
| ./booking/apps.py | No errors / warnings |![apps.py code reviewed image](/media/screenshots/testing/booking-apps-py-clear.PNG) |
| ./booking/forms.py | ![forms.py errors/warnings image](/media/screenshots/testing/booking-forms-py-errors.PNG) | ![forms.py code reviewed image](/media/screenshots/testing/booking-forms-py-clear.PNG) |
| ./booking/models.py | ![models.py errors/warnings image](/media/screenshots/testing/booking-models-py-errors.PNG) | ![models.py code reviewed image](/media/screenshots/testing/booking-models-py-clear.PNG) |
| ./booking/urls.py | ![urls.py errors/warnings image](/media/screenshots/testing/booking-urls-py-errors.PNG) | ![urls.py code reviewed image](/media/screenshots/testing/booking-urls-py-clear.PNG) |
| ./booking/views.py | ![views.py errors/warnings image](/media/screenshots/testing/booking-views-py-errors.PNG) | ![views.py code reviewed image](/media/screenshots/testing/booking-views-py-clear.PNG) |

### JavaScript

[JSHint, a JavaScript Code Validator](https://jshint.com) was used to check JS code.

No errors were found.

# Accessibility

### Lighthouse Reports

Page | Lighthouse Report |
| --- | --- |
| Home | ![Home Page Lighthouse Report](/media/screenshots/testing/lighthouse/index-lighthouse-report.PNG) |
| Membership | ![Membership Page Lighthouse Report](/media/screenshots/testing/lighthouse/membership-lighthouse-report.PNG) |
| Workouts | ![Workouts Page Lighthouse Report](/media/screenshots/testing/lighthouse/workouts-lighthouse-report.PNG) |
| Register | ![Register Page Lighthouse Report](/media/screenshots/testing/lighthouse/register-lighthouse-report.PNG) |
| Login | ![Login Page Lighthouse Report](/media/screenshots/testing/lighthouse/login-lighthouse-report.PNG) |
| Logout | ![Logout Page Lighthouse Report](/media/screenshots/testing/lighthouse/logout-lighthouse-report.PNG) |
| PT !| ![Personal Trainer Page Lighthouse Report](/media/screenshots/testing/lighthouse/personal-trainer-lighthouse-report.PNG) |
| Contact Us | ![Contact Page Lighthouse Report](/media/screenshots/testing/lighthouse/contact-lighthouse-report.PNG) |
| Terms and Conditions | ![Terms and Conditions Page Lighthouse Report](/media/screenshots/testing/lighthouse/terms-and-conditions-lighthouse-report.PNG) |
| Privacy Policy | ![Privacy Policy Page Lighthouse Report](/media/screenshots/testing/lighthouse/privacy-policy-lighthouse-report.PNG) |
| My Profile | ![My Profile Page Lighthouse Report](/media/screenshots/testing/lighthouse/user-profile-lighthouse-report.PNG) |
| Update Profile | ![Update Profile Page Lighthouse Report](/media/screenshots/testing/lighthouse/update-profile-lighthouse-report.PNG) |
| Staff Panel | ![Staff Panel Page Lighthouse Report](/media/screenshots/testing/lighthouse/staff-panel-lighthouse-report.PNG) |
| Book Workout | ![Book Workout Page Lighthouse Report](/media/screenshots/testing/lighthouse/booking1-lighthouse-report.PNG) |
| Book Workout Submit| ![Book Workout Page Lighthouse Report](/media/screenshots/testing/lighthouse/booking2-lighthouse-report.PNG) |

## Tools Testing

### [Chrome DevTools](https://developer.chrome.com/docs/devtools/)

Chrome DevTools was used during the development process to test, explore and modify HTML elements and CSS styles used in the project.


### Responsiveness

* Chrome DevTools was used to test responsiveness in different screen sizes during the development process.


## Manual Testing

### Browser Compatibility

Browser | Outcome | Pass/Fail | 
--- | --- | --- |
Google Chrome | No appearance, responsiveness nor functionality issues.| <span style="color:green">Pass</span> |
Safari | No appearance, responsiveness nor functionality issues. | <span style="color:green">Pass</span> |
Mozilla Firefox | No responsiveness nor functionality issues.| <span style="color:green">Pass</span> |
Microsoft Edge | No appearance, responsiveness nor functionality issues. | <span style="color:green">Pass</span> |


### Device Compatibility

Device | Operative System |Outcome | Pass/Fail
--- | --- | --- | --- |
Dell Optiplex 7060 | Windows 11 | No appearance, responsiveness nor functionality issues. | <span style="color:green">Pass</span> |
MacBook Pro 15" | macOS Big Sur | No appearance, responsiveness nor functionality issues. | <span style="color:green">Pass</span> |
Dell Latitude 5300 | Windows 10 | No appearance, responsiveness nor functionality issues. | <span style="color:green">Pass</span> |
iPad Pro 12.9" | iOS 15 | No appearance, responsiveness nor functionality issues. | <span style="color:green">Pass</span> |
iPad Pro 10.5" | iOS 15 |No appearance, responsiveness nor functionality issues. | <span style="color:green">Pass</span> |
iPhone XR | iOS 15 |No appearance, responsiveness nor functionality issues. | <span style="color:green">Pass</span> |
iPhone 7 | iOS 15 |No appearance, responsiveness nor functionality issues. | <span style="color:green">Pass</span> |

