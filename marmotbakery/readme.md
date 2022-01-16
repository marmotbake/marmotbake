# Marmot Bakery
## Final Project Harvard CS5oW

###### Author: Dr. Delyan Malchev, 19.12.2021

### Scope & Motivation

I started this course in order to be able to build a web page for my wife's passion - hand made sourdough bread. She is starting her own home based bakery with a capacity of only 10 loafs per day. The purpose of this project is to give her and her potential customers a tool to manage orders, organise tasks, and keep track on statistics.

### Distinctiveness and Complexity

As I started the course I had no idea that there was a pizza project. I acknowledge that I have never looked at the files of that project, nor have I looked for solutions on the internet or elsewhere. Furthermore I have done carefull analysis of the requirements and done my best to distinguish my work from this project. Even a bakery might be similar to a pizza shop, the real similarity is due to the fact that we are targeting a CRUD operations app, and in fact all such apps will always have that in common. 

My app is a real project for real business and incorporates all neccessary bits that the bakery owner needs. The app realizes the business logic and limitations in the bread ordering process, has a lightweight ordering process with the ability to edit in real time and delete orders as soon they have not been processed for sourdough preparation. Furthermore there is a blog section that is needed for better SEO characteristics and communication with the customers. The blog section has its own content management system, where the administrator can create a blog based on content and image blocks that are not limited in their order or number. The app has its own administrator panel and does not use the standart Django admin app. The admin panel is created specially for the business owner to be able to manage her tasks. The app is build according to the responsive requirement and is fully responsive even on small smartphone displays.

### Business logic

The app incorporates the folowing limitations:
1. The user is allowed to order maximum 5 breads at once
2. The bakery can accept maximum 10 breads per day
3. Orders that exceed the total daily ammount are transfered to the next day as a whole, i.e. not split. For example, if there are already 8 breads ordered for this day, a user orders 3 breads, all 3 breads are transfered for the next day. The user has a JS metric that tells him how much bread can be ordered for this day, and if the user ignores this and orders more, a JS message informs him that the order will be rescheduled.
4. Orders can be edited or canceled if there are more than 2 days until completion. Once the sourdough is prepared, the users order is marked as Processed and cannot be changed any more.
5. Orders after 21h are rescheduled for the next day.
6. If delivery date is more than 2 days ahead, orders after 21h are not rescheduled.

### App functions for all users

All users have access to the blog (read only), waitlist and the Our Bread section.

### App functions for loged in users

1. Place order pannel - user shipping details are remembered if user is a returning customer. User has a JS real time calculator that always updates the pricing information based on users choice and displays order quantity limitations.
2. My Orders pannel - user has all his orders at one place and can edit/ delete them. There is a JS logic that guides the user in real time how much additional bread can be ordered. Additional the user has metrics: summary in graphical form for active orders and order history.

### App functions for Admin users

Admin users have three additional pannels: Task Manager, Blog Admin and Metrics
1. Task Manager - lists the daily tasks - summary for the day and details. This function will be used every day by the bakery owner to display how much and what type of bread has to be made today (and in the next days if orders exceed 10). 
2. Blog Admin - this section contains a home made content management system (CMS) that allows the bakery owner to create blogs. The CMS allows for a dynamic blog creation and does not have to follow a pre programmed schema. The content manager can use content and image blocks in a random order to create a blog. For example: A blog can be made of a content block with text, then 2 or 3 images, then another content block, then images etc. There are no limitations. In addition the blog entries can be edited and extended or deleted. The CMS can access the local machines drives to upload pictures and saves them to the database.
3. Metrics - there are User and Order metrics. User metrics list all users (except admin users) with their total ammount of ordered items and cancelled orders. The table can be sorted for ordered or camceled items. User profiles can be deleted from this pannel. Order metrics are graphical summaries for the current month and history.

### Responsive Design

The app will be most likely used entirely on mobile devices, therefore a special attention has been paid that it performs flawlessly on small displays.

### File description

MARMOTBAKERY
* bakery
static -> images : the site header image
blogadmin.js -> the JS file that dynamically creates the admin blog section, fetches data to django, saves and posts blogs, manages the file upload
mySort.js -> W3Schools sorting function modified to work with strings and more table columns
style.css -> css files
templates -> all html pages
templatetags -> contains custom tags used in the html pages. For example remove the $ sign and make percentage calculations for the graphical representations
admin.py -> register models for the admin pannel. The django default admin pannel is not used in this app.
apps.py -> lists the bakery app only
forms.py -> contains the forms for placing an order, editing order, user creation (not implemented yet, see section Outlook), file upload form
models.py -> django models
tests.py -> no tests created yet
urls.py -> has all urls used in the app
views.py -> has all the app logic
* marmotbakery
settings.py -> app settings + the registration of the media folder for pictres upload
urls.py -> has the admin app url and ties in all bakery urls + the static url
* media
This folder is used to store all pictures uploaded thtough the Blog Admin file upload functionality

### How tu run application

The application contains a database, because there are images that are needed for it to function propperly. In order to run the app first you have to issue: **py manage.py runserver**. If the database has to be recreated in addition **py manage.py makemigrations bakery** and **py manage.py migrate** have to be issued.

### Outlook

As this is a real project it has functions that are not implemented yet.
1. More attetion will be given to security, user authentication, cross site scripting and SQL injection.
2. A limitation for the uploaded file types has to be implemented, for example only *.jpeg, *.png etc.
3. The blog section will have a comment form for users and voting function.
4. The app will be web hosted and beta users will start using it in order to identify and fix bugs, mainly in the business logic
5. The CMS will be extended with more functionality, giving the content manager more tools to create great blogs. For example management of picture size, tags, text highlighting
6. Connection of the Instagramm account of the bakery: insta user marmotbake

### Final notes

As I started this course I had no idea about web development. The second project was the corner stone for me, where I almost gave up. After that point things got better and smoother. I guarantee that I have written ALL the code alone, used NO help from anybody and enjoyed the process (after project 2 though). Thank You Mr. Yu, Thak You Prof. Malan! This is one of the best courses I have ever experienced. Wish You all the best and stay safe!