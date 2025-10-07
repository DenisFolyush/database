
try:
    from .service import CountryService, CityService  # твій фактичний файл з класами
except Exception as e:
    # щоб у логах було видно першопричину, якщо раптом класів нема
    raise
