# War Thunder Localhost API

Documentação da API HTTP local exposta pelo War Thunder em `localhost:8111`.
Ela fornece telemetria da aeronave, estado de voo, chat, missão e dados do mapa
para clientes locais.

## Especificação OpenAPI

A especificação completa está em [`openapi.yaml`](openapi.yaml). Ela pode ser
importada diretamente no Swagger UI, Redoc, Postman ou em qualquer gerador de
clientes compatível com OpenAPI 3.0.

> A API é local e não exige autenticação. Os endpoints só ficam disponíveis
> enquanto o servidor HTTP do jogo estiver ativo.

## Início rápido

```bash
# Estado atual da aeronave
curl http://localhost:8111/state

# Instrumentos da aeronave
curl http://localhost:8111/indicators

# Mensagens novas do chat a partir do último ID processado
curl 'http://localhost:8111/gamechat?lastId=0'
```

Os endpoints de chat e HUD usam identificadores incrementais. Um cliente deve
guardar o último `id` processado e enviá-lo na próxima consulta para realizar
polling incremental.

## Endpoints

| Recurso | Método e rota | Documentação |
| --- | --- | --- |
| Chat | `GET /gamechat?lastId=0` | [`GameChat`](Gamechat/GameChat.md) |
| HUD e danos | `GET /hudmsg?lastEvt=0&lastDmg=0` | [`HudMsg`](Hudmsg/Hudmsg.md) |
| Instrumentos | `GET /indicators` | [`Indicators`](Indicators/Indicators.md) |
| Objetos do mapa | `GET /map_obj.json` | [`MapObjects`](MapObjects/MapObjects.md) |
| Metadados do mapa | `GET /map_info.json` | [`MapInfo`](Mapinfo/MapInfo.md) |
| Imagem do mapa | `GET /map.img` | [`MapInfo`](Mapinfo/MapInfo.md) |
| Missão | `GET /mission.json` | [`Mission`](Mission/Mission.md) |
| Estado da aeronave | `GET /state` | [`State`](State/State.md) |

## Integração

1. Inicie o War Thunder e certifique-se de que a API local esteja disponível.
2. Consulte os endpoints JSON com `GET` em `http://localhost:8111`.
3. Para chat e HUD, mantenha os últimos identificadores recebidos.
4. Use [`openapi.yaml`](openapi.yaml) como contrato para gerar modelos ou um
   cliente da API.

Os valores de instrumentos e estado variam conforme a aeronave. Por isso,
clientes devem tolerar propriedades adicionais e a ausência de campos que não
se aplicam ao veículo atual.

## Cliente de referência

- [WarTelemetry](https://github.com/lucasvmx/WarTelemetry)

## Desenvolvimento

O [`script.py`](script.py) é um utilitário auxiliar que consulta os endpoints
JSON e gera listas de campos em Markdown. Ele requer que o jogo esteja
disponível em `localhost:8111`.

## War Thunder

[Baixe o War Thunder no site oficial](https://warthunder.com/en/game/).
