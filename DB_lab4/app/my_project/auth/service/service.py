# app/my_project/auth/service/service.py

from app.my_project.auth.dao.dao import CountryDAO, CityDAO, WeatherConditionLabelDAO, DailyWeatherDAO, HourlyWeatherDAO, WeatherAlertDAO, WeatherForecastDAO,UserDAO, UserPreferencesDAO

class CountryService:
    @staticmethod
    def get_all_countries():
        return CountryDAO.get_all()

    @staticmethod
    def get_country_by_id(id_country):
        return CountryDAO.get_by_id(id_country)

    @staticmethod
    def create_country(country_data):
        return CountryDAO.create(country_data)

    @staticmethod
    def update_country(id_country, update_data):
        return CountryDAO.update(id_country, update_data)

    @staticmethod
    def delete_country(id_country):
        CountryDAO.delete(id_country)

class CityService:
    @staticmethod
    def get_all_cities():
        return CityDAO.get_all()

    @staticmethod
    def get_city_by_id(id_city):
        return CityDAO.get_by_id(id_city)

    @staticmethod
    def create_city(city_data):
        return CityDAO.create(city_data)

    @staticmethod
    def update_city(id_city, update_data):
        return CityDAO.update(id_city, update_data)

    @staticmethod
    def delete_city(id_city):
        CityDAO.delete(id_city)
    @staticmethod
    def get_cities_by_country(id_country):
        return CityDAO.get_cities_by_country(id_country)


class WeatherConditionLabelService:
    @staticmethod
    def get_all_labels():
        return WeatherConditionLabelDAO.get_all()

    @staticmethod
    def get_label_by_id(id_label):
        return WeatherConditionLabelDAO.get_by_id(id_label)

    @staticmethod
    def create_label(label_data):
        return WeatherConditionLabelDAO.create(label_data)

class DailyWeatherService:
    @staticmethod
    def get_all_daily_weather():
        return DailyWeatherDAO.get_all()

    @staticmethod
    def get_daily_weather_by_id(id_daily_weather):
        return DailyWeatherDAO.get_by_id(id_daily_weather)

    @staticmethod
    def create_daily_weather(daily_weather_data):
        return DailyWeatherDAO.create(daily_weather_data)

    @staticmethod
    def update_daily_weather(id_daily_weather, update_data):
        return DailyWeatherDAO.update(id_daily_weather, update_data)

    @staticmethod
    def delete_daily_weather(id_daily_weather):
        DailyWeatherDAO.delete(id_daily_weather)

class HourlyWeatherService:
    @staticmethod
    def get_all_hourly_weather():
        return HourlyWeatherDAO.get_all()

    @staticmethod
    def get_hourly_weather_by_id(id_hourly_weather):
        return HourlyWeatherDAO.get_by_id(id_hourly_weather)

    @staticmethod
    def create_hourly_weather(hourly_weather_data):
        return HourlyWeatherDAO.create(hourly_weather_data)

    @staticmethod
    def update_hourly_weather(id_hourly_weather, update_data):
        return HourlyWeatherDAO.update(id_hourly_weather, update_data)

    @staticmethod
    def delete_hourly_weather(id_hourly_weather):
        HourlyWeatherDAO.delete(id_hourly_weather)

class WeatherAlertService:
    @staticmethod
    def get_all_alerts():
        return WeatherAlertDAO.get_all()

    @staticmethod
    def get_alert_by_id(id_alert):
        return WeatherAlertDAO.get_by_id(id_alert)

    @staticmethod
    def create_alert(alert_data):
        return WeatherAlertDAO.create(alert_data)

    @staticmethod
    def delete_alert(id_alert):
        WeatherAlertDAO.delete(id_alert)

class WeatherForecastService:
    @staticmethod
    def get_all_forecasts():
        return WeatherForecastDAO.get_all()

    @staticmethod
    def get_forecast_by_id(id_forecast):
        return WeatherForecastDAO.get_by_id(id_forecast)

    @staticmethod
    def create_forecast(forecast_data):
        return WeatherForecastDAO.create(forecast_data)

    @staticmethod
    def update_forecast(id_forecast, update_data):
        return WeatherForecastDAO.update(id_forecast, update_data)

    @staticmethod
    def delete_forecast(id_forecast):
        WeatherForecastDAO.delete(id_forecast)


class UserService:
    @staticmethod
    def get_all():
        return UserDAO.get_all()

    @staticmethod
    def get_by_id(id_user):
        return UserDAO.get_by_id(id_user)

    @staticmethod
    def create(user_data):
        return UserDAO.create(user_data)

    @staticmethod
    def add_city_to_user(id_user, id_city):
        return UserDAO.add_city_to_user(id_user, id_city)

    @staticmethod
    def get_cities_by_user(id_user):
        return UserDAO.get_cities_by_user(id_user)

class UserPreferencesService:
    @staticmethod
    def get_all():
        return UserPreferencesDAO.get_all()

    @staticmethod
    def get_by_id(id_user_preferences):
        return UserPreferencesDAO.get_by_id(id_user_preferences)

    @staticmethod
    def create(data):
        return UserPreferencesDAO.create(data)
