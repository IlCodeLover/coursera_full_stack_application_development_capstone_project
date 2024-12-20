from .models import CarModel, CarMake
# Populate data in your database
def initiate():
    #print("Populate not implemented. Add data manually")
    car_make_data = [
        {"name":"NISSAN", "description":"Japanese tech"},
        {"name":"Mercedes", "description":"German tech"},
        {"name":"Audi", "description":"German tech"},
        {"name":"Kia", "description":"Korean tech"},
        {"name":"Toyota", "description":"Japanese tech"},
    ]

    car_make_instances = []

    for data in car_make_data:
        car_make_instances.append(CarMake.objects.create(name=data['name'],
                                                          description=data['description']))

    # Create CarModel instances with the corresponding CarMake instances
    car_model_data = [
        {"name":"Pathfinder", "type":"SUV", "year":2023, "car_make":car_make_instances[0]},
        {"name":"A-Class", "type":"SUV", "year":2023, "car_make":car_make_instances[1]},
        {"name":"C-Class", "type":"SUV", "year":2023, "car_make":car_make_instances[1]},
        {"name":"A4", "type":"SUV", "year":2023, "car_make":car_make_instances[2]},
        {"name":"Cerato", "type":"Sedan", "year":2023, "car_make":car_make_instances[3]},
        {"name":"Corolla", "type":"Sedan", "year":2023, "car_make":car_make_instances[4]},
        {"name":"Camry", "type":"Sedan", "year":2023, "car_make":car_make_instances[4]},
    ]

    for data in car_model_data:
        CarModel.objects.create(name=data['name'],
                                 type=data['type'],
                                 year=data['year'],
                                 car_make=data['car_make']
                                 )

