# SB tweet like system


## Usage

First install required libs with pip:

**pip install -r requirements.txt**

After that get running the mysql server on localhost:3306 and run sql script located in root dir of project **sb.sql**

Add **config.json** file in root of project with credentials for connecting on running mysql db:
```json
{
    "username": "user",
    "password": "password"
}
```
Run **python app.py**, if everything is fine server should be listening on port 5000.

Examples of used **curl** commands:

GET request: **curl -X GET "http://localhost:5000/v1/tweets?hashTag=%23hash1&hashTag=%23hash2&hashTag=%23cool_hash1&offset=0&limit=10" --header "X-username: sbg_user1"**

POST request: **curl -X POST http://localhost:5000/v1/tweets -H "X-username: sbg_user1" -H "Content-Type: application/json" -d "{\\"tweetBody\\":\\"Some random text hehe\\",\\"hashTags\\":[\\"#cool_hash1\\", \\"#cool_hash2\\"]}"**

DELETE request: **curl -X DELETE "http://localhost:5000/v1/tweets/a937b2fd-3055-4dbe-b954-d8912c90cf84" --header "X-username: sbg_user1"**