# State
- This URL retrieves data of current aircraft state

<br>

#### HTTP Request

- ```GET localhost:8111/state```

- Example:

```json
{
   "valid":true,
   "aileron, %":-0,
   "elevator, %":-20,
   "rudder, %":-0,
   "flaps, %":0,
   "H, m":4936,
   "TAS, km/h":237,
   "IAS, km/h":185,
   "M":0.20,
   "AoA, deg":1.1,
   "AoS, deg":-0.1,
   "Ny":1.00,
   "Vy, m/s":3.2,
   "Wx, deg/s":-0,
   "Mfuel, kg":750,
   "Mfuel0, kg":2620,
   "throttle 1, %":100,
   "mixture 1, %":100,
   "magneto 1":3,
   "power 1, hp":484.0,
   "RPM 1":1957,
   "manifold pressure 1, atm":0.81,
   "oil temp 1, C":73,
   "pitch 1, deg":28.2,
   "thrust 1, kgs":473,
   "efficiency 1, %":85,
   "throttle 2, %":100,
   "mixture 2, %":100,
   "magneto 2":3,
   "power 2, hp":501.2,
   "RPM 2":2016,
   "manifold pressure 2, atm":0.82,
   "oil temp 2, C":75,
   "pitch 2, deg":28.2,
   "thrust 2, kgs":488,
   "efficiency 2, %":84,
   "throttle 3, %":100,
   "mixture 3, %":100,
   "magneto 3":3,
   "power 3, hp":483.9,
   "RPM 3":1957,
   "manifold pressure 3, atm":0.81,
   "oil temp 3, C":73,
   "pitch 3, deg":28.2,
   "thrust 3, kgs":473,
   "efficiency 3, %":85
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
    
    
