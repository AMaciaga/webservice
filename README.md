# Webservice

### Build image
```
docker build -t webservice .  
```
### Run container
```
docker run -d -p 5000:5000 webservice
```
### How to send requests in curl
* GET
  ```
  curl 127.0.0.1:5000/add
  ```
* POST
  ```
  curl -H "Content-Type: application/json" -X POST -d '{"first_num": 1,"second_num":2}' http://127.0.0.1:5000/add
  ```
### Expected results
* GET
  ```
  Hello :)
  ```
* POST
  ```
  {
    "result": 3
  }

  ```
