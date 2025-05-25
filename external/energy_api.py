import requests

ENERGY_API_URL = "https://cea.nic.in/api/power_generation.php"  # replace with your real API endpoint


def fetch_energy_data(location, power_type="THERMAL"):
    try:
        response = requests.get(ENERGY_API_URL)
        response.raise_for_status()
        data = response.json()
        # print(data)

        # Aggregate total generation per mode
        mode_totals = {}
        mode_counts = {}

        for year, records in data.items():
            for record in records:
                print(f"Record {record}")
                if record["Region_State"].lower() == location.lower() or location.lower() == "all india":
                    mode = record["mode"]
                    bus_value = float(record["bus"])
                    mode_totals[mode] = mode_totals.get(mode, 0) + bus_value
                    mode_counts[mode] = mode_counts.get(mode, 0) + 1
        print(f"mode total {mode_totals}")
        print(f"mode total {mode_counts}")
        # Calculate average monthly kWh per mode
        average_monthly_kwh = {
            mode: (total / count) if count > 0 else 0
            for mode, (total, count) in zip(mode_totals.keys(), zip(mode_totals.values(), mode_counts.values()))
        }

        # Example placeholder for peak usage times (real API probably doesn’t provide this)
        peak_usage_times = ["6pm-9pm"]
        print(f"average {average_monthly_kwh}")
        return {
            "location": location,
            "average_monthly_kwh": average_monthly_kwh["THERMAL"],
            "peak_usage_times": peak_usage_times
        }
    except Exception as e:
        print(f"Error fetching energy data: {e}")
        peak_usage_times = ["6pm-9pm"]
        return {
            "location": location,
            "average_monthly_kwh": 0,
            "peak_usage_times": peak_usage_times
        }
