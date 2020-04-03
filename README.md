#  Awards App.
This is a web app that allows users to post their projects and have them voted for.

##  Getting Started

###  Prerequisites and Installing
You need to install the following software to have the app running on your local machine for development and testing purposes. Instructions on how to install will also be provided next to the software.


|Software|Installation Instructions/Terminal Commands|
|----------|---------------------------|
|Python3.6|1. sudo apt-get update|
|  |         2. sudo apt-get install python3.6|
|Virtual Environment|1. pip install pipenv|
|   |2. Activate by running: pipenv shell|
|Django 3.0|pipenv install Django|
|psycopg2|pipenv install psycopg2|
|dj-database-url|pipenv install dj-database-url|
|django-cors-headers|pipenv install django-cors-headers|
|gunicorn|pipenv install gunicorn|
|python-decouple|pipenv install python-decouple|
|django rest framework|pipenv install djangorestframework|


###  Running Tests
The test classes are divided into ProjectTestCase, ProfileTestCase and RateTestCase.

Once you get the development server running, run the following command:
`python3 manage.py test` which runs all the test cases one by one.

Examples of tests are given below.

####  ProjectTestCase

      def test_project_creation(self):
         project = self.create_project()
         self.assertTrue(isinstance(project, Project))
         self.assertEqual(project.__str__(), project.title)

The test above tests if a project was created successfully.

      def test_save_project(self):
        self.new_user.save()
        self.new_project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects)>0)

The test above tests if a project was saved successfully.

      def test_delete_project(self):
        self.new_user.save()
        self.new_project.save_project()
        self.new_project.delete_project()
        project = Project.objects.filter(id=1).delete()

The test above tests if a project was deleted successfully.

    def test_update_project(self):
        self.new_user.save()
        self.new_project.save_project()
        self.new_project.update_project(link='Just a link update', description='Just a description update', title='Just a title update')
        self.assertTrue(self.new_project.link == 'Just a link update')
        self.assertTrue(self.new_project.description == 'Just a description update')
        self.assertTrue(self.new_project.title == 'Just a title update')

The test above tests if a project was deleted successfully.


####  ProfileTestCase

      def test_profile_creation(self):
        profile = self.create_profile()
        self.assertTrue(isinstance(profile, Profile))
        self.assertEqual(profile.__str__(), profile.contact)

The test above tests if a profile was created successfully.
        
    def test_save_profile(self):
        self.new_user.save()
        self.new_profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)

The test above tests if a profile was saved successfully.
        
    def test_delete_profile(self):
        self.new_user.save()
        self.new_profile.save_profile()
        self.new_profile.delete_profile()
        profile = Profile.objects.filter(id=1).delete()

The test above tests if a profile was deleted successfully.
        
    def test_update_profile(self):
        self.new_user.save()
        self.new_profile.save_profile()
        self.new_profile.update_profile(contact='Just a contact update', bio='Just a bio update', profile_pic='/path/example2.png')
        self.assertTrue(self.new_profile.contact == 'Just a contact update')
        self.assertTrue(self.new_profile.bio == 'Just a bio update')
        self.assertTrue(self.new_profile.profile_pic == '/path/example2.png')

The test above tests if a profile was updated successfully.


####  RateTestCase

       def test_save_rate(self): 
        self.new_user.save()
        self.new_project.save_project()
        self.new_rate.save_rate()
        rates = Rate.objects.all()
        self.assertTrue(len(rates)>0)

The test above tests if a rating was saved successfully.
        
      def test_delete_rate(self):
        self.new_user.save()
        self.new_project.save_project()
        self.new_rate.save_rate()
        self.new_rate.delete_rate()
        rate = Rate.objects.filter(id=1).delete()

The test above tests if a rating was deleted successfully.

      def test_update_rate(self):
        self.new_user.save()
        self.new_project.save_project()
        self.new_rate.save_rate()
        self.new_rate.update_rate(content=10, design=10, usability=10)
        self.assertTrue(self.new_rate.content == 10)
        self.assertTrue(self.new_rate.usability == 10)
        self.assertTrue(self.new_rate.design == 10)

The test above tests if a rating was updated successfully.


##  Deployment

Follow along with this document (https://gist.github.com/newtonkiragu/42f2500e56d9c2375a087233587eddd0) to deploy your application to Heroku.

##  Built With

*  [Django] - 3.0 (https://docs.djangoproject.com/en/3.0/)


##  Contributing


Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

##  Versioning


##  Authors

* **Wendy Munyasi**


##  License

This project is licensed under the MIT License.


## DB Diagram

<img src="db.png">

## Api Link and description

(https://awardss-api.herokuapp.com/)

On loading the link above, a 404 page is displayed with the various urls.
Select any and login with the credentials provided if asked to do so. Though I advice against using this route.

An alternative is to use **Postman** to access the api routes as the token identifier is provided directly.

## Project-Setup Instructions.

1.Open your github account and search for github username: **wendymunyasi**

1. git clone using the following links.

   link: https://github.com/wendymunyasi/awards.git

2. For Django app, set the database to your own url then run `python3 manage.py makemigrations` and `python3 manage.py migrate`.
3. Run the command `python3 manage.py runserver`.
4. Click the local host link on your terminal  and navigate to the api root. Use the credentials provided to login if asked to do so.


## BDD

| Behaviour | Input | Output |
| --------- | ------| ------ |
|On loading the app you see the landing page with login up form with a register link at the bottom of the form.| Clicking `sign up`.| You are redirected to a page where you enter your details and sign up then redirected to the login page.|
|Enter your username and password on the login page.| Clicking `login`. |You are redirected to a page where all the projects are visible.|
|Clicking any project's landing_page.|Mouse click.|You are redirected to a page showing just the project you clicked.|
|Clicking `RATE PROJECT` button.|Mouse click.|You are redirected to a page with a from where you fill your ratings under **content**, **design** and **usability** in the range of 1 to 10. |
|Clicking `VISIT SITE` button.|Mouse click.|You are redirected to the project's website.|
|Clicking the `New Project` link on the navbar. | Mouse click. |You are redirected to a page where you enter the details of your project then post.|
|Clicking the `Profile` link on the navbar.| Mouse click. | You are redirected to a page where you can view your profile or create your profile if you didn't have any.|
|||


## CODEBEAT


## The following include the list of technologies used:

**Python3.6**
**Django 3**
**Bootstrap**
**PostgreSQL**
**Django Rest Framework**

## Known Bugs

The UI isn't as user friendly.

## Collaborate

To colloborate, reach me through my email address wendymunyasi@gmail.com

