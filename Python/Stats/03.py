import pandas as pd
import numpy as np
# Create a sample time series DataFrame
date_rng = pd.date_range(start='2023-01-01', end='2023-01-10', freq='D')
data = np.random.randint(0, 100, size=(len(date_rng), 2))
df = pd.DataFrame(data, columns=['A', 'B'], index=date_rng)
# Display the DataFrame
print("Original DataFrame:")
print(df)

#Output
#Original DataFrame:
#A B
#2023-01-01 83 7
#2023-01-02 72 61
#2023-01-03 13 5
#2023-01-04 0 8
#2023-01-05 79 79
#2023-01-06 53 11
#2023-01-07 4 39
#2023-01-08 92 45
#2023-01-09 26 74
#2023-01-10 52 49

daily_mean = df.resample('D').mean()
print("\nDaily Mean:")
print(daily_mean)

# Output
#Daily Mean:
#A B
#2023-01-01 83.0 7.0
#2023-01-02 72.0 61.0
#2023-01-03 13.0 5.0
#2023-01-04 0.0 8.0
#2023-01-05 79.0 79.0
#2023-01-06 53.0 11.0
#2023-01-07 4.0 39.0
#2023-01-08 92.0 45.0
#2023-01-09 26.0 74.0
#2023-01-10 52.0 49.0

		# Multivariate Time Series

# Create a multivariate time series DataFrame
date_rng = pd.date_range(start='2023-01-01', end='2023-01-10', freq='D')
data = {
'Temperature': np.random.randint(20, 30, size=(len(date_rng))),
'Humidity': np.random.randint(30, 70, size=(len(date_rng)))
}
df_multivariate = pd.DataFrame(data, index=date_rng)
# Display the multivariate DataFrame
print("\nMultivariate DataFrame:")
print(df_multivariate)

#Multivariate DataFrame:
#Temperature Humidity
#2023-01-01    23 53
#2023-01-02	23 51
#2023-01-03	29 36
#2023-01-04	22 60
#2023-01-05	25 46
#2023-01-06	22 56
#2023-01-07	23 65
#2023-01-08	25 39	
#2023-01-09	27 43
#2023-01-10	22 36

# Group by day and calculate the mean for each variable
daily_mean_multivariate = df_multivariate.resample('D').mean()
print("\nDaily Mean for Multivariate DataFrame:")
print(daily_mean_multivariate)

#Output-
#Daily Mean for Multivariate DataFrame:
#Temperature Humidity
#2023-01-01    23.0 53.0
#2023-01-02	23.0 51.0
#2023-01-03	29.0 36.0
#2023-01-04	22.0 60.0
#2023-01-05	25.0 46.0
#2023-01-06	22.0 56.0
#2023-01-07	23.0 65.0
#2023-01-08	25.0 39.0
#2023-01-09	27.0 43.0
#2023-01-10	22.0 36.0

			# Forecasting Formats
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt
# Fit anARIMAmodel
model=ARIMA(df['A'], order=(1, 1, 1))
model_fit = model.fit()
# Forecast the next 5 days
forecast = model_fit.forecast(steps=5)
print("\nForecast for the next 5 days:")
print(forecast)

#Output
#Forecast for the next 5 days:
#2023-01-11 45.658360
#2023-01-12 46.916272
#2023-01-13 46.666756
#2023-01-14 46.716249
#2023-01-15 46.706432

# Plot the results
plt.figure(figsize=(10, 5))
plt.plot(df['A'], label='Historical Data')
plt.plot(pd.date_range(start=df.index[-1] + pd.Timedelta(days=1), periods=5), forecast,
label='Forecast', color='red')
plt.title('Time Series Forecasting')
plt.xlabel('Date')
plt.ylabel('Values')
plt.legend()
plt.show()