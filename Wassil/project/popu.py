import csv

# Data
wilayas = {
    "Adrar": 439700, "Chlef": 1013718, "Laghouat": 477328, "Oum El Bouaghi": 644364, "Batna": 1128030,
    "Béjaïa": 915835, "Biskra": 730262, "Béchar": 274866, "Blida": 1009892, "Bouïra": 694750,
    "Tamanrasset": 198691, "Tébessa": 657227, "Tlemcen": 945525, "Tiaret": 842060, "Tizi Ouzou": 1119646,
    "Algiers": 2947461, "Djelfa": 1223223, "Jijel": 634412, "Sétif": 1496150, "Saïda": 328685,
    "Skikda": 904195, "Sidi Bel Abbès": 603369, "Annaba": 640050, "Guelma": 482261, "Constantine": 943112,
    "Médéa": 830943, "Mostaganem": 746947, "M'Sila": 991846, "Mascara": 780959, "Ouargla": 552539,
    "Oran": 1584607, "El Bayadh": 262187, "Illizi": 54490, "Bordj Bou Arréridj": 634396, "Boumerdes": 795019,
    "El Taref": 411783, "Tindouf": 159000, "Tissemsilt": 296366, "El Oued": 673934, "Khenchela": 384268,
    "Souk Ahras": 440299, "Tipaza": 617661, "Mila": 768419, "Ain Defla": 771890, "Naâma": 209470,
    "Ain Timouchent": 384565, "Ghardaia": 375988, "Relizane": 733060, "El M'Ghair": 162267, "El Menia": 57276,
    "Ouled Djellal": 174219, "Bordj Baji Mokhtar": 16437, "Béni Abbès": 50163, "Timimoun": 122019,
    "Touggourt": 247221, "Djanet": 17618, "In Salah": 50392, "In Guezzam": 11202
}

# Calculate total population
total_population = sum(wilayas.values())

# Calculate percentage and create CSV
with open('wilayas_population_percentage.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Wilaya', 'Population', 'Percentage'])
    for wilaya, population in wilayas.items():
        percentage = population / total_population  # Calculate percentage correctly
        writer.writerow([ percentage])

print("CSV file with population percentages created successfully!")
