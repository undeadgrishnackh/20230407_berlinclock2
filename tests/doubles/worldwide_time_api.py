import json
import responses

stub_json_19_36_01 = json.loads(
    '{"abbreviation": "CEST", '
    '"client_ip": "188.95.151.252", '
    '"datetime": "2023-09-01T19:36:01.940852+02:00", '
    '"day_of_week": 5, '
    '"day_of_year": 244, '
    '"dst": true, '
    '"dst_from": "2023-03-26T01:00:00+00:00", '
    '"dst_offset": 3600, '
    '"dst_until": "2023-10-29T01:00:00+00:00", '
    '"raw_offset": 3600, '
    '"timezone": "Europe/Berlin", '
    '"unixtime": 1693556553, '
    '"utc_datetime": "2023-09-01T08:22:33.940852+00:00", '
    '"utc_offset": "+02:00", '
    '"week_number": 35}'
)

stub_response_19_36_01 = responses.Response(
    method="GET",
    url="http://worldtimeapi.org/api/timezone/Europe/Berlin",
    json=stub_json_19_36_01,
    status=200,
)
