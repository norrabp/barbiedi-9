import json
from json_to_edi import get_edi


def test_mojo_dojo_casa_house():
    with open("./examples/mojo_dojo_casa_house.json") as file:
        json_data = json.load(file)
    
    edi = get_edi(json_data)
    with open("./examples/mojo_dojo_casa_house.837") as file:
        correct = "\n".join(file.readlines())
        assert edi == correct


def test_multi_procedure_barbie():
    with open("./examples/multi_procedure_barbie.json") as file:
        json_data = json.load(file)
    
    edi = get_edi(json_data)
    with open("./examples/multi_procedure_barbie.837") as file:
        correct = "\n".join(file.readlines())
        assert edi == correct


def test_subscriber_with_a_dekedent():
    with open("./examples/subscriber_with_a_dekendent.json") as file:
        json_data = json.load(file)
    
    edi = get_edi(json_data)
    with open("./examples/subscriber_with_a_dekendent.837") as file:
        correct = "\n".join(file.readlines())
        assert edi == correct