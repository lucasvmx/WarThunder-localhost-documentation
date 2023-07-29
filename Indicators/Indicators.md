# Indicators
- This URL retrieves data from aircraft instruments

<br>

#### HTTP Request
- GET http://localhost:8111/indicators

#### Query parameters

- None

#### HTTP Response :white_check_mark:

- Example:

HTTP/1.1 200 OK<br>
Content-Type: application/json<br>
Content-Length: 1389<br>
Access-Control-Allow-Origin: *<br>
Access-Control-Allow-Methods: GET, POST, OPTIONS<br>
    
```json
    {
   "valid":true,
   "type":"so_4050_vautour_2a_iaf",
   "speed":0.000000,
   "pedals":0.000000,
   "pedals1":0.000000,
   "pedals2":0.000000,
   "pedals3":0.000000,
   "stick_elevator":0.000000,
   "stick_elevator1":0.000000,
   "stick_ailerons":-0.000000,
   "vario":0.000000,
   "altitude_hour":63.055698,
   "altitude_min":63.055698,
   "altitude_10k":63.055698,
   "aviahorizon_roll":-0.083683,
   "aviahorizon_pitch":-4.278834,
   "bank":0.083683,
   "turn":0.000000,
   "compass":355.831299,
   "compass1":355.831299,
   "compass2":355.831299,
   "clock_hour":9.166667,
   "clock_min":10.000000,
   "clock_sec":13.000000,
   "rpm_min":897.000000,
   "rpm1_min":915.000000,
   "rpm_hour":2897.420898,
   "rpm1_hour":2915.319092,
   "oil_pressure":51.979767,
   "oil_pressure1":52.032928,
   "head_temperature":529.008423,
   "head_temperature1":529.614746,
   "fuel":3182.000000,
   "fuel1":3182.000000,
   "fuel_pressure":0.000000,
   "fuel_pressure1":0.000000,
   "airbrake_lever":0.000000,
   "airbrake_indicator":0.000000,
   "gears":0.500000,
   "gears1":0.500000,
   "gears_lamp":0.000000,
   "flaps":0.000000,
   "flaps1":0.000000,
   "throttle":0.000000,
   "throttle1":0.000000,
   "weapon2":0.000000,
   "weapon3":0.000000,
   "mach":0.000000,
   "g_meter":0.919596,
   "g_meter_min":0.075778,
   "g_meter_max":43.741905,
   "blister1":1.000000,
   "blister2":1.000000,
   "blister3":1.000000,
   "blister4":1.000000,
   "blister5":1.000000,
   "blister6":1.000000,
   "blister7":1.000000
}
```


### Fields

- name: **valid**
    * contains: bool
    * description:

- name: **type**
    * contains: string
    * description: contains aircraft name

- name: **speed**
    * contains: float
    * description:

- name: **pedals**
    * contains: float
    * description:

- name: **pedals1**
    * contains: float
    * description:

- name: **pedals2**
    * contains: float
    * description:

- name: **pedals3**
    * contains: float
    * description:

- name: **stick_elevator**
    * contains: float
    * description:

- name: **stick_elevator1**
    * contains: float
    * description:

- name: **stick_ailerons**
    * contains: float
    * description:

- name: **vario**
    * contains: float
    * description:

- name: **altitude_hour**
    * contains: float
    * description:

- name: **altitude_min**
    * contains: float
    * description:

- name: **altitude_10k**
    * contains: float
    * description:

- name: **aviahorizon_roll**
    * contains: float
    * description:

- name: **aviahorizon_pitch**
    * contains: float
    * description:

- name: **bank**
    * contains: float
    * description:

- name: **turn**
    * contains: float
    * description:

- name: **compass**
    * contains: float
    * description:

- name: **compass1**
    * contains: float
    * description:

- name: **compass2**
    * contains: float
    * description:

- name: **clock_hour**
    * contains: float
    * description:

- name: **clock_min**
    * contains: float
    * description:

- name: **clock_sec**
    * contains: float
    * description:

- name: **rpm_min**
    * contains: float
    * description:

- name: **rpm1_min**
    * contains: float
    * description:

- name: **rpm_hour**
    * contains: float
    * description:

- name: **rpm1_hour**
    * contains: float
    * description:

- name: **oil_pressure**
    * contains: float
    * description:

- name: **oil_pressure1**
    * contains: float
    * description:

- name: **head_temperature**
    * contains: float
    * description:

- name: **head_temperature1**
    * contains: float
    * description:

- name: **fuel**
    * contains: float
    * description:

- name: **fuel1**
    * contains: float
    * description:

- name: **fuel_pressure**
    * contains: float
    * description:

- name: **fuel_pressure1**
    * contains: float
    * description:

- name: **airbrake_lever**
    * contains: float
    * description:

- name: **airbrake_indicator**
    * contains: float
    * description:

- name: **gears**
    * contains: float
    * description:

- name: **gears1**
    * contains: float
    * description:

- name: **gears_lamp**
    * contains: float
    * description:

- name: **flaps**
    * contains: float
    * description:

- name: **flaps1**
    * contains: float
    * description:

- name: **throttle**
    * contains: float
    * description:

- name: **throttle1**
    * contains: float
    * description:

- name: **weapon2**
    * contains: float
    * description:

- name: **weapon3**
    * contains: float
    * description:

- name: **mach**
    * contains: float
    * description:

- name: **g_meter**
    * contains: float
    * description:

- name: **g_meter_min**
    * contains: float
    * description:

- name: **g_meter_max**
    * contains: float
    * description:

- name: **blister1**
    * contains: float
    * description:

- name: **blister2**
    * contains: float
    * description:

- name: **blister3**
    * contains: float
    * description:

- name: **blister4**
    * contains: float
    * description:

- name: **blister5**
    * contains: float
    * description:

- name: **blister6**
    * contains: float
    * description:

- name: **blister7**
    * contains: float
    * description:

- name: **wing_sweep_lever**
    * contains: string
    * description: wing speed angle
