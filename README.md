# Full Stack Application Development Capstone Project

[Full Stack Application Development Capstone Project
](https://www.coursera.org/learn/ibm-cloud-native-full-stack-development-capstone/home/info)

## Project requirement
A national car dealership with local branches spread across the United States recently conducted a market survey. One of the suggestions that emerged from the survey was that customers would find it beneficial if they could access a central database of dealership reviews across the country.

You are a new hire at the company. You are assigned the task of building a website that allows new and existing customers to look up different branches by state and look at customer reviews of the various branches. Customers should be able to create an account and add their review for any of the branches. The management hopes this will bring transparency to the system and also increase the trust customers have in the dealership.

After thorough research and brainstorming, the team developed use cases for anonymous, authorized, and admin users.

### Use cases for anonymous users:
- View the Contact Us page.
- View the About Us page.
- View the list of dealerships.
- Filter the list of dealerships by state:
    - Select Show all or a specific state from the State dropdown on the dealership page.
    - View all states if nothing is selected in the dropdown.
    - View a table of dealerships for the selected state when the form is submitted.
- Click on a dealership to view the reviews for that dealership on the details page with each review displayed on a bootstrap card.
- Log in using their credentials.

### Use cases for authorized users:
In addition to the above, authorized users should be able to write a review for any dealership on the dealership's page. In order to enable authorized users to write their reviews:

- A Review button should be provided against each dealer listed in the dealership table.
- Clicking on the Review button should take the user to the review page.
- Filling the form on the review page and submitting it should add the review.
```python  
{
  "user_id": 1, => from Django
  "name": "Berkly Shepley", => from Django
  "dealership": 15, => from the form
  "review": "Total grid-enabled service-desk", => form textbox
  "time": "", => current time
  "purchase": true, => form checkbox
  "purchase_date": "07/11/2020", => form calendar (bootstrap)
  "car_make": "Audi", => from django dropdown
  "car_model": "A6", => from django dropdown
  "car_year": 2010 => form django dropdown
  }
```
On submission, the user should be taken back to the dealership detail page with the submitted review featured at the top of the reviews list, sorted on time.


### Use cases for admin users:
-  Log in to the admin site with a predefined username and password.
- Add new make, model, and other attributes.
  Your organization has assigned you as the Lead Full-Stack Software Developer on this project. Your job is to develop this portal as part of your Capstone project by following best practices for Full-Stack software development.
## Course resource
7 modules

# Module 1: Create static page About us, Contact us
The Django app will be mainly used for user management and authentication, managing car models and makes, and routing other MongoDB services for dealership and customer reviews. You will build this Django app and related services in a phased manner along the capstone course.

In this module, you are asked to perform the following tasks:

- Fork the GitHub repo containing the project template.
- Clone your forked repository.
- Run the Django app on the development server.
- Add a navigation to the website using Bootstrap.
- Add an "About Us" static page.
- Add a "Contact Us" static page.
  Follow the instructional Skill Network lab to complete the above tasks step by step.

## Step 1: Clone and ckeck the main app running
As part of the project, your first task is to run and test its main Django application. You are given a skeleton of the Django application as a starting point.

### Fork and Clone the repository
- Navigate to this [repo](https://github.com/ibm-developer-skills-network/xrwvm-fullstack_developer_capstone): link and create a fork of the repository that includes essential starter code required for this project.

- Go to your forked repository.

- Copy the git clone URL of the skeleton repository that you forked into your account.

### Run the Django app on development server

# Reference