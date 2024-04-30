from Request import Requests
from Drivers import Drivers
from Riders import Riders
from Destination import Destination
from RequestHandler import RequestHandler
from DriverHandler import DriverHandler
from CarpoolGenerator import CarpoolGenerator


# this script is used to test the carpooling algorithm



Aman1 = Riders("Aman1","IT","20124005")
Aman2 = Riders("Aman2","IT","20124005")
Aman3 = Riders("Aman3","IT","20124005")
Aman4 = Riders("Aman4","IT","20124005")
Aman5 = Riders("Aman5","IT","20124005")
Aman6 = Riders("Aman6","IT","20124005")
Aman7 = Riders("Aman7","IT","20124005")
Aman8 = Riders("Aman8","IT","20124005")
Aman9 = Riders("Aman9","IT","20124005")
Aman10 = Riders("Aman10","IT","20124005")
Aman11 = Riders("Aman11","IT","20124005")
Aman12 = Riders("Aman12","IT","20124005")
Aman13 = Riders("Aman13","IT","20124005")
Aman14 = Riders("Aman14","IT","20124005")
Aman15 = Riders("Aman15","IT","20124005")



driver1 = Drivers("Ramkishan1","ABCDEX#33","123456")
driver2 = Drivers("Ramkishan2","ABCDEX#33","123456")
driver3 = Drivers("Ramkishan3","ABCDEX#33","123456")
driver4 = Drivers("Ramkishan4","ABCDEX#33","123456")
driver5 = Drivers("Ramkishan5","ABCDEX#33","123456")
driver6 = Drivers("Ramkishan6","ABCDEX#33","123456")
driver7 = Drivers("Ramkishan7","ABCDEX#33","123456")
driver8 = Drivers("Ramkishan8","ABCDEX#33","123456")



Destination1 = Destination("Jalandhar Bus Stand", "31.31273", "75.59125")
Destination2 = Destination("Jalandhar Railway Station", "31.33098", "75.59051")
Destination3 = Destination("Jalandhar Cantt Railway Station", "31.30734", "75.63121")
Destination4 = Destination("Pathankot Bypass", "31.35448", "75.59066")
Destination5 = Destination("Sarb Multiplex", "31.35786", "75.57962")
Destination6 = Destination("Maqsudan Market Chowk", "31.36042", "75.55226")
Destination7 = Destination("PAP Chowk", "31.31025", "75.61189")
Destination8 = Destination("Jalandhar City Shopping Center", "31.29833", "75.58147")
Destination9 = Destination("PPR Mall", "31.29785", "75.58102")
Destination10 = Destination("Model Town Market Chowk", "31.30689", "75.57931")
Destination11 = Destination("Jyoti chowk", "31.32613", "75.57593")
Destination12 = Destination("Shree Ram Chowk", "31.32533", "75.58009")
Destination13 = Destination("Lal Bahadur Shastri Chowk", "31.32406", "75.58318")
Destination14 = Destination("PVR MBD Mall", "31.31937", "75.58421")
Destination15 = Destination("Ladowali Road", "31.32258", "75.59387")
Destination16 = Destination("Devi Talab Mandir", "31.34354", "75.58277")
Destination17 = Destination("Baba Sodal Mandir", "31.3439", "75.57395")


handler = RequestHandler()

handler.add_Request(Requests(Aman1,Destination1,"12","16"))
handler.add_Request(Requests(Aman2,Destination1,"13","15"))
handler.add_Request(Requests(Aman3,Destination4,"13","16"))
handler.add_Request(Requests(Aman4,Destination3,"14","16"))
handler.add_Request(Requests(Aman5,Destination5,"10","14"))
handler.add_Request(Requests(Aman6,Destination5,"11","15"))
handler.add_Request(Requests(Aman7,Destination4,"12","14"))
handler.add_Request(Requests(Aman8,Destination13,"13","17"))
handler.add_Request(Requests(Aman9,Destination6,"15","17"))
handler.add_Request(Requests(Aman10,Destination7,"13","16"))
handler.add_Request(Requests(Aman11,Destination8,"14","16"))
handler.add_Request(Requests(Aman12,Destination9,"12","17"))
handler.add_Request(Requests(Aman13,Destination10,"15","17"))
handler.add_Request(Requests(Aman14,Destination11,"15","16"))
handler.add_Request(Requests(Aman15,Destination12,"14","18"))

handler.create_groups()
# handler.show_groups()
driver_handler = DriverHandler()

driver_handler.add_to_avaialble(driver1)
driver_handler.add_to_avaialble(driver2)
driver_handler.add_to_avaialble(driver3)
driver_handler.add_to_avaialble(driver4)
driver_handler.add_to_avaialble(driver5)
driver_handler.add_to_avaialble(driver6)
driver_handler.add_to_avaialble(driver7)
driver_handler.add_to_avaialble(driver8)


genrator = CarpoolGenerator(handler,driver_handler)

genrator.divide_into_carpools()