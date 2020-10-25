# State
- This URL retrieves data of current aircraft state

<br>

#### HTTP Request

- ```GET localhost:8111/state```

- Example:

```json
{
   "valid":true,
   "aileron, %":0,
   "elevator, %":-6,
   "rudder, %":-1,
   "H, m":132,
   "TAS, km/h":264,
   "IAS, km/h":262,
   "M":0.22,
   "AoA, deg":1.1,
   "AoS, deg":-0.0,
   "Ny":1.03,
   "Vy, m/s":3.3,
   "Wx, deg/s":0,
   "Mfuel, kg":63,
   "Mfuel0, kg":210,
   "throttle 1, %":86,
   "radiator 1, %":0,
   "magneto 1":3,
   "power 1, hp":486.7,
   "RPM 1":2034,
   "manifold pressure 1, atm":1.05,
   "water temp 1, C":90,
   "oil temp 1, C":61,
   "pitch 1, deg":31.0,
   "thrust 1, kgs":431,
   "efficiency 1, %":85
}
```

### Fields

#### Legend
<table>
   <tr>
      <th>Symbol</th>
      <th>Description</th>
   </tr>
   <tr>
      <th>N</th>
      <th>The engine number</th>
   </tr>
 </table>

- name: **valid**
    * contains: boolean
    * description:

- name: **aileron, %**
    * contains: integer
    * description:

- name: **elevator, %**
    * contains: integer
    * description:

- name: **rudder, %**
    * contains: integer
    * description:

- name: **H, m**
    * contains: integer
    * description: current aircraft altitude in meters

- name: **TAS, km/h**
    * contains: integer
    * description: the true airspeed in kilometers per hour

- name: **IAS, km/h**
    * contains: integer
    * description: the indicated airspeed in kilometers per hour

- name: **M**
    * contains: decimal
    * description:

- name: **AoA, deg**
    * contains: decimal
    * description: aircraft angle of attack in degrees

- name: **AoS, deg**
    * contains: decimal
    * description:

- name: **Ny**
    * contains: decimal
    * description:

- name: **Vy, m/s**
    * contains: decimal
    * description: aircraft vertical speed in meters per second

- name: **Wx, deg/s**
    * contains: integer
    * description: aircraft rotation on *x* axis in degrees per second

- name: **Mfuel, kg**
    * contains: integer
    * description:

- name: **Mfuel0, kg**
    * contains: integer
    * description:

- name: **throttle _N_, %**
    * contains: integer
    * description:

- name: **radiator _N_, %**
    * contains: integer
    * description:

- name: **magneto _N_**
    * contains: integer
    * description:

- name: **power _N_, hp**
    * contains: decimal
    * description: power of engine nº 1 in horse-power

- name: **RPM _N_**
    * contains: integer
    * description:

- name: **manifold pressure _N_, atm**
    * contains: decimal
    * description:

- name: **water temp _N_, C**
    * contains: integer
    * description: water temperature of engine nº 1 in celsius

- name: **oil temp _N_, C**
    * contains: integer
    * description:

- name: **pitch _N_, deg**
    * contains: decimal
    * description:

- name: **thrust _N_, kgs**
    * contains: integer
    * description:

- name: **efficiency _N_, %**
    * contains: integer
    * description:
    
    
