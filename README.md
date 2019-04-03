Overview
============

Penpalz server is a server you can use to handle messages sent between users in different languages

Models
============

Each table in the database and its fields. All models also include a serial "id" field as well.
*User
    *email
    *firstname
    *lastname

*Lang
    *name
    *avg_level (this field is annotated in the view)

*Prof
    *user(foreign key to User)
    *language(foreign key to Lang)
    *level(must be and interger between 1 - 10)

*Message
    *sent (foreign key to User)
    *rec (foreign key to User)
    *language (foreign key to Lang)
    *content

URLs and CRUD
============

All endpoints start with "/api/". Each of the specific model urls are:
-domain/api/User/
-domain/api/Lang/
-domain/api/Prof/
-domain/api/Message/

A GET request to this url provides the index view.
Adding the id to the url returns the show view for that specifc object, I'll use the User model from here on but the same format applies to all models.

-domain/api/User/1/
A GET request to this endpoint will return the user with "id" 1. The trailing "/" after the one is required. 

-domain/api/User/
A POST request that includes a JSON object with all reqired fields will create a new user. For the models that include foreign key fields, the id of the desired object in the database should be passed as an interger. 

-domain/api/User/1/
A PUT or PATCH request with a body that includes all fields, not just the one being updated, will update the selected item in the database.

-domain/api/User/1/
A DELETE request will delete the item from the database. Also returns not found if no entry with the id is found in the database.

Additional Parameters
============

For the Lang model, in addition to the name, there is an extra field that displays the average level of all users in that language. This is calculated by taking the average of the level of all proficiencies of that language in the database.

For the Message model, I wrote a custom 'create' method that gets the proficiency of each user in the selected language from the database, calculates the absolute difference between their levels, and then only creates the new message if that difference is less than or equal to 2. If the difference is too great, the method returns an error of "Proficency mismatch".

Additional Notes
============
I used Django REST Framework instead of writing each of the urls and views individually so I could spend more time on the logic of the language calculated field and the message validation. However, I would like to be able to update an entry in the database without having to submit a copy of the entire object, so that may require writing a custom "change" method. Also, all of the foreign key fields currently just return the id, I would like those to return the id and some more useful information, like the user's name or the language name. Just a few things I'd like to work on if I had more time going forward.
