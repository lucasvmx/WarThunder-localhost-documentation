# Map Information

- Contains information about the current map.

<br>

#### HTTP Request

- `GET http://localhost:8111/map_info.json`
- `GET http://localhost:8111/map.img`

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
  - contains: array of numeric strings
  - description: Distance between grid lines on the X and Y axes.

- name: **grid_zero**
  - contains: array of numeric strings
  - description: Map coordinates corresponding to the grid origin.

- name: **map_generation**
  - contains: numeric string
  - description: Map version or generation.

- name: **map_max**
  - contains: array of numeric strings
  - description: Maximum map coordinates.

- name: **map_min**
  - contains: array of numeric strings
  - description: Minimum map coordinates.
