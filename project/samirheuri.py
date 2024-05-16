import csv
from math import sqrt

# Wilaya names and IDs
wilaya_names = {
    "1": "Adrar", "2": "Chlef", "3": "Laghouat", "4": "Oum El Bouaghi",
    "5": "Batna", "6": "Béjaïa", "7": "Biskra", "8": "Bechar",
    "9": "Blida", "10": "Bouira", "11": "Tamanrasset", "12": "Tbessa",
    "13": "Tlemcen", "14": "Tiaret", "15": "Tizi Ouzou", "16": "Alger",
    "17": "Djelfa", "18": "Jijel", "19": "Sétif", "20": "Saïda",
    "21": "Skikda", "22": "Sidi Bel Abbès", "23": "Annaba", "24": "Guelma",
    "25": "Constantine", "26": "Médéa", "27": "Mostaganem", "28": "M'Sila",
    "29": "Mascara", "30": "Ouargla", "31": "Oran", "32": "El Bayadh",
    "33": "Illizi", "34": "Bordj Bou Arréridj", "35": "Boumerdès",
    "36": "El Tarf", "37": "Tindouf", "38": "Tissemsilt", "39": "El Oued",
    "40": "Khenchela", "41": "Souk Ahras", "42": "Tipaza", "43": "Mila",
    "44": "Aïn Defla", "45": "Naâma", "46": "Aïn Témouchent",
    "47": "Ghardaïa", "48": "Relizane", "49": "El M'ghair", "50": "El Menia",
    "51": "Ouled Djellal", "52": "Bordj Baji Mokhtar", "53": "Béni Abbès",
    "54": "Timimoun", "55": "Touggourt", "56": "Djanet", "57": "In Salah",
    "58": "In Guezzam"
}

# Wilaya coordinates
wilaya_coords = {
    "1": {"latitude": 27.9766155, "longitude": -0.20396},
    "2": {"latitude": 36.1691245, "longitude": 1.3539002},
    "3": {"latitude": 33.7873735, "longitude": 2.8829115},
    "4": {"latitude": 35.8726014, "longitude": 7.1180248},
    "5": {"latitude": 35.32147, "longitude": 3.1066502},
    "6": {"latitude": 36.7695969, "longitude": 5.0085855},
    "7": {"latitude": 34.8515041, "longitude": 5.7246709},
    "8": {"latitude": 31.5977602, "longitude": -1.8540446},
    "9": {"latitude": 36.4803023, "longitude": 2.8009379},
    "10": {"latitude": 36.2084234, "longitude": 3.925049},
    "11": {"latitude": 22.2746227, "longitude": 5.6754684},
    "12": {"latitude": 35.4117259, "longitude": 8.110545},
    "13": {"latitude": 34.8959541, "longitude": -1.3150979},
    "14": {"latitude": 35.3599899, "longitude": 1.3916159},
    "15": {"latitude": 36.7002068, "longitude": 4.075957},
    "16": {"latitude": 36.7538259, "longitude": 3.057841},
    "17": {"latitude": 34.6672467, "longitude": 3.2993118},
    "18": {"latitude": 36.7962714, "longitude": 5.7504845},
    "19": {"latitude": 36.1905173, "longitude": 5.4202134},
    "20": {"latitude": 34.841945, "longitude": 0.1483583},
    "21": {"latitude": 36.8777912, "longitude": 6.9357204},
    "22": {"latitude": 35.206334, "longitude": -0.6301368},
    "23": {"latitude": 36.9184345, "longitude": 7.7452755},
    "24": {"latitude": 36.4569088, "longitude": 7.4334312},
    "25": {"latitude": 36.319475, "longitude": 6.7370571},
    "26": {"latitude": 36.2838408, "longitude": 2.7728462},
    "27": {"latitude": 35.9751841, "longitude": 0.1149273},
    "28": {"latitude": 35.7211476, "longitude": 4.5187283},
    "29": {"latitude": 35.382998, "longitude": 0.1542592},
    "30": {"latitude": 32.1961967, "longitude": 4.9634113},
    "31": {"latitude": 35.7066928, "longitude": -0.6405861},
    "32": {"latitude": 32.5722756, "longitude": 0.950011},
    "33": {"latitude": 26.5065999, "longitude": 8.480587},
    "34": {"latitude": 36.0686488, "longitude": 4.7691823},
    "35": {"latitude": 36.7564181, "longitude": 3.4917212},
    "36": {"latitude": 36.7534258, "longitude": 8.2984543},
    "37": {"latitude": 27.2460501, "longitude": -6.3252899},
    "38": {"latitude": 35.6021906, "longitude": 1.802187},
    "39": {"latitude": 33.3714492, "longitude": 6.8573436},
    "40": {"latitude": 35.4263293, "longitude": 7.1414137},
    "41": {"latitude": 36.277849, "longitude": 7.9592299},
    "42": {"latitude": 36.5980966, "longitude": 2.4085379},
    "43": {"latitude": 36.4514882, "longitude": 6.2487316},
    "44": {"latitude": 36.1283915, "longitude": 2.1772514},
    "45": {"latitude": 33.1995605, "longitude": -0.8021968},
    "46": {"latitude": 35.404044, "longitude": -1.0580975},
    "47": {"latitude": 32.5891743, "longitude": 3.7455655},
    "48": {"latitude": 35.8050195, "longitude": 0.867381},
    "49": {"latitude": 33.947222, "longitude": 5.922222},
    "50": {"latitude": 30.579167, "longitude": 2.879167},
    "51": {"latitude": 34.433333, "longitude": 5.066667},
    "52": {"latitude": 21.327778, "longitude": 0.955556},
    "53": {"latitude": 30.133333, "longitude": -2.166667},
    "54": {"latitude": 29.258333, "longitude": 0.230556},
    "55": {"latitude": 33.108333, "longitude": 6.063889},
    "56": {"latitude": 24.554167, "longitude": 9.484722},
    "57": {"latitude": 27.197222, "longitude": 2.483333},
    "58": {"latitude": 19.572222, "longitude": 5.769444}
}

# Calculate Euclidean distance
def euclidean(lat1, lon1, lat2, lon2):
    return sqrt((lat2 - lat1)**2 + (lon2 - lon1)**2)

# Write data to CSV file
with open("wilaya_distancesv.csv", mode="w", newline="") as file:
    writer = csv.writer(file, delimiter=' ')
    writer.writerow(["Wilaya ID", "Wilaya", "All Wilayas (ID: Distance km)"])
    for wilaya_id, coords in wilaya_coords.items():
        distances = [(other_id, 0.0 if wilaya_id == other_id else euclidean(coords["latitude"], coords["longitude"], other_coords["latitude"], other_coords["longitude"])) for other_id, other_coords in wilaya_coords.items()]
        distances.sort(key=lambda x: int(x[0]))  # Sort distances based on wilaya ID
        combined_string = " ".join([f"{distance:.2f}" for other_id, distance in distances])
        writer.writerow([combined_string])

print("CSV file created successfully.")
