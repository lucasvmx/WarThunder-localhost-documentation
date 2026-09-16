# HUD Messages

- Retrieves HUD events and damage messages.

The response is similar to the game chat response. Instead of an array, it is
an object with `events` and `damage` keys. The `events` array is currently
empty in observed responses, while `damage` contains a list of objects.

<br>

#### Detailed Description

The HUD messages endpoint accepts URL query parameters in the `?field=value`
format.

Note: these identifiers start at 0 or 1, depending on the game, only when the
game starts. The next match continues with the identifier where the previous
match ended.

`http://localhost:8111/hudmsg?lastEvt=0&lastDmg=0`

<br>

#### HTTP Request

- `GET http://localhost:8111/hudmsg`

#### Query Parameters

- `lastEvt`
  - ID of the last event to process.

- `lastDmg`
  - ID of the last damage message to process.

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
    },
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
