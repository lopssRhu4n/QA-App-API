import httpx

class RouteTester:
    def __init__(self, route):
        self.route = route
        
    def RouteGetStatus(self, endpoint):
        return httpx.get(self.route + endpoint).status_code
    
    def RoutePostStatus(self, endpoint, payload):
        return httpx.post(self.route + endpoint, json=payload).status_code
    
    def RoutePutStatus(self, endpoint, payload):
        return httpx.put(self.route + endpoint, json=payload).status_code
    
    def RouteDeleteStatus(self, endpoint):
        return httpx.delete(self.route + endpoint).status_code