# app/my_project/auth/domain/models.py
from app import db

class Country(db.Model):
    __tablename__ = 'country'
    id_country = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), unique=True, nullable=False)
    code = db.Column(db.String(5), unique=True, nullable=False)

    cities = db.relationship('City', backref='country', lazy=True, cascade="all, delete-orphan")

    def to_dict(self):
        return {"id_country": self.id_country, "name": self.name, "code": self.code}

class City(db.Model):
    __tablename__ = 'city'
    id_city = db.Column(db.Integer, primary_key=True)
    longitude = db.Column(db.Numeric(9, 6), nullable=False)
    latitude = db.Column(db.Numeric(9, 6), nullable=False)
    name = db.Column(db.String(45), nullable=False)
    country_id_country = db.Column(db.Integer, db.ForeignKey('country.id_country', ondelete='CASCADE'))

    daily_weathers = db.relationship('DailyWeather', backref='city', lazy=True, cascade="all, delete-orphan")
    hourly_weathers = db.relationship('HourlyWeather', backref='city', lazy=True, cascade="all, delete-orphan")
    water_temperatures = db.relationship('CityWaterTemperature', backref='city', lazy=True, cascade="all, delete-orphan")
    alerts = db.relationship('WeatherAlert', backref='city', lazy=True, cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id_city": self.id_city,
            "longitude": str(self.longitude),
            "latitude": str(self.latitude),
            "name": self.name,
            "country_id_country": self.country_id_country
        }

class WeatherConditionLabel(db.Model):
    __tablename__ = 'weather_condition_label'
    id_weather_condition_label = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(45), nullable=False)

    def to_dict(self):
        return {"id_weather_condition_label": self.id_weather_condition_label, "label": self.label}

class CityWaterTemperature(db.Model):
    __tablename__ = 'city_water_temperature'
    id_city_water_temperature = db.Column(db.Integer, primary_key=True)
    water_temp = db.Column(db.Numeric(5, 2), nullable=False)
    date = db.Column(db.Date, nullable=False)
    city_id_city = db.Column(db.Integer, db.ForeignKey('city.id_city', ondelete='CASCADE'))

    def to_dict(self):
        return {
            "id_city_water_temperature": self.id_city_water_temperature,
            "water_temp": str(self.water_temp),
            "date": self.date,
            "city_id_city": self.city_id_city
        }

class DailyWeather(db.Model):
    __tablename__ = 'daily_weather'
    id_daily_weather = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    min_temp = db.Column(db.Numeric(5, 2), nullable=False)
    max_temp = db.Column(db.Numeric(5, 2), nullable=False)
    water_temp = db.Column(db.Numeric(5, 2), nullable=False)
    wind_speed = db.Column(db.Numeric(5, 2), nullable=False)
    humidity = db.Column(db.Numeric(5, 2), nullable=False)
    weather_condition_label_id = db.Column(db.Integer, db.ForeignKey('weather_condition_label.id_weather_condition_label'))
    city_id_city = db.Column(db.Integer, db.ForeignKey('city.id_city', ondelete='CASCADE'))

    def to_dict(self):
        return {
            "id_daily_weather": self.id_daily_weather,
            "date": self.date,
            "min_temp": str(self.min_temp),
            "max_temp": str(self.max_temp),
            "water_temp": str(self.water_temp),
            "wind_speed": str(self.wind_speed),
            "humidity": str(self.humidity),
            "weather_condition_label_id": self.weather_condition_label_id,
            "city_id_city": self.city_id_city
        }

class HourlyWeather(db.Model):
    __tablename__ = 'hourly_weather'
    id_hourly_weather = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    hour = db.Column(db.Integer, nullable=False)
    temperature = db.Column(db.Numeric(5, 2), nullable=False)
    wind_speed = db.Column(db.Numeric(5, 2), nullable=False)
    weather_condition_label_id = db.Column(db.Integer, db.ForeignKey('weather_condition_label.id_weather_condition_label'))
    city_id_city = db.Column(db.Integer, db.ForeignKey('city.id_city', ondelete='CASCADE'))

    def to_dict(self):
        return {
            "id_hourly_weather": self.id_hourly_weather,
            "date": self.date,
            "hour": self.hour,
            "temperature": str(self.temperature),
            "wind_speed": str(self.wind_speed),
            "weather_condition_label_id": self.weather_condition_label_id,
            "city_id_city": self.city_id_city
        }

class WeatherAlert(db.Model):
    __tablename__ = 'weather_alert'
    id_weather_alert = db.Column(db.Integer, primary_key=True)
    alert_type = db.Column(db.String(255), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.Text, nullable=False)
    city_id_city = db.Column(db.Integer, db.ForeignKey('city.id_city', ondelete='CASCADE'))

    def to_dict(self):
        return {
            "id_weather_alert": self.id_weather_alert,
            "alert_type": self.alert_type,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "description": self.description,
            "city_id_city": self.city_id_city
        }

class WeatherForecast(db.Model):
    __tablename__ = 'weather_forecast'
    id_weather_forecast = db.Column(db.Integer, primary_key=True)
    forecast_date = db.Column(db.Date, nullable=False)
    validity_days = db.Column(db.Integer, nullable=False)
    min_temp = db.Column(db.Numeric(5, 2), nullable=False)
    max_temp = db.Column(db.Numeric(5, 2), nullable=False)
    wind_speed = db.Column(db.Numeric(5, 2), nullable=False)
    humidity = db.Column(db.Numeric(5, 2), nullable=False)
    weather_condition_label_id = db.Column(db.Integer, db.ForeignKey('weather_condition_label.id_weather_condition_label'))
    city_id_city = db.Column(db.Integer, db.ForeignKey('city.id_city', ondelete='CASCADE'))

    def to_dict(self):
        return {
            "id_weather_forecast": self.id_weather_forecast,
            "forecast_date": self.forecast_date,
            "validity_days": self.validity_days,
            "min_temp": str(self.min_temp),
            "max_temp": str(self.max_temp),
            "wind_speed": str(self.wind_speed),
            "humidity": str(self.humidity),
            "weather_condition_label_id": self.weather_condition_label_id,
            "city_id_city": self.city_id_city
        }
from app import db

class User(db.Model):
    __tablename__ = 'user'
    id_user = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    
    # Зв'язок багато-до-багатьох з таблицею City через user_has_city
    cities = db.relationship('City', secondary='user_has_city', backref=db.backref('users', lazy=True))

    def to_dict(self):
        return {
            "id_user": self.id_user,
            "name": self.name,
            "email": self.email
        }

class UserHasCity(db.Model):
    __tablename__ = 'user_has_city'
    user_id_user = db.Column(db.Integer, db.ForeignKey('user.id_user', ondelete='CASCADE'), primary_key=True)
    city_id_city = db.Column(db.Integer, db.ForeignKey('city.id_city', ondelete='CASCADE'), primary_key=True)

class UserPreferences(db.Model):
    __tablename__ = 'user_preferences'
    id_user_preferences = db.Column(db.Integer, primary_key=True)
    preference = db.Column(db.String(255), nullable=False)
    user_id_user = db.Column(db.Integer, db.ForeignKey('user.id_user', ondelete='CASCADE'))

    def to_dict(self):
        return {
            "id_user_preferences": self.id_user_preferences,
            "preference": self.preference,
            "user_id_user": self.user_id_user
        }
