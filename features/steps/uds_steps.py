#This is a test for cucumber 
from behave import given, when, then

class FakeECU:
    def __init__(self):
        self.session = "default"

    def set_session(self, session):
        self.session = session

    def send_request(self, request):
        if request == "0x22 F187":
            return {"positive": True, "data": "PN12345678"}
        elif request == "0x22 F999":
            return {"positive": False}
        return {"positive": False}

ecu = FakeECU()

@given('the ECU is powered on')
def step_power(context):
    context.ecu = ecu

@given('diagnostic session is "{session}"')
def step_session(context, session):
    context.ecu.set_session(session)

@when('I send a UDS request "{request}"')
def step_request(context, request):
    context.response = context.ecu.send_request(request)

@then('the response should be positive')
def step_positive(context):
    assert context.response["positive"] is True

@then('the response should be negative')
def step_negative(context):
    assert context.response["positive"] is False

@then('the DID "{did}" should return a valid part number')
def step_validate_pn(context, did):
    data = context.response.get("data", "")
    assert data.startswith("PN")
    assert len(data) >= 8