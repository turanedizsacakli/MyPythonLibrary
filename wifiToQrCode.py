import wifi_qrcode_generator as qr
import os

share=qr.wifi_qrcode("wifi name ", False, "WPA", "password")

print(share)