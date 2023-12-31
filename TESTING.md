# GenStar Fitness Testing

[Back to the README.md file](https://github.com/GenaGrig/genstar-fitness/blob/main/README.md)  

[View the live website here](https://genstar-fitness-and-gym-0d51dc3aa6d0.herokuapp.com/)  

## Table of Contents

1. [Testing User Stories](#testing-user-stories)
2. [Code Validation](#code-validation)
3. [Accessibility](#accessibility)
4. [Tools Testing](#tools-testing)
5. [Manual Testing](#manual-testing)

# Testing User Stories

### As a Site User, I can navigate on web site easily so that I can find necessary information and links fast

* Easy understandable navigation bar was made with descriptive links
* Separate navigation bar was made for profile view containing only necessary links for booking and checking profile

### As a Site User, I can create account so that I can login and book workout, see all my passes and edit or delete them

* Registration form was updated for easy understanding and hints below each field
* After registration user is redirected to profile page, where user can book workout and have all the CRUD features

### As a Site User, I can find information about memberships so that I can choose one that suits me best

* Membership page contains all the necessary information about available memberships and its preferences
* Right now "Buy membership" button does not work, because payment system cannot be implemented at this stage

### As a Site User, I can login to my account so that I can book/view/edit or delete workout or personal training

* CRUD functionality was implemented to give user ability to create booking, see all booked passes, edit and delete them

### As a Site User, I can see all available workouts so that I can choose that one that suits me best!

* Workout page was made to list all available workouts to choose from
* Each workout has a little photo and description for understanding what it is about

### As a Site User, I can see what preferences gives personal trainer so that I can understand how he can help me with my goals

* Personal trainer is extra feature that gives help to users who are new to a fitness club or workouts
* Contact form is added for users to contact personal trainers with personal questions and advices

### As a Site User, I can see clubs contact information so that I can visit or contact them

* All contact information is available at contact page
* Google Maps API was embedded on page to show location of fitness club
* Contact form is added to provide users possibility to contact club reception with different questions

### As a Site User, I can get a confirmation modal about deleting my booking so that I cannot to delete my booking accidentally

* Extra feature as delete workout confirmation modal was implemented to secure that user will not delete workout accidentally
* Same feature was added for staff members on staff panel for the same reason 

### As a Site User, I want to see my user panel so that I can see advanced information and booked workouts

* User panel contains general information about user, such as first and last name, user name and email address
* Below the user panel "My bookings" part contains all bookings made by user with buttons to edit or delete them

### As a Site Admin or Staff member, I can use Staff panel so that I can see all bookings made by users

* Staff panel is available only for staff members and admins
* Staff panel contains all bookings made by all users

### As a Staff member, I can use search panel so that I can sort out only one type of workout and see all bookings for it

* Staff panel contains Search panel that can filter workouts by different values, every value is searchable

### As a Site User, I can have all CRUD functionality so that I can create, see, edit and delete my bookings

* Registered site users has access to CRUD functionality on their Profile page
* Booking can be added, seen in My Booking, edited and deleted in appropriate row with help of related icons

[Back to top ⇧](#genstar-fitness-testing)

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

There are four CSS files in my project, main is style.css, containing all general styling for the project and overriding most of Bootstrap default CSS. Booking.css, membership.css and workout.css were made to override default Bootstrap CSS in specific files, as there were problem with CSS override when adding to main style.css file. No attempts to join all CSS files in one were successful, as design broke and only discard of changes helped to restore it. 

There are no repetitions, comment out or double code across all css files.

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

[Back to top ⇧](#genstar-fitness-testing)

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

[Back to top ⇧](#genstar-fitness-testing)

# Tools Testing

### [Chrome DevTools](https://developer.chrome.com/docs/devtools/)

Chrome DevTools was used during the development process to test, explore and modify HTML elements and CSS styles used in the project.


### Responsiveness

* Chrome DevTools was used to test responsiveness in different screen sizes during the development process.


## Manual Testing

### Browser Compatibility

Browser | Outcome | Pass/Fail | 
--- | --- | --- |
Google Chrome | No appearance, responsiveness nor functionality issues.| <span style="color:green">Pass</span> |
Opera | No appearance, responsiveness nor functionality issues. | <span style="color:green">Pass</span> |
Mozilla Firefox | No appearance, responsiveness nor functionality issues.| <span style="color:green">Pass</span> |
Microsoft Edge | No appearance, responsiveness nor functionality issues. | <span style="color:green">Pass</span> |


### Device Compatibility

Device | Operative System |Outcome | Pass/Fail
--- | --- | --- | --- |
MSI Katana 15.6" | Windows 11 | No appearance, responsiveness nor functionality issues. | <span style="color:green">Pass</span> |
Asus Rog Strix Desktop 27" | Windows 10 | No appearance, responsiveness nor functionality issues. | <span style="color:green">Pass</span> |
Lenovo Pad | Android | No appearance, responsiveness nor functionality issues. | <span style="color:green">Pass</span> |
Samsung S21 6.2" | Android |No appearance, responsiveness nor functionality issues. | <span style="color:green">Pass</span> |
Nokia S7 Plus 6.0" | Android |No appearance, responsiveness nor functionality issues. | <span style="color:green">Pass</span> |

### Test results

#### General

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=32>Navigation Bar</td>
        <td rowspan=2>Main logo link</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the link redirects to the Home page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=2>Home link</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the link redirects to the Home page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Membership link</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the link redirects to the Membership page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Workouts link</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the link redirects to the Workouts page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
     <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>PT link</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the link redirects to the PT page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Contact Us link</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the link redirects to the Contact page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
        <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Terms of Use dropdown menu</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the link opens dropdown menu with two links - Terms and Conditions and Privacy Policy.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Terms and Conditions link</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the link opens Terms and Conditions page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Privacy Policy</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the link opens Privacy Policy page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Register link</td>
        <td rowspan=2>Unregistered</td>
        <td>Functionality</td>
        <td>Clicking the link redirects to the Register page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Login link</td>
        <td rowspan=2>Unregistered</td>
        <td>Functionality</td>
        <td>Clicking the link redirects to the Sign In page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Book Workout link</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Clicking the link redirects to the Book Workout page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>User Profile link</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Clicking the link redirects to the User Profile page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Staff panel link</td>
        <td rowspan=2>Admins or stagg members</td>
        <td>Functionality</td>
        <td>Clicking the link redirects to the Staff Panel page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Logout link</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Clicking the link redirects to the Sign Out page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Hamburger Menu button </td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the button toggle navigation menu.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Responsive navigation menu on smaller screens.<br>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=10>Footer</td>
        <td rowspan=2>Email link</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the Email link opens email sending program.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td><span>N/A</span></td>
    </tr>
    <tr>
        <td rowspan=2>Facebook icon</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the link open Facebook page on a separate tab.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td><span>N/A</span></td>
    </tr>
    <tr>
        <td rowspan=2>Instagram icon</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the link open Instagram page on a separate tab.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td><span>N/A</span></td>
    </tr>
    <tr>
        <td rowspan=2>Twitter icon</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the link open Twitter page on a separate tab.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td><span>N/A</span></td>
    </tr>
</table>

#### Home page

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=2>Carousel</td>
        <td rowspan=2>Left/Right scroll buttons</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the Left/Rights scroll button slides images.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
</table>

#### Membership page

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=2>Membership button</td>
        <td rowspan=2>Buy membership buttons</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the Buy membership button redirect user to Contact Us page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Bootstrap button CSS</td>
        <td>Pass</td>
    </tr>
</table>

#### Workouts page

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=2>Accordion</td>
        <td rowspan=2>Accordion slides</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking each accordion slide should open its content and close previous.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>General styling</td>
        <td>Pass</td>
    </tr>
</table>

#### Personal Trainer page

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=10>Contact form</td>
        <td rowspan=2>Name input</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Text can be entered in the field.<br>Field is required and validates input.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Focus effect working as expected.</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td rowspan=2>Email input</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Text can be entered in the field.<br>Field is required and validates input text as email.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Focus effect working as expected.</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td rowspan=2>Select subject</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Text can be entered in the field.<br>Field is optional and no subject can be chosen.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=2>Message</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Text can be entered in the field.<br>Field is required and validates input.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Focus effect working as expected.</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td rowspan=2>Send button</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the button submits this form and shows returned form data from CI to confirm that form works and submits data to back-end.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Bootstrap button CSS</td>
        <td>Pass</td>
    </tr>
</table>

#### Contact Us page

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=2>Google maps API</td>
        <td rowspan=2>Google maps</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Google maps embedded to page and shows map with chosen location.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Responsive design on all screen sizes.</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td rowspan=10>Contact form</td>
        <td rowspan=2>Name input</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Text can be entered in the field.<br>Field is required and validates input.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Focus effect working as expected.</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td rowspan=2>Email input</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Text can be entered in the field.<br>Field is required and validates input text as email.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Focus effect working as expected.</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td rowspan=2>Select subject</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Text can be entered in the field.<br>Field is optional and no subject can be chosen.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=2>Message</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Text can be entered in the field.<br>Field is required and validates input.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Focus effect working as expected.</td>
        <td>Pass</td>
    </tr>
    <tr>
        <td rowspan=2>Submit button</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the button submits this form and shows returned form data from CI to confirm that form works and submits data to back-end</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Bootstrap button CSS</td>
        <td>Pass</td>
    </tr>
</table>

#### Register Page

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=10>Register New Account</td>
        <td rowspan=2>Username input</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Text can be entered in the field.<br>Field validates input to be present.<br>Display message if the username already exists.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Focus effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>E-mail input</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Text can be entered in the field.<br>Field validates input to be present.<br>Validate input is an email address.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Focus effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Password input</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Text can be entered in the field.<br>Field validates input to be present.<br>Validate input is a valid password.<br>Display message if password is not valid.<br>Display message if both passwords are not equal.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Focus effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Password Repeat input</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Text can be entered in the field.<br>Field validates input to be present.<br>Validate input is a valid password<br>Display message if password is not valid<br>Display message if both passwords are not equal</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Focus effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Sign Up button</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the button submit the form and redirects to the User Profile page.<br>Create user if form is valid.<br>Display message if user is successfully created.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
</table>


#### Login Page

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=6>Sign In Form</td>
        <td rowspan=2>Username input</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
         <td>Text can be entered in the field.<br>Field validates input to be present.<br>Display message if the user name and/or password are not correct.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Focus effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Password input</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Text can be entered in the field.<br>Field validates input to be present.<br>Display message if the user name and/or password are not correct.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Focus effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Sign In button</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the button authenticates the user and redirect to the User Profile page.<br>Display message if credentials are not valid.<br>Display message if user login successfully.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
</table>


#### Logout Page

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=2>Sign Out Page</td>
        <td rowspan=2>Sign Out button</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Clicking the button sign out the user and redirect to the Home page.<br>Display message if user logout successfully.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
</table>

#### User Profile page

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=8>Page Buttons</td>
        <td rowspan=2>Edit Profile button</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Clicking Edit Profile button redirects to Edit Profile page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Book Workout button</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Clicking Book Workout button redirects to Book Workout page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
     <tr>
        <td rowspan=2>Edit Workout icon/button</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Clicking Edit Workout button redirects to Edit Workout page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=2>Delete Workout icon/button</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Clicking Delete Workout button opens confirmation modal.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=4>Delete confirmation modal</td>
        <td rowspan=2>Cancel button</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Clicking Cancel button cancels deleting of workout and closes modal.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Delete button</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Clicking Delete workout button delete selected workout and closes the modal.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
</table>

#### Update Profile Page

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=10>Update Profile Form</td>
        <td rowspan=2>First name input</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Text can be entered in the field.<br>Optional field. Allows to be left empty.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=2>Last name input</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Text can be entered in the field.<br>Optional field. Allows to be left empty.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=2>Username input</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Text can be entered in the field.<br>Field validates input to be present.<br>Validate input is a valid username.<br>Display message if username is not valid.<br></td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Focus effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>E-mail input</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Text can be entered in the field.<br>Optional field. Allows to be left empty.<br>Validate input is an email address.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=2>Update Profile button</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Clicking the button submit the form and redirects to the User Profile page.<br>Updates user profile info if form is valid.<br>Display message if user profile is successfully updated.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
</table>

#### Staff Panel page

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=2>Search Bar</td>
        <td rowspan=2>Input field</td>
        <td rowspan=2>Admins or staff members</td>
        <td>Functionality</td>
        <td>Placeholder "Search Booking" shows as expected.<br>Text can be entered in the field.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=2>Delete icon/button</td>
        <td rowspan=2>Delete Workout icon/button</td>
        <td rowspan=2>Admins or staff members</td>
        <td>Functionality</td>
        <td>Clicking Delete Workout button opens confirmation modal.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=4>Delete confirmation modal</td>
        <td rowspan=2>Cancel button</td>
        <td rowspan=2>Admins or staff members</td>
        <td>Functionality</td>
        <td>Clicking Cancel button cancels deleting of workout and closes modal.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Delete button</td>
        <td rowspan=2>Admins or staff members</td>
        <td>Functionality</td>
        <td>Clicking Delete workout button delete selected workout and closes the modal.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
</table>

#### Book Workout page

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=4>Select element</td>
        <td rowspan=2>Workout selector</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking on "Select Workout" selector all bookable workouts shows up.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=2>Date selector</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking on "Select Date" selector, Datepicker calender shows up.<br>Placeholder "Select Date" shows as expected.<br>Field validates input to be present.<br>Display message if date is not valid.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Custom CSS</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=4>Online Booking page buttons</td>
        <td rowspan=2>Continue button</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Clicking the button redirects user to Booking submit page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Back button</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Clicking the Back button cancels the booking process and redirects user to User Profile page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
</table>

#### Book Workout Submit page

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=2>Select element</td>
        <td rowspan=2>Time selector</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking on "Time" selector all bookable times shows up.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=4>Online Booking page buttons</td>
        <td rowspan=2>Book Workout button</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Clicking the button saves the booking and redirects user to User Profile page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Back button</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Clicking the Back button redirects user to previous Booking workout page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
</table>

[Back to top ⇧](#genstar-fitness-testing)