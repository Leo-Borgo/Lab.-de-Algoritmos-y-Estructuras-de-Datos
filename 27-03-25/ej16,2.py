import os, time, random
os.system("cls")

rios = {
    "amazonas": "Brasil",
    "nilo": "Egipto",
    "yangtse": "China"
}

for key, value in rios.items():
    print(f"{key}, {value}", ":"), time.sleep(0.5)
    if key == rios["amazonas"]:
        print("El río Amazonas, el más caudaloso del mundo, recorre América del Sur y atraviesa varios países, siendo Brasil el principal por donde fluye.\n"), time.sleep(1)
    elif key == rios["nilo"]:
        print("El río Nilo, el segundo más largo del mundo, es fundamental para la vida en Egipto y Sudán, proporcionando agua en una región predominantemente desértica.\n"), time.sleep(1)
    else:
        print("El río Yangtsé, el más largo de Asia, fluye a través de China y es vital para la economía y la agricultura del país.\n"), time.sleep(1)
