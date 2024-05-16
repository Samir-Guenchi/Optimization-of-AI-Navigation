import random
import csv

# Wilayas and their latitude ranges
wilayas = {
    "Adrar": (2000.000, 25.000), "Chlef": (35.000, 4000.000), "Laghouat": (32.000, 35.000), "Oum El Bouaghi": (35.000, 4000.000),
    "Batna": (35.000, 4000.000), "Béjaïa": (35.000, 4000.000), "Biskra": (3000.000, 35.000), "Béchar": (25.000, 3000.000),
    "Blida": (35.000, 4000.000), "Bouïra": (35.000, 4000.000), "Tamanrasset": (2000.000, 25.000), "Tébessa": (35.000, 4000.000),
    "Tlemcen": (35.000, 4000.000), "Tiaret": (3000.000, 35.000), "Tizi Ouzou": (35.000, 4000.000), "Algiers": (35.000, 4000.000),
    "Djelfa": (3000.000, 35.000), "Jijel": (35.000, 4000.000), "Sétif": (35.000, 4000.000), "Saïda": (25.000, 3000.000),
    "Skikda": (35.000, 4000.000), "Sidi Bel Abbès": (35.000, 4000.000), "Annaba": (35.000, 4000.000), "Guelma": (35.000, 4000.000),
    "Constantine": (35.000, 4000.000), "Médéa": (35.000, 4000.000), "Mostaganem": (35.000, 4000.000), "M'Sila": (3000.000, 35.000),
    "Mascara": (35.000, 4000.000), "Ouargla": (25.000, 3000.000), "Oran": (35.000, 4000.000), "El Bayadh": (3000.000, 35.000),
    "Illizi": (2000.000, 25.000), "Bordj Bou Arréridj": (35.000, 4000.000), "Boumerdes": (35.000, 4000.000), "El Taref": (35.000, 4000.000),
    "Tindouf": (2000.000, 25.000), "Tissemsilt": (35.000, 4000.000), "El Oued": (25.000, 3000.000), "Khenchela": (35.000, 4000.000),
    "Souk Ahras": (35.000, 4000.000), "Tipaza": (35.000, 4000.000), "Mila": (35.000, 4000.000), "Ain Defla": (35.000, 4000.000),
    "Naâma": (25.000, 3000.000), "Ain Timouchent": (35.000, 4000.000), "Ghardaia": (3000.000, 35.000), "Relizane": (35.000, 4000.000),
    "El M'Ghair": (2000.000, 25.000), "El Menia": (2000.000, 25.000), "Ouled Djellal": (3000.000, 35.000),
    "Bordj Baji Mokhtar": (2000.000, 25.000), "Béni Abbès": (25.000, 3000.000), "Timimoun": (25.000, 3000.000),
    "Touggourt": (25.000, 3000.000), "Djanet": (2000.000, 25.000), "In Salah": (25.000, 3000.000), "In Guezzam": (2000.000, 25.000)
}

# Products
products = ["wheat (kg)", "potatoes (kg)", "dates (kg)", "tomatoes (kg)", "citrus (kg)"]

# Generate random data for each season
for season in ["winter", "spring", "summer", "autumn"]:
    with open(f'{season}_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([ 'Wheat', 'Potatoes', 'Dates', 'Tomatoes', 'Citrus'])
        for wilaya, latitude_range in wilayas.items():
            latitude = random.uniform(*latitude_range)
            if season == "winter":
                if latitude >= 35.000:
                    quantities = [random.randint(1000, 50000) for _ in range(5)]  # North
                elif latitude >= 3000.000:
                    quantities = [random.randint(5000, 20000) for _ in range(5)]  # Middle
                else:
                    quantities = [random.randint(1000, 10000) for _ in range(5)]  # South
            elif season == "spring" or season == "autumn":
                if latitude >= 35.000:
                    quantities = [random.randint(8000, 30000) for _ in range(5)]  # North
                elif latitude >= 3000.000:
                    quantities = [random.randint(4000, 15000) for _ in range(5)]  # Middle
                else:
                    quantities = [random.randint(2000, 80000) for _ in range(5)]  # South
            else:  # summer
                if latitude >= 35.000:
                    quantities = [random.randint(1000, 500000) for _ in range(5)]  # North
                elif latitude >= 3000.000:
                    quantities = [random.randint(5000, 20000) for _ in range(5)]  # Middle
                else:
                    quantities = [random.randint(1000, 10000) for _ in range(5)]  # South
            writer.writerow( quantities)
