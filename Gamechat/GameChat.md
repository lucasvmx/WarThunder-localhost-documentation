# Gamechat

- Retrieves data from game chat

<br>

#### Detailed description

Gamechat is accessed via url query parameters ``?field=value``  
Note: these values start at 0 or 1 (whatever it is) only at game start. so the second match will start the id where the first match id ended.

http://localhost:8111/gamechat?lastId=0

<br>

#### HTTP Request
- GET http://localhost:8111/gamechat

#### Query parameters

- lastId
    - gives you json of all chat messages up until the point you requested it
    
- Example:
  - if there were 56 messages, and you requested ``GET http://localhost:8111/gamechat?lastId=55`` you would only get the last (56th) message (assuming that it has a index start of 0, not 1...)
  
#### HTTP Response :white_check_mark:

```json
[
    {
        "id": 70,
        "msg": "hahaha",
        "sender": "pecusgaming",
        "enemy": false,
        "mode": "All"
    },
    {
        "id": 71,
        "msg": "this thing is slightly op tbh",
        "sender": "pecusgaming",
        "enemy": false,
        "mode": "All"
    }
]
```

### Fields

- name: **id**
    * contains: integer
    * description: message id

- name: **msg**
    * contains: string
    * description: message content

- name: **sender**
    * contains: string
    * description: player name

- name: **enemy**
    * contains: boolean
    * description: true if is a enemy player false otherwise

- name: **mode**
    * contains: string
    * description: