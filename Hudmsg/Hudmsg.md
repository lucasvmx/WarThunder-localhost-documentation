# Hudmsg

- very similar to gamechat.. instead of a list of dicts, its a dict with keys events and damage, events is always empty iirc, and damage is a list of dicts

<br>

#### Detailed description

Hudmsg is accessed via url query parameters ``?field=value``  
Note: these values start at 0 or 1 (whatever it is) only at game start. so the second match will start the id where the first match id ended.  

http://localhost:8111/hudmsg?lastEvt=0&lastDmg=0  

#### HTTP Request
- GET http://localhost:8111/hudmsg

#### Query parameters

- lastEvt
    - id of event to search

- lastDmg
    - id of damage

#### HTTP Response :white_check_mark:
```json
{
  "events": [],
  "damage": [
    {
      "id": 161,
      "msg": "percusiones1r (Spitfire) set afire *shino_rs (Spitfire)",
      "sender": "",
      "enemy": false,
      "mode": ""
    }
    {
      "id": 162,
      "msg": "*shino_rs (Spitfire) has crashed.",
      "sender": "",
      "enemy": false,
      "mode": ""
    }
  ]
}
```