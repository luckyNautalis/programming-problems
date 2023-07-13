# Problem 1396: Design Underground System

"""
Constraints

1) 1 <= id, t <= 10^6
2) 1 <= stationName.length, startStation.length, endStation.length <= 10
3) All strings consist of uppercase and lowercase English letters and digits
4) There will be at most 2 * 104 calls in total to checkIn, checkOut, and getAverageTime
5) Answers within 10-5 of the actual value will be accepted

"""

class UndergroundSystem:

    def __init__(self):
        # routes_start={id:(start,st)}
        self.routes_start = {}
        # routes_end={id:(end,et)}
        self.routes_end = {}
        # completed_routes={(start,end):nums}
        self.completed_routes = {}
        # total_times={(start,end):t}
        self.total_times = {}

    def checkIn(self, id: int, start: str, st: int) -> None:
        start_data = (start, st)
        self.routes_start[id] = start_data

    def checkOut(self, id: int, end: str, et: int) -> None:
        end_data=(end, et)
        self.routes_end[id] = end_data

        route = (self.routes_start[id][0], end)
        if route in self.completed_routes:
            self.completed_routes[route]+=1
            self.total_times[route] += et - self.routes_start[id][1]
        else:
            self.completed_routes[route] = 1
            self.total_times[route] = et - self.routes_start[id][1]

    def getAverageTime(self, start: str, end: str) -> float:
        # Get the total time for the route by accessing the total time
        # in the total_t for route & divide by the number those routes taken.
        route = (start, end)
        total_time = self.total_times[route]
        route_num = self.completed_routes[route]
        return total_time/route_num

subway = UndergroundSystem()
subway.checkIn(12,"Tuscany",1)
subway.checkOut(12,"Somerset",12)
subway.checkIn(13,"Tuscany",1)
subway.checkOut(13,"Somerset",13)
print(subway.completed_routes)
print(subway.getAverageTime("Tuscany","Somerset"))
