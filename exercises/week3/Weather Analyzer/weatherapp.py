import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class WeatherApp:
    def __init__(self, csv_file):
        self.df = self.load_data(csv_file)
        self.clean_data()

    def load_data(self, csv_file):
        df = pd.read_csv(csv_file, index_col="Date", parse_dates=True)
        df.sort_index(inplace=True)
        return df

    def clean_data(self):
        self.df.dropna(inplace=True)
        self.df.drop_duplicates(inplace=True)

    def calculate_average_temperature(self):
        monthly_avg_temp = self.df["Temperature"].resample("ME").mean()
        return monthly_avg_temp

    def data_visualization(self):
        plt.plot(self.df.index, self.df["Temperature"], label="Temperature")
        plt.title("Temperaturtrend över tid")
        plt.xlabel("Date")
        plt.xticks(rotation=25)
        plt.ylabel("Temperature")
        plt.savefig("Temperaturtrend_över_tid.png")
        plt.close()

        plt.bar(self.df.index, self.df["Precipitation"], color="maroon", width=0.4)
        plt.title("månatlig nederbörd")
        plt.xlabel("Date")
        plt.xticks(rotation=25)
        plt.ylabel("Precipitation")
        plt.savefig("månatlig_nederbörd.png")
        plt.close()

        plt.scatter(self.df["Temperature"], self.df["Humidity"])
        plt.title("temperatur vs luftfuktighet")
        plt.xlabel("Temperature")
        plt.ylabel("Humidity")
        plt.savefig("Temperature_vs_Humidity.png")
        plt.close()

        sns.heatmap(self.df.corr(), annot=True, cmap="coolwarm", linewidths=0.5)
        plt.xticks(rotation=25)
        plt.yticks(rotation=25)
        plt.title("Correlation Matrix")
        plt.savefig("korrelation_heat_map.png")
        plt.close()

    def calculate_temperature_moving_avarage(self):
        self.df["MATemperature"] = self.df["Temperature"].rolling(window=15).mean()
        tomorrow_prediction = self.df["MATemperature"].iloc[-1]
        print(f"Predicted temperature: {tomorrow_prediction:.2f} °C")

    def generate_summary_report(self):
        mean_temp = self.df["Temperature"].mean()
        median_temp = self.df["Temperature"].median()
        min_temp = self.df["Temperature"].min()
        max_temp = self.df["Temperature"].max()
        std_temp = self.df["Temperature"].std()
        temperature_range = max_temp - min_temp

        summary_report = f"""
        ### Temperature Summary Report

        - Mean Temperature: {mean_temp:.2f} °C
        - Median Temperature: {median_temp:.2f} °C
        - Minimum Temperature: {min_temp:.2f} °C
        - Maximum Temperature: {max_temp:.2f} °C
        - Temperature Range: {temperature_range:.2f} °C
        - Standard Deviation: {std_temp:.2f} °C
        - Last 10-Day Moving Average: {self.df['MATemperature'].iloc[-1]:.2f} °C
        """
        print(summary_report)


def main():
    weatherApp = WeatherApp("weather_data.csv")
    
    # Beräkna genomsnittlig temperatur per månad
    print("Beräkna genomsnittlig temperatur per månad...")
    monthly_avg_temp = weatherApp.calculate_average_temperature()
    print(monthly_avg_temp)
    
    # 2. Datavisualisering
    weatherApp.data_visualization()
    
    # 3. Enkel prognos
    weatherApp.calculate_temperature_moving_avarage()
    print(weatherApp.df)
    
    # 4. Rapportering
    weatherApp.generate_summary_report()

if __name__ == "__main__":
    main()