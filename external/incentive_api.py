def fetch_incentives(location):
    # Placeholder for actual data retrieval
    # Replace with actual data sources or APIs
    incentives = []

    if location.lower() == "all india":
        incentives.append({
            "name": "Pradhan Mantri Surya Ghar Muft Bijli Yojana",
            "description": "Provides subsidies for rooftop solar installations.",
            "link": "https://pmsuryaghar.gov.in/"
        })
        incentives.append({
            "name": "PM E-DRIVE Scheme",
            "description": "Incentives for electric vehicle adoption.",
            "link": "https://www.reuters.com/business/autos-transportation/india-allots-109-bln-rupees-scheme-promote"
                    "-electric-vehicles-2024-09-11/"
        })

    return incentives
