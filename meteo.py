import meteofrance_api as mf

LeTouquet = { "Lat" : "50.521276",
          "Long" : "1.590675"}

Gennevilliers = { "Lat" : "48.925525",
          "Long" : "2.293275"}

client = mf.MeteoFranceClient()

def meteo(ville):
    meteo_ville = client.get_forecast(ville["Lat"],ville["Long"],'fr')
    temperature = meteo_ville.current_forecast['T']['value']
    temps = meteo_ville.current_forecast['weather']['desc']

    return {
        "temps" : temps,
        "temperature" : temperature
    }
