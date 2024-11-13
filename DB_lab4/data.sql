INSERT INTO `country` (`id_country`, `name`, `code`) VALUES 
(1, 'Ukraine', 'UA'),
(2, 'France', 'FE'),
(3, 'Spain', 'ES');

-- Insert data for `city`
INSERT INTO `city` (`id_city`, `longitude`, `latitude`, `name`, `country_id_country`) VALUES 
(1, 50.45, 30.52, 'Kyiv', 1),
(2, 48.85, 2.35, 'Paris', 2),
(3, 40.42, -3.70, 'Madrid', 3),
(4, 46.48, 30.73, 'Odessa', 1),
(5, 41.38, 2.17, 'Barcelona', 3);

-- Insert data for `weather_condition_label`
INSERT INTO `weather_condition_label` (`id_weather_condition_label`, `label`) VALUES 
(1, 'Sunny'),
(2, 'Rainy'),
(3, 'Cloudy'),
(4, 'Stormy'),
(5, 'Snowy');

-- Insert data for `daily_weather`
INSERT INTO `daily_weather` (`id_daily_weather`, `date`, `min_temp`, `max_temp`, `water_temp`, `wind_speed`, `humidity`, `weather_condition_label_id`, `city_id_city`) VALUES 
(1, '2024-09-01', 15.0, 25.0, 23.0, 10.5, 55, 1, 1),
(2, '2024-09-01', 18.5, 28.0, 25.0, 12.0, 60, 2, 2),
(3, '2024-09-02', 22.0, 30.0, 26.0, 8.0, 40, 1, 3),
(4, '2024-09-01', 19.0, 27.0, 22.0, 14.0, 70, 4, 4),
(5, '2024-09-03', 21.5, 29.5, 27.5, 9.5, 50, 3, 5);

-- Insert data for `hourly_weather`
INSERT INTO `hourly_weather` (`id_hourly_weather`, `date`, `hour`, `temperature`, `wind_speed`, `weather_condition_label_id`, `city_id_city`) VALUES 
(1, '2024-09-01', 9, 22.0, 8.5, 1, 1),
(2, '2024-09-01', 12, 25.5, 10.0, 3, 1),
(3, '2024-09-01', 15, 27.0, 12.0, 2, 2),
(4, '2024-09-01', 9, 29.0, 9.5, 1, 3),
(5, '2024-09-01', 18, 26.0, 15.0, 4, 4);

-- Insert data for `user`
INSERT INTO `user` (`id_user`, `name`, `email`, `password`) VALUES 
(1, 'Bob', 'Bob@gmail.com', 'bib'),
(2, 'Bib', 'Bib@gmail.com', 'bib'),
(3, 'Boll', 'Boll@gmail.com', 'bib'),
(4, 'Bill', 'Bill@gmail.com', 'bib'),
(5, 'Bell', 'Bell@gmail.com', 'bib');

-- Insert data for `user_has_city`
INSERT INTO `user_has_city` (`user_id_user`, `city_id_city`) VALUES 
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);

-- Insert data for `user_preferences`
INSERT INTO `user_preferences` (`id_user_preferences`, `preference`, `user_id_user`) VALUES 
(1, 'Storm Alerts', 1),
(2, 'Heatwave Alerts', 2),
(3, 'Flood Alerts', 3),
(4, 'Snow Alerts', 4),
(5, 'Rain Alerts', 5);

-- Insert data for `weather_alert`
INSERT INTO `weather_alert` (`id_weather_alert`, `alert_type`, `start_time`, `end_time`, `description`, `city_id_city`) VALUES 
(1, 'Storm', '2024-09-01 14:00', '2024-09-01 18:00', 'Strong storm in the area', 1),
(2, 'Flood', '2024-09-02 09:00', '2024-09-02 20:00', 'Heavy rain causing floods', 2),
(3, 'Heatwave', '2024-09-03 19:00', '2024-09-03 19:00', 'Heatwave with high temperatures', 3),
(4, 'Storm', '2024-09-04 22:00', '2024-09-04 22:00', 'Windy storm approaching', 4),
(5, 'Blizzard', '2024-09-05 08:00', '2024-09-05 16:00', 'Severe snowstorm expected', 5);

-- Insert data for `weather_forecast`
INSERT INTO `weather_forecast` (`id_weather_forecast`, `forecast_date`, `validity_days`, `min_temp`, `max_temp`, `wind_speed`, `humidity`, `weather_condition_label_id`, `city_id_city`) VALUES 
(1, '2024-09-01', 1, 15.0, 25.0, 10.0, 55, 1, 1),
(2, '2024-09-02', 2, 19.5, 27.5, 11.5, 60, 2, 2),
(3, '2024-09-03', 7, 20.0, 29.0, 8.0, 45, 3, 3),
(4, '2024-09-04', 14, 21.5, 31.0, 9.5, 50, 1, 4),
(5, '2024-09-05', 1, 22.0, 28.5, 14.0, 70, 5, 5);
-- Insert data for `city_water_temperature`
INSERT INTO `city_water_temperature` (`id_city_water_temperature`, `water_temp`, `date`, `city_id_city`) VALUES 
(1, 20.5, '2024-09-01', 1), -- Kyiv
(2, 22.3, '2024-09-02', 1), -- Kyiv
(3, 19.0, '2024-09-01', 2), -- Paris
(4, 23.7, '2024-09-03', 3), -- Madrid
(5, 24.1, '2024-09-01', 4), -- Odessa
(6, 21.4, '2024-09-04', 5); -- Barcelona