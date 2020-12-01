# MapInfo
- Contains information about current map

<br>

#### HTTP Request
- GET http://localhost:8111/map_info.json
- GET http://localhost:8111/map.img

#### HTTP Response :white_check_mark:
```json
{
  "grid_steps": [
    "3250.0",
    "3250.0"
  ],
  "grid_zero": [
    "-32768.0",
    "32768.0"
  ],
  "map_generation": "1",
  "map_max": [
    "32768.0",
    "32768.0"
  ],
  "map_min": [
    "-32768.0",
    "-32768.0"
  ]
}
```

### Fields

- name: **grid_steps**
    * contains: array of floats
    * description:

- name: **grid_zero**
    * contains: array of floats
    * description:

- name: **map_generation**
    * contains: integer
    * description:

- name: **map_max**
    * contains: array of floats
    * description:

- name: **map_min**
    * contains: array of floats
    * description: 