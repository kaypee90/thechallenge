# thechallenge

Initial Setup:
----------------
- Run `docker-compose build `
- Then use `docker-compose up` to get the containers running
- You will get a prompt saying `database "take_home_drf" does not exist`
- To create a database connect to adminer container on http://localhost:8080, select postgres and provide the user name and password in .env file
- Once you are logged in create take_home_drf.
- After creating database stop and run `docker-compose up` again which will create all the tables needed
- Then login back to adminer on http://localhost:8080 and run the sql scripts in `seeddata.txt` file to populate the database with random test data
- After visit the api on http://localhost:8000/api/v1/diagnosis/
- Swagger documentation is located on http://localhost:8000/docs/

- Get all enpoint is paginated by passing limit and page as querystrings. It always defaults to limit=20 and page=1 when nothing is passed
- Provided is also a postman collection file `takehome.postman_collection.json`
