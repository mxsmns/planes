import json
from typing import TypedDict


class AircraftDict(TypedDict):
    hex: str
    type: str
    flight: str
    r: str
    t: str
    alt_baro: str
    gs: float
    true_heading: float
    squawk: str
    emergency: str
    category: str
    lat: float
    lon: float
    nic: int
    rc: int
    seen_pos: float
    version: int
    nac_p: int
    nac_v: int
    sil: int
    sil_type: str
    sda: int
    alert: int
    spi: int
    mlat: list[object]
    tisb: list[object]
    messages: int
    seen: float
    rssi: float


def parse_json(data: str) -> AircraftDict:
    return json.loads(data)
