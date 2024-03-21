# Subsistema

class FlightBookingSystem:
    def book_flight(self, origin, destination, date):
        return f"Voo de {origin} para {destination} no dia {date} agendado!"

class HotelBookingSystem:
    def book_hotel(self, destination, check_in_date, check_out_date):
        return f"Hotel em {destination} agendado de {check_in_date} até {check_out_date}!"

class CarRentalSystem:
    def rent_car(self, location, start_date, end_date):
        return f"Carro alugado em {location} de {start_date} até {end_date}!"

# Facade

class TravelBookingFacade:
    def __init__(self):
        self._flight_booking = FlightBookingSystem()
        self._hotel_booking = HotelBookingSystem()
        self._car_rental = CarRentalSystem()

    def book_trip(self, origin, destination, date, check_in_date, check_out_date, start_date, end_date):
        flight = self._flight_booking.book_flight(origin, destination, date)
        hotel = self._hotel_booking.book_hotel(destination, check_in_date, check_out_date)
        car = self._car_rental.rent_car(destination, start_date, end_date)
        return f"Viagem agendada:\n{flight}\n{hotel}\n{car}"

# Cliente

def main():

    facade = TravelBookingFacade()

    # Viagem em modelo:
    # trip = facade.book_trip(origem, destino, data do voo, data de check-in, data de check-out, data de aluguel do carro, data de devolvimento do carro)
    # print(trip)

    trip = facade.book_trip("Rio de Janeiro", "Londres", "2024-03-10", "2024-03-11", "2024-03-20", "2024-03-12", "2024-03-19")
    print(trip)

if __name__ == "__main__":
    main()

# Neste código, um conjunto de funcionalidades e subsistemas são escondidos pelo padrão de facade.
# O cliente apenas precisa preencher as informações de sua viagem, sem se preocupar com detalhes de funcionamento.