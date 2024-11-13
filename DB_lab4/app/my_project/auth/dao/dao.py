# app/my_project/auth/dao/dao.py
from app import db
from app.my_project.auth.domain.models import Country, City, WeatherConditionLabel, CityWaterTemperature, DailyWeather, HourlyWeather, WeatherAlert, WeatherForecast, City,UserHasCity ,User, UserHasCity, UserPreferences

class CountryDAO:
    @staticmethod
    def get_all():
        return Country.query.all()

    @staticmethod
    def get_by_id(id_country):
        return Country.query.get(id_country)

    @staticmethod
    def create(country_data):
        new_country = Country(**country_data)
        db.session.add(new_country)
        db.session.commit()
        return new_country

    @staticmethod
    def update(id_country, update_data):
        country = Country.query.get(id_country)
        if country:
            for key, value in update_data.items():
                setattr(country, key, value)
            db.session.commit()
        return country

    @staticmethod
    def delete(id_country):
        country = Country.query.get(id_country)
        if country:
            db.session.delete(country)
            db.session.commit()

class CityDAO:
    @staticmethod
    def get_all():
        return City.query.all()

    @staticmethod
    def get_by_id(id_city):
        return City.query.get(id_city)

    @staticmethod
    def create(city_data):
        new_city = City(**city_data)
        db.session.add(new_city)
        db.session.commit()
        return new_city

    @staticmethod
    def update(id_city, update_data):
        city = City.query.get(id_city)
        if city:
            for key, value in update_data.items():
                setattr(city, key, value)
            db.session.commit()
        return city

    @staticmethod
    def delete(id_city):
        city = City.query.get(id_city)
        if city:
            db.session.delete(city)
            db.session.commit()
    @staticmethod
    def get_cities_by_country(id_country):
        return City.query.filter_by(country_id_country=id_country).all()

class WeatherConditionLabelDAO:
    @staticmethod
    def get_all():
        return WeatherConditionLabel.query.all()

    @staticmethod
    def get_by_id(id_label):
        return WeatherConditionLabel.query.get(id_label)

    @staticmethod
    def create(label_data):
        new_label = WeatherConditionLabel(**label_data)
        db.session.add(new_label)
        db.session.commit()
        return new_label

class DailyWeatherDAO:
    @staticmethod
    def get_all():
        return DailyWeather.query.all()

    @staticmethod
    def get_by_id(id_daily_weather):
        return DailyWeather.query.get(id_daily_weather)

    @staticmethod
    def create(daily_weather_data):
        new_daily_weather = DailyWeather(**daily_weather_data)
        db.session.add(new_daily_weather)
        db.session.commit()
        return new_daily_weather

    @staticmethod
    def update(id_daily_weather, update_data):
        daily_weather = DailyWeather.query.get(id_daily_weather)
        if daily_weather:
            for key, value in update_data.items():
                setattr(daily_weather, key, value)
            db.session.commit()
        return daily_weather

    @staticmethod
    def delete(id_daily_weather):
        daily_weather = DailyWeather.query.get(id_daily_weather)
        if daily_weather:
            db.session.delete(daily_weather)
            db.session.commit()

class HourlyWeatherDAO:
    @staticmethod
    def get_all():
        return HourlyWeather.query.all()

    @staticmethod
    def get_by_id(id_hourly_weather):
        return HourlyWeather.query.get(id_hourly_weather)

    @staticmethod
    def create(hourly_weather_data):
        new_hourly_weather = HourlyWeather(**hourly_weather_data)
        db.session.add(new_hourly_weather)
        db.session.commit()
        return new_hourly_weather

    @staticmethod
    def update(id_hourly_weather, update_data):
        hourly_weather = HourlyWeather.query.get(id_hourly_weather)
        if hourly_weather:
            for key, value in update_data.items():
                setattr(hourly_weather, key, value)
            db.session.commit()
        return hourly_weather

    @staticmethod
    def delete(id_hourly_weather):
        hourly_weather = HourlyWeather.query.get(id_hourly_weather)
        if hourly_weather:
            db.session.delete(hourly_weather)
            db.session.commit()

class WeatherAlertDAO:
    @staticmethod
    def get_all():
        return WeatherAlert.query.all()

    @staticmethod
    def get_by_id(id_alert):
        return WeatherAlert.query.get(id_alert)

    @staticmethod
    def create(alert_data):
        new_alert = WeatherAlert(**alert_data)
        db.session.add(new_alert)
        db.session.commit()
        return new_alert

    @staticmethod
    def delete(id_alert):
        alert = WeatherAlert.query.get(id_alert)
        if alert:
            db.session.delete(alert)
            db.session.commit()

class WeatherForecastDAO:
    @staticmethod
    def get_all():
        return WeatherForecast.query.all()

    @staticmethod
    def get_by_id(id_forecast):
        return WeatherForecast.query.get(id_forecast)

    @staticmethod
    def create(forecast_data):
        new_forecast = WeatherForecast(**forecast_data)
        db.session.add(new_forecast)
        db.session.commit()
        return new_forecast

    @staticmethod
    def update(id_forecast, update_data):
        forecast = WeatherForecast.query.get(id_forecast)
        if forecast:
            for key, value in update_data.items():
                setattr(forecast, key, value)
            db.session.commit()
        return forecast

    @staticmethod
    def delete(id_forecast):
        forecast = WeatherForecast.query.get(id_forecast)
        if forecast:
            db.session.delete(forecast)
            db.session.commit()

class UserDAO:
    @staticmethod
    def get_all():
        return User.query.all()

    @staticmethod
    def get_by_id(id_user):
        return User.query.get(id_user)

    @staticmethod
    def create(user_data):
        new_user = User(**user_data)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def add_city_to_user(id_user, id_city):
        user_city_link = UserHasCity(user_id_user=id_user, city_id_city=id_city)
        db.session.add(user_city_link)
        db.session.commit()
        return True

    @staticmethod
    def get_cities_by_user(id_user):
        user = User.query.get(id_user)
        return user.cities if user else []

class UserPreferencesDAO:
    @staticmethod
    def get_all():
        return UserPreferences.query.all()

    @staticmethod
    def get_by_id(id_user_preferences):
        return UserPreferences.query.get(id_user_preferences)

    @staticmethod
    def create(data):
        new_preference = UserPreferences(**data)
        db.session.add(new_preference)
        db.session.commit()
        return new_preference
