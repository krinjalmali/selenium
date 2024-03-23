from booking.booking import Booking

with Booking() as booking:
    booking.land_first_page()
    booking.change_currency()

