# Rename settings_sample.py to settings.py
# Generate jss_credentials with:
# printf "username:password" | iconv -t ISO-8859-1 | base64 -i -

jss_server = "YOUR_JAMF_PRO_URL"
jss_credential = "YOUR_CREDENTIALS"

attributes = {
    "extension_attributes": [
        {
            "id": 32,                       # Extenssion attribute ID
            "name": "shared_computer",      # Name in API output
        },
        {
            "id": 11,
            "name": "Whetever..."
        }
    ]
}
