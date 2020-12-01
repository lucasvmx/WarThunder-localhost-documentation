# Mission
- This URL retrieves data from the current mission

<br>

#### HTTP Request

- ```GET localhost:8111/mission.json```

#### Query parameters

- None

#### HTTP Response :white_check_mark:

- Example:

```json
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 52
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: GET, POST, OPTIONS

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
    * type: JSON array containing all mission objectives
    * description:

    - name: **primary**
        * type: boolean
        * description: flag to determine if this is a primary mission
    
    - name: **status**
        * type: string
        * description: contains the status of current primary objective
        * possible values: "in_progress", "completed" or "failed"
    
    - name: **text**
        * type: string
        * description: contains instruction of what the player needs to do for complete the mission

- name: **status**
    - type: string
    - descruption: contains status of the current mission can be "running" or "fail"