# War Thunder Localhost API

Documentation for the local HTTP API exposed by War Thunder at
`localhost:8111`. It provides aircraft telemetry, flight state, chat, mission,
and map data for local clients.

## OpenAPI Specification

The complete specification is available in [`openapi.yaml`](openapi.yaml). It
can be imported directly into Swagger UI, Redoc, Postman, or any client
generator compatible with OpenAPI 3.0.

Interactive documentation is available in the [Swagger UI published on GitHub
Pages](https://lucasvmx.github.io/WarThunder-localhost-documentation/).

> The API is local and does not require authentication. Endpoints are only
> available while the game's HTTP server is running.

## Quick Start

```bash
# Current aircraft state
curl http://localhost:8111/state

# Aircraft instruments
curl http://localhost:8111/indicators

# New chat messages since the last processed ID
curl 'http://localhost:8111/gamechat?lastId=0'
```

The chat and HUD endpoints use incremental identifiers. A client should store
the last processed `id` and send it in the next request for incremental
polling.

## Endpoints

| Resource | Method and route | Documentation |
| --- | --- | --- |
| Chat | `GET /gamechat?lastId=0` | [`GameChat`](Gamechat/GameChat.md) |
| HUD and damage | `GET /hudmsg?lastEvt=0&lastDmg=0` | [`HudMsg`](Hudmsg/Hudmsg.md) |
| Instruments | `GET /indicators` | [`Indicators`](Indicators/Indicators.md) |
| Map objects | `GET /map_obj.json` | [`MapObjects`](MapObjects/MapObjects.md) |
| Map metadata | `GET /map_info.json` | [`MapInfo`](Mapinfo/MapInfo.md) |
| Map image | `GET /map.img` | [`MapInfo`](Mapinfo/MapInfo.md) |
| Mission | `GET /mission.json` | [`Mission`](Mission/Mission.md) |
| Aircraft state | `GET /state` | [`State`](State/State.md) |

## Integration

1. Start War Thunder and make sure the local API is available.
2. Query the JSON endpoints with `GET` at `http://localhost:8111`.
3. For chat and HUD data, keep track of the latest identifiers received.
4. Use [`openapi.yaml`](openapi.yaml) as the contract for generating models or
   an API client.

Instrument and state values vary by aircraft. Clients should therefore allow
additional properties and missing fields that do not apply to the current
vehicle.

## Reference Client

- [WarTelemetry](https://github.com/lucasvmx/WarTelemetry)

## Development

[`script.py`](script.py) is a helper utility that queries the JSON endpoints
and generates field lists in Markdown. It requires the game to be available at
`localhost:8111`.

## War Thunder

[Download War Thunder from the official website](https://warthunder.com/en/game/).
