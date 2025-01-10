# utils.py
import requests
from django.core.exceptions import ValidationError

def geocode_address(complaint):
    # added our actual Google API key
    GOOGLE_MAPS_API_KEY = "AIzaSyC5tQsxri8webEFQRqqFwL_gYhq2nyKoQM"

    # Getting the full address (address, city, and postal code)
    address = f"{complaint.address}, {complaint.city}, {complaint.postal_code}"
    print(f"Geocoding address: {address}")

    # Sending request to Google Geocoding API
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={GOOGLE_MAPS_API_KEY}"
    try:
        response = requests.get(url)
        data = response.json()

        if data['status'] == 'OK':
            location = data['results'][0]['geometry']['location']
            complaint.latitude = location['lat']
            complaint.longitude = location['lng']
            complaint.save()
            print(f"Geocoding successful: {location['lat']}, {location['lng']}")
        else:
            raise ValidationError(f"Invalid address: {address}. Please provide a valid address.")
    except Exception as e:
        raise ValidationError(f"Geocoding failed with error: {str(e)}")