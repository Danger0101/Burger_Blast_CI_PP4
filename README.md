# Burger Blast

Welcome to Burger Blast, where flavor meets delight! We're a culinary haven dedicated to crafting unforgettable experiences through sensational bites and impeccable service.

---

## User Stories

-

## Features

### Navbar

![]()

- ***

### Index

- The index page for Burger Blast provides users with essential information about the restaurant, such as its name, slogan, and opening hours. It welcomes visitors to the restaurant, highlighting its commitment to delivering delightful flavors and memorable experiences through its food and service. Users can quickly find the restaurant's operating hours, ensuring they know when they can visit. Additionally, the page encourages users to embark on a flavorful journey with Burger Blast, promising a satisfying dining experience that will leave them happy. Overall, the index page serves as a welcoming introduction to Burger Blast, enticing users to explore further and consider visiting the restaurant for a tasty adventure.

![]()

---

### About US

- It provides users with an engaging overview of the restaurant's ethos, cuisine, and dining experience. Through vibrant language and enticing imagery, it aims to create an immersive experience for the user, inviting them to explore the restaurant's offerings and join its culinary journey. The page is structured into sections, each highlighting different aspects such as the restaurant's philosophy, menu offerings, commitment to quality, culinary expertise, customer service, community engagement, and the overall dining adventure awaiting the visitors. It serves to inform and entice potential customers, giving them a glimpse into what makes Burger Blast unique and why they should consider dining there.

![]()

---

### Signup

- Allows Users to signup for an account using providing username, first name, last name, email, and password with a validation method provided by django.

![]()

---

### Sign In

- Allows Users to sign into their accounts using username and password.

![]()

---

### Change Details

- Alows users to change their account details or password.

![]()

---

### My Reservations

- The "My Reservations" page is where users can view all their bookings in one place. It displays essential details like confirmation number, reservation date and time, party size, and any special requests made during the booking process. Users can also perform actions such as deleting or editing their reservations. If there are no reservations found, a message indicating so will be shown. Additionally, users have the option to make a new reservation directly from this page. Overall, it's a convenient hub for managing and keeping track of reservations. Staff can view and edit all reservations as well sa see slightly more information like name and user.

![]()

---

### Make Reservations

- The "Make Reservations" page is where you can easily reserve a spot or book a service. It's designed to be user-friendly, with a simple form for you to fill out. You'll find fields asking for necessary information, such as your name, contact details, and the specifics of what you're booking. Once you've filled out the form, just hit the "Submit Reservation" button, and your reservation will be confirmed. It's a convenient way to secure your spot without any hassle.

![]()

---

### Edit Reservations

- The "Edit Reservations" page allows you to make changes to your existing reservations. If you need to update your booking details, such as the date, time, or any other specifics, you can do so easily on this page. It's designed to be user-friendly, similar to the reservation form, with a straightforward interface for you to modify your information. Once you've made the necessary edits, simply save your changes, and your reservation will be updated accordingly. It's a convenient way to ensure that your booking reflects any adjustments you need to make.

![]()

---

### Menu

- The menu page is a part of a website where you can explore the different food options available. It's designed to make it easy for you to find what you're looking for by organizing the menu into categories like sides, entrees, and desserts. Each category has its own section that you can navigate to by clicking on buttons. When you click on a category, it shows you all the items available in that category. Each item is displayed with a name, a description, price, calories, allergens, and preparation time. This layout helps you quickly browse through the menu and decide what you want to order based on your preferences.

![]()

---

### footer

- Provides contact information for Meaningful Careers
- Has links to the relevant social media accounts

![Image of footer](assets/images/meaningfulcareersreadmeimg/footer.png)

---

### Django Admin

- Django admin is a powerful tool designed to make managing a website easier for staff members. It provides a user-friendly interface where staff can easily add, edit, or delete content without needing technical skills. Staff members can log in and access a dashboard that gives them control over various aspects of the website, such as managing user accounts, updating product listings, posting articles, and more. The admin panel organizes information neatly, allowing staff to navigate through different sections effortlessly. It's like having a control center for the website, making it simple for staff members to keep everything running smoothly and up-to-date.

![]()

---

## Testing

|                                                         What test was completed                                                         | Passed? Y(yes)/N(no) |           Other information           |
| :-------------------------------------------------------------------------------------------------------------------------------------: | :------------------: | :-----------------------------------: |
|                                                       Make a super user (Manager)                                                       |          Y           |                                       |
|                                                         Make a staff member ()                                                          |          N           |                                       |
|                                        Sign up as a customer/user (Jane.Doe, John.Doe, Jon.Doe)                                         |          Y           |                                       |
|                                                      Login to site as a superuser                                                       |          Y           |                                       |
|                                                        Login to site as a staff                                                         |          N           |                                       |
|                                                    Login to site as a customer/user                                                     |          Y           |                                       |
|                                                     Log out of site as a superuser                                                      |          Y           |                                       |
|                                                       Log out of site as a staff                                                        |          N           |                                       |
|                                                   Log out of site as a customer/user                                                    |          Y           |                                       |
|                                                 Login to Django admin as customer/user                                                  |          Y           |  Only staff can log in successfully   |
|                                                   Login to Django admin as superuser                                                    |          Y           |  Only staff can log in successfully   |
|                                                     Login to Django admin as staff                                                      |          Y           |  Only staff can log in successfully   |
|                                                  Log out of Django admin as superuser                                                   |          Y           |                                       |
|                                                    Log out of Django admin as staff                                                     |          Y           |                                       |
|                                             Successfully change any users data on main site                                             |          Y           |                                       |
|                                            Successfully change any users data on admin site                                             |          Y           |  Can only be done as a satff member   |
|                                                   Make reservation as a customer/user                                                   |          Y           |                                       |
|                                                     Make reservation as a superuser                                                     |          Y           |                                       |
|                                                        Make reservation as staff                                                        |          Y           |                                       |
|                                                   Edit reservation as a customer/user                                                   |          Y           |                                       |
|                                                     Edit reservation as a superuser                                                     |          Y           |                                       |
|                                                        Edit reservation as staff                                                        |          Y           |                                       |
|                                                  Delete reservation as a customer/user                                                  |          Y           |                                       |
|                                                    Delete reservation as a superuser                                                    |          Y           |                                       |
|                                                       Delete reservation as staff                                                       |          Y           |                                       |
|                                              Edit reservation as a superuser on admin site                                              |          Y           |                                       |
|                                                 Edit reservation as staff on admin site                                                 |          Y           |                                       |
|                                             Delete reservation as a superuser on admin site                                             |          Y           |                                       |
|                                                Delete reservation as staff on admin site                                                |          Y           |                                       |
| Check vanila validation setting to see if a typical user can make a reservation out side of normal constraints with out nefarious means |          Y           | Unable to book outside of constraints |
|                                                                                                                                         |                      |                                       |

### Bugs/Issues Encountered

|                                                 Bugs/Issues Encountered                                                 |                                                                                                How problem was fixed                                                                                                | Fixed Y(yes)/N(no) |
| :---------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :----------------: |
| Allowing customers/users to sign up for an account with an email verification system as emails wern't sending correctly |                                                                                  Removed the verification prior to making it live                                                                                   |         Y          |
|                                       Getting images to load into the menu items                                        |                                                                                Removed due to time constraint may add back in future                                                                                |         Y          |
|                                        Getting static files to work as intended                                         |                                                  A few varriations of code to find one that worked best for my needs had 2 locations stores brought it down to one                                                  |         Y          |
|                                    Getting static file js to load for menu selection                                    |                                                                                added it in script tags instead as its a small script                                                                                |         Y          |
|                      Users could set any date or time in making reservation whether future or past                      | Added js and python with validation checks in place ti ensure users can only book during opening hours and up to two hours prior to close with up to two weeks in advance possible. Same day is not possible online |         Y          |

---

## Validation Testing

### Python

All Scripts checked with [PEP8 Code institute](https://pep8ci.herokuapp.com/)

| **File** | **Line** | **Errors or Warnings** |
| :------: | :------: | :--------------------: |
|          |          |                        |

### CSS

-checked with [W3 CSS Validator](https://jigsaw.w3.org/css-validator/) completed with no issues found.

![]()

### HTML

- checked with [W3 HTML Validator](https://validator.w3.org/) on all pages with no errors or warnings.

![W3 HTML Validation Image](assets/images/meaningfulcareersreadmeimg/w3htmlvalidation.png)

### Contrast

- Checked all pages with [A11Y contrast checker](https://color.a11y.com/) Cameback with no issues.

![Contrast checker Image]()

### Index

**Chrome lighthouse desktop**

![Screencap index lighthouse desktop](./staticfiles/images/burger_blast_lighthouse/Index_lh_desktop.png)

**Chrome mobile lighthouse**

![Screencap index lighthouse mobile](./staticfiles/images/burger_blast_lighthouse/Index_lh_mobile.png)

### About

**Chrome lighthouse desktop**

![Screencap about lighthouse desktop](./staticfiles/images/burger_blast_lighthouse/aboutus_lh_desktop.png)

**Chrome mobile lighthouse**

![Screencap about lighthouse mobile](./staticfiles/images/burger_blast_lighthouse/aboutus_lh_mobile.png)

### Admin

**Admin Login Chrome lighthouse desktop**

![Screencap index.html lighthouse desktop](./staticfiles/images/burger_blast_lighthouse/admin_signin_lh_desktop.png)

**Admin Login Chrome mobile lighthouse**

![Screencap index.html lighthouse mobile](./staticfiles/images/burger_blast_lighthouse/admin_signin_lh_mobile.png)

**Admin Pannel Chrome lighthouse desktop**

![Screencap index.html lighthouse desktop](./staticfiles/images/burger_blast_lighthouse/admin_lh_desktop.png)

**Admin Pannel Chrome mobile lighthouse**

![Screencap index.html lighthouse mobile](./staticfiles/images/burger_blast_lighthouse/admin_lh_mobile.png)

### Reservations

**Edit Reservation Chrome lighthouse desktop**

![Screencap about lighthouse desktop](./staticfiles/images/burger_blast_lighthouse/edit_reservations_lh_desktop.png)

**Edit Reservation Chrome mobile lighthouse**

![Screencap about lighthouse mobile](./staticfiles/images/burger_blast_lighthouse/edit_reservations_lh_mobile.png)

**Make Reservation Chrome lighthouse desktop**

![Screencap about lighthouse desktop](./staticfiles/images/burger_blast_lighthouse/make_reservations_lh_desktop.png)

**Make Reservation Chrome mobile lighthouse**

![Screencap about lighthouse mobile](./staticfiles/images/burger_blast_lighthouse/make_reservations_lh_mobile.png)

**My Reservation Chrome lighthouse desktop**

![Screencap about lighthouse desktop](./staticfiles/images/burger_blast_lighthouse/my_reservations_lh_desktop.png)

**My Reservation Chrome mobile lighthouse**

![Screencap about lighthouse mobile](./staticfiles/images/burger_blast_lighthouse/my_reservations_lh_mobile.png)

### Menu

**Chrome lighthouse desktop**

![Screencap about lighthouse desktop](./staticfiles/images/burger_blast_lighthouse/menu_lh_desktop.png)

**Chrome mobile lighthouse**

![Screencap about lighthouse mobile](./staticfiles/images/burger_blast_lighthouse/menu_lh_mobile.png)

### Signup

**Chrome lighthouse desktop**

![Screencap about lighthouse desktop](./staticfiles/images/burger_blast_lighthouse/signup_lh_desktop.png)

**Chrome mobile lighthouse**

![Screencap about lighthouse mobile](./staticfiles/images/burger_blast_lighthouse/signup_lh_mobile.png)

### Sign In

**Chrome lighthouse desktop**

![Screencap about lighthouse desktop](./staticfiles/images/burger_blast_lighthouse/signin_lh_desktop.png)

**Chrome mobile lighthouse**

![Screencap about lighthouse mobile](./staticfiles/images/burger_blast_lighthouse/signin_lh_mobile.png)

### Change Details

**Chrome lighthouse desktop**

![Screencap about lighthouse desktop](./staticfiles/images/burger_blast_lighthouse/update_details_lh_desktop.png)

**Chrome mobile lighthouse**

![Screencap about lighthouse mobile](./staticfiles/images/burger_blast_lighthouse/update_details_lh_mobile.png)

---

### Database

![Data Base Visiualization](./staticfiles/images/)

- I was able to make this using [django-extensions](https://pypi.org/project/django-extensions/) and [graphviz](https://django-extensions.readthedocs.io/en/latest/graph_models.html)

---

## Deployment

Used Heroku to deploy the website. You can [Visit Live Site by clicking here](https://burger-blast-ci-2024-63403f4a3896.herokuapp.com/)

### How to deploy to heroku:

1. **Run Migrations:** Once your project is deployed, you'll need to run any pending database migrations. You can do this using Heroku's web-based console or by running commands in your local terminal.
2. **Create a Superuser:** If your project uses Django's admin interface, you may want to create a superuser account on Heroku. You can do this by accessing your app's shell through the Heroku dashboard and running the createsuperuser command.
3. **Create a Heroku Account:** If you haven't already, sign up for a Heroku account at heroku.com.
4. **Prepare Your Django Project:** Ensure your Django project is properly configured for deployment. This includes setting up a requirements.txt file listing all dependencies and a Procfile specifying the command to start your application.
5. **Install Gunicorn:** Gunicorn is a WSGI HTTP server for Python. You'll need to install it via pip: "pip install gunicorn"
6. **Create a Procfile:** In the root directory of your project, create a file named Procfile (without any file extension) and add the following line: web: "web: gunicorn burger_blast.wsgi:application"
7. **Update Django Settings:** Ensure your Django settings.py file is configured to work in a production environment. This includes setting DEBUG = False and adding Heroku's domain to the ALLOWED_HOSTS list.
8. **Create a requirements.txt File:** Generate a requirements.txt file listing all Python dependencies your project needs. You can create it by running: "pip freeze > requirements.txt"
9. **Create a Heroku App:** Go to the Heroku dashboard and create a new app. Choose a unique name for your app.
10. **Link GitHub Repo:** Under deploy tab in the settings link your GitHub repository.
11. **Set Up Environment Variables:** Now under settings tab set any necessary environment variables for this django project. See chart below for needed key and values.

**Heroku Cofig Variables**
| Key | Value |
|:---:|:-----:|
| DISABLE_COLLECTSTATIC | 1 |
| CLOUDINARY_API_KEY | Api key value |
| CLOUDINARY_API_SECRET | Api secret value |
| CLOUDINARY_CLOUD_NAME | Cloudinary Name |
| DATABASE_URL | postgres database url |
| DJANGO_SECRET_KEY | Django secret key for the project |
| SENDGRID_API_KEY | sendgrid api key |

12. **Deploy Your Project:** Back under deploy tab on Heroku scroll down to manual deploy and choose the branch you wish to deploy and hit button "Deploy Branch" wait for the success and trouble shoot if needed.

## Technology used

- HTML
- CSS
- Fontawesome
- Google Fonts
- Visual Studios Code (VSCode)
- Github
- Git
- Gyzo
- Github Desktop App
- Cloudinary
- Python
- Django
- Django-extensions
- fotor (AI Image generator)

## Wireframes

### Admin Page

- Ended up going with a pre built one from ![django-admin-interface](https://pypi.org/project/django-admin-interface/0.6.0/) "pip install django-admin-interface"

![Image for admin page wireframe](staticfiles/images/wireframes/admin_page.png)

### Landing Page

![Image for admin page wireframe](staticfiles/images/wireframes/landing_page.png)

### Menu

![Image for admin page wireframe](staticfiles/images/wireframes/menu_page.png)

### Make/Edit Reservations

![Image for admin page wireframe](staticfiles/images/wireframes/reservation_and_edit_reservastion_page.png)

## Credits

**Images**

![websitebackground Actual Image](./staticfiles/images/background_burger_two.jpg)

- Website Background Image by [fotor:](https://www.fotor.com/)

**More Credits**

- My wife who’s been supper supportive of this change in career for me and just being out right amazing we will get her into this one way or another I am sure.

- Code Institute for providing an excellent accelerated learning platform worth every penny.

---

## Future feature ideas

|                                Feature Idea                                 |                    Why Not Implimented                    |
| :-------------------------------------------------------------------------: | :-------------------------------------------------------: |
|                       Email confirmation intigration                        | Was giving odd complication and was hindering development |
|     Contact us page that emails the restaraunt when a form is submited      |                 Low on time to impliment                  |
| Reviews page for users to leave a review or edit theirs using a star rating |                  Low on time to complete                  |
