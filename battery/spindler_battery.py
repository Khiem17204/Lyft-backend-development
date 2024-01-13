from battery.battery import Battery

class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
    def needs_service(self):
        date_need_serviced = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if self.current_date > date_need_serviced:
            return True
        else:
            return False