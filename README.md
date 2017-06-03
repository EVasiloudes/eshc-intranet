# ESHC Intranet
[ESHC Homepage](http://edinburghcoop.wordpress.com/)

[Heroku deployment](https://eshc.herokuapp.com/)

## Goal
Make usable intranet.

## Testing Instructions
**Virtualenv recommended!**
Install Python3
1. Make venv for this project
2. Activate venv
3. Install Django in venv
4. Install waliki in venv
5. Clone repo into venv directory
6. run eshcIntranet/manage.py runserver
7. Go to 127.0.0.1:8000

### New Testing Instructions
create folder

clone repo to folder

virtualenv venv

pip install -r eshcIntranet/requirements.txt in venv

uses postgresql on heroku so to mimic the heroku setup completely install postgress locally

[postgres database creation tutorial](https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04)

can also develop using SQLite (will need a different setting.py file setup to use SQLite locally and keep postgreql on heroku)

with either setup before running server migrate databse and collectstatic 

## Features implemented
* Basic user login
* Basic new user registration
* User information displayed on profile page
* Store ESHC member specific information
* Allow user to edit relevant profile information
* Basic Wiki - based on [waliki](https://github.com/mgaitan/waliki) - modified
* User management available through admin app
* Lease management - admin and user sides
* Mark Users as deactivated when they have moved out 
* 'Share received' checkbox for admins, display on user profile
* Style everything nicely (Bootstrap 3.3.0)
* Navbar
* Walik app copied to main directory 
* Wiki change history button appears in navbar

## Features wanted

### Leases app
* ~~Prompt if no valid lease registered~~
* Notify that lease will run out some months before end (via email?)
* ~~Add 'date_signed' field~~
* ~~Fill out inventory information - only allowed once~~
* Generate customised PDF ready for signing - user can print on their own
* TESTS

## Stretch features wanted
* GM help?  
  * Agenda forming?
* Extend wiki functionality
  * Side bars, no-link page list,
  * Per page comments section?
* Email verification/authentication?
* Email sending
* Automatically assign reference numbers to new users?
  * QBO integration? Maybe better to keep manual
* Proposal voting
* Calendar?
* Polling
* Flat map
* Browse bylaws - subset of wiki
* £££ Overview
* Option to change password
* mySQL? Deploy and see
* Deploy to web?

## Notes
* Uses the [waliki](https://github.com/mgaitan/waliki) app for wiki functionality. 
  * Had to modify the page creation views to use page.raw = " " instead of page.raw = "".
* Uses bootstrap v3.3.0
* If we decide to continue with Heroku, then to actually host the wiki (and any other files) we'll need S3 AWS
