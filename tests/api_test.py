import os

import pytest

from planes.api import AircraftDict
from planes.api import parse_json


def test_parse_json(single_aircraft_json):
    result = parse_json(single_aircraft_json)

    assert result == AIRCRAFT_DATA


@pytest.fixture
def single_aircraft_json(resource_folder):
    with open(os.path.join(resource_folder, "single_aircraft.json")) as f:
        yield f.read()


AIRCRAFT_DATA: AircraftDict = {
    "hex": "abd90c",
    "type": "adsb_icao",
    "flight": "SWA347  ",
    "r": "N8623F",
    "t": "B738",
    "alt_baro": "ground",
    "gs": 0,
    "true_heading": 14.06,
    "squawk": "2657",
    "emergency": "none",
    "category": "A3",
    "lat": 33.433502,
    "lon": -111.994574,
    "nic": 8,
    "rc": 186,
    "seen_pos": 0.844,
    "version": 2,
    "nac_p": 9,
    "nac_v": 1,
    "sil": 3,
    "sil_type": "perhour",
    "sda": 2,
    "alert": 0,
    "spi": 0,
    "mlat": [],
    "tisb": [],
    "messages": 15366443,
    "seen": 0.8,
    "rssi": -8.8,
}
