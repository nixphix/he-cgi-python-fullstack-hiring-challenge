![banner](https://media-fastly.hackerearth.com/media/hackathon/cgi-python-fullstack-hiring-challenge/images/c187b650aa-cgi_hackathon_banner_1.png)
## [CGI Python Fullstack Hiring Challenge](https://www.hackerearth.com/challenges/hiring/cgi-python-fullstack-hiring-challenge/)

### Solution to Django-DRF API Question

   1. To upload the csv place the data in `games-api/data` folder and run management command
      ```python
      python manage.py upload_csv <file_name>
      ```
   2. Create django user via console
      ```python
      python manage.py createsuperuser
      ```
      will prompt for details
      ```shell
      Username : user
      Email address: user@domain.tld
      Password:
      Password (again):
      Superuser created successfully.
      ```
   3. To get the authentication token cURL with username and password
      ```shell
      curl -d '{"username":"user", "password":"*********"}' -H "Content-Type: application/json" -X POST http://localhost:8000/token/
      ```
      should return token for the user
      ```
      {"token":"fb9a152b9b9dca66c43e90bb2d4a9c94f3493473"}
      ```
   4. Pass the token as Authorization head to access the api resources
      ```shell
      curl -H "Content-Type: application/json" -H "Authorization: Token fb9a152b9b9dca66c43e90bb2d4a9c94f3493473" -X GET http://localhost:8000/api/v1/games/1/
      ```
      should return
      ```shell
      {"title":"LittleBigPlanet PS Vita","platform":"PlayStation Vita","score":9.0,"genre":"Platformer","editors_choice":"Y","created_at":"2019-08-26T00:44:52.185538Z","updated_at":"2019-08-26T00:44:52.185578Z"}
      ```
   5. Swagger Docs available at [http://localhost:8000/docs/](http://localhost:8000/docs/)


### Swagger Docs
![Swagger Docs](https://raw.githubusercontent.com/nixphix/assets/master/hack/he-games-api-swagger-docs.png)
