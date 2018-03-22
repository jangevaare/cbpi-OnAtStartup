from modules import cbpi
from modules.core.props import Property
from modules.core.hardware import ActorBase

@cbpi.actor
class OnAtStartup(ActorBase):
    actor_setting = Property.Actor("Actor", description="Select the actor you would like to have ON at startup")
    power_setting = Property.Number("Power", True, 100, description="Select the power of the actor at startup")
    wait = Property.Number("Wait time", True, 60, description="Select the time (in seconds) before turning the actor on at startup")

    def init(self):
        if not 0 <= int(self.power_setting) <= 100:
            self.api.notify(headline="OnAtStartup Error", message="Power must be between 0 and 100", timeout=None, type="danger")
            raise ValueError("Power must be between 0 and 100")
        elif self.wait < 0:
            self.api.notify(headline="OnAtStartup Error", message="Wait time can not be negative", timeout=None, type="danger")
            raise ValueError("Wait time can not be negative")
        else:
            self.sleep(float(self.wait))
            self.api.switch_actor_on(int(self.actor_setting), power=int(self.power_setting))

    def set_power(self, power):
        pass

    def off(self):
        pass

    def on(self, power=None):
        pass
