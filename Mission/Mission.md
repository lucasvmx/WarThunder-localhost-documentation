# Mission

- Retrieves data from the current mission.

<br>

#### HTTP Request

- `GET http://localhost:8111/mission.json`

#### Query Parameters

- None

#### HTTP Response :white_check_mark:

- Example:

```json
{
   "objectives" : [
      {
         "primary" : true,
         "status" : "in_progress",
         "text" : "Decole"
      }
   ],
   "status" : "running"
}
```

### Fields

- name: **objectives**
  - type: JSON array containing all mission objectives
  - description: List of objectives for the current mission.

  - name: **primary**
    - type: boolean
    - description: Flag indicating whether this is a primary mission objective.

  - name: **status**
    - type: string
    - description: Status of the current primary objective.
    - possible values: `in_progress`, `completed`, or `failed`

  - name: **text**
    - type: string
    - description: Instruction describing what the player must do to complete
      the mission.

- name: **status**
  - type: string
  - description: Status of the current mission; observed values include
    `running` and `fail`.
