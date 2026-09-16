# Aircraft State
- This URL retrieves data about the current aircraft state

<br>

#### HTTP Request

- GET http://localhost:8111/state

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
      <th>Engine number</th>
   </tr>
 </table>

- name: **valid**
    * contains: boolean
    * description: Whether the returned state is valid.

- name: **aileron, %**
    * contains: integer
    * description: Aileron control input as a percentage.

- name: **elevator, %**
    * contains: integer
    * description: Elevator control input as a percentage.

- name: **rudder, %**
    * contains: integer
    * description: Rudder control input as a percentage.

- name: **H, m**
    * contains: integer
    * description: Current aircraft altitude in meters.

- name: **TAS, km/h**
    * contains: integer
    * description: True airspeed in kilometers per hour.

- name: **IAS, km/h**
    * contains: integer
    * description: Indicated airspeed in kilometers per hour.

- name: **M**
    * contains: decimal
    * description: Mach number.

- name: **AoA, deg**
    * contains: decimal
    * description: Aircraft angle of attack in degrees.

- name: **AoS, deg**
    * contains: decimal
    * description: Aircraft angle of sideslip in degrees.

- name: **Ny**
    * contains: decimal
    * description: Normal load factor.

- name: **Vy, m/s**
    * contains: decimal
    * description: Aircraft vertical speed in meters per second.

- name: **Wx, deg/s**
    * contains: integer
    * description: Aircraft rotation around the *x* axis in degrees per second.

- name: **Mfuel, kg**
    * contains: integer
    * description: Current fuel mass in kilograms.

- name: **Mfuel0, kg**
    * contains: integer
    * description: Initial fuel mass in kilograms.

- name: **throttle _N_, %**
    * contains: integer
    * description: Throttle position of engine _N_ as a percentage.

- name: **radiator _N_, %**
    * contains: integer
    * description: Radiator position of engine _N_ as a percentage.

- name: **magneto _N_**
    * contains: integer
    * description: Magneto setting for engine _N_.

- name: **power _N_, hp**
    * contains: decimal
    * description: Power of engine _N_ in horsepower.

- name: **RPM _N_**
    * contains: integer
    * description: Revolutions per minute of engine _N_.

- name: **manifold pressure _N_, atm**
    * contains: decimal
    * description: Manifold pressure of engine _N_ in atmospheres.

- name: **water temp _N_, C**
    * contains: integer
    * description: Water temperature of engine _N_ in degrees Celsius.

- name: **oil temp _N_, C**
    * contains: integer
    * description: Oil temperature of engine _N_ in degrees Celsius.

- name: **pitch _N_, deg**
    * contains: decimal
    * description: Propeller pitch of engine _N_ in degrees.

- name: **thrust _N_, kgs**
    * contains: integer
    * description: Thrust produced by engine _N_ in kilograms-force.

- name: **efficiency _N_, %**
    * contains: integer
    * description: Efficiency of engine _N_ as a percentage.
    
    
