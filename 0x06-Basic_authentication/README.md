# 0x06. Basic authentication

## Resources:books:
Read or watch:
* [REST API Authentication Mechanisms](https://intranet.hbtn.io/rltoken/Yx1Na2qEzCLnke8RnpACDw)
* [Base64 in Python](https://intranet.hbtn.io/rltoken/R2kTeyWl2ef19mdxQuffww)
* [HTTP header Authorization](https://intranet.hbtn.io/rltoken/5BfGd-_oV9Asi_Ymi_lRSA)
* [Flask](https://intranet.hbtn.io/rltoken/3ivma6PpGZfjzDrA2zLq7g)
* [Base64 - concept](https://intranet.hbtn.io/rltoken/8ckHTvJq00WnvgEmn6GGtg)

---
## Learning Objectives:bulb:
What you should learn from this project:

* What authentication means
* What Base64 is
* How to encode a string in Base64
* What Basic authentication means
* How to send the Authorization header

---
# Simple API

Simple HTTP API for playing with `User` model.


## Files

### `models/`

- `base.py`: base of all models of the API - handle serialization to file
- `user.py`: user model

### `api/v1`

- `app.py`: entry point of the API
- `views/index.py`: basic endpoints of the API: `/status` and `/stats`
- `views/users.py`: all users endpoints


## Setup

```
$ pip3 install -r requirements.txt
```


## Run

```
$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```


## Routes

- `GET /api/v1/status`: returns the status of the API
- `GET /api/v1/stats`: returns some stats of the API
- `GET /api/v1/users`: returns the list of users
- `GET /api/v1/users/:id`: returns an user based on the ID
- `DELETE /api/v1/users/:id`: deletes an user based on the ID
- `POST /api/v1/users`: creates a new user (JSON parameters: `email`, `password`, `last_name` (optional) and `first_name` (optional))
- `PUT /api/v1/users/:id`: updates an user based on the ID (JSON parameters: `last_name` and `first_name`)




---

## Author
* **Sergio Steben Arias Quintero** - [sarias12](https://github.com/sarias12)
