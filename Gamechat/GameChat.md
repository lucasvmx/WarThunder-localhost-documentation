# Game Chat

- Retrieves data from the game chat.

<br>

#### Detailed Description

The game chat endpoint accepts URL query parameters in the `?field=value`
format.

Note: these identifiers start at 0 or 1, depending on the game, only when the
game starts. The next match continues with the identifier where the previous
match ended.

`http://localhost:8111/gamechat?lastId=0`

<br>

#### HTTP Request

- `GET http://localhost:8111/gamechat`

#### Query Parameters

- `lastId`
  - ID of the last message already processed. Messages after this ID are
    returned.

- Example:
  - If there were 56 messages and you requested
    `GET http://localhost:8111/gamechat?lastId=55`, you would receive only the
    last (56th) message, assuming indexing starts at 0 rather than 1.

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
  - contains: integer
  - description: Incremental message ID.

- name: **msg**
  - contains: string
  - description: Message content.

- name: **sender**
  - contains: string
  - description: Player name.

- name: **enemy**
  - contains: boolean
  - description: `true` if the sender is an enemy player; `false` otherwise.

- name: **mode**
  - contains: string
  - description: Chat channel or mode.
