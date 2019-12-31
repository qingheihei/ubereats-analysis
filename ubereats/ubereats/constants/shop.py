BASE_DOMAIN = "www.ubereats.com"
BASE_URL = "https://" + BASE_DOMAIN
BASE_URL_JP = BASE_URL + "/ja-JP/"
SHOP_BASE_URL = BASE_URL_JP + "feed/?pl="

MUSASHINAKAHARA_PLID = "JTdCJTIyYWRkcmVzcyUyMiUzQSUyMiVFNiVBRCVBNiVFOCU5NCVCNSVFNCVCOCVBRCVFNSU4RSU5RiVFOSVBNyU4NSUyMiUyQyUyMnJlZmVyZW5jZSUyMiUzQSUyMkNoSUpkYXpMbUtMMUdHQVJHSjFYRzlJZVpWWSUyMiUyQyUyMnJlZmVyZW5jZVR5cGUlMjIlM0ElMjJnb29nbGVfcGxhY2VzJTIyJTJDJTIybGF0aXR1ZGUlMjIlM0EzNS41ODA3MTQzJTJDJTIybG9uZ2l0dWRlJTIyJTNBMTM5LjY0MjEwNyU3RA%3D%3D"  # noqa
MUSASHINAKAHARA_SHOP_URL = SHOP_BASE_URL + MUSASHINAKAHARA_PLID

MUSASHINAKAHARA_CARID = "eyJwbHVnaW4iOiJyZWNvbW1lbmRhdGlvbkZlZWRQbHVnaW4iLCJyZWNvbW1UeXBlIjoidG9wX3N0b3Jlc19ieV9jaXR5X3YyIn0%3D"  # noqa
POPULAR_BASE_URL = BASE_URL_JP + "search/?carid="

MUSASHINAKAHARA_POPULAR_URL = POPULAR_BASE_URL + MUSASHINAKAHARA_CARID + "&pl=" + MUSASHINAKAHARA_PLID  # noqa

MUSASHINAKAHARA_SEARCH_NAKAHARA_URL = MUSASHINAKAHARA_SHOP_URL + "&q=武蔵中原"
MUSASHINAKAHARA_SEARCH_SHINJO_URL = MUSASHINAKAHARA_SHOP_URL + "&q=武蔵新城"
MUSASHINAKAHARA_SEARCH_KOSUGI_URL = MUSASHINAKAHARA_SHOP_URL + "&q=武蔵小杉"

MIZONOKUCHI_PLID = "JTdCJTIyYWRkcmVzcyUyMiUzQSUyMiVFNiVBRCVBNiVFOCU5NCVCNSVFNiVCQSU5RCVFMyU4MyU4RSVFNSU4RiVBMyVFOSVBNyU4NSUyMiUyQyUyMnJlZmVyZW5jZSUyMiUzQSUyMkNoSUo0eTVNRWlmMEdHQVJ3alFsMUtPVDRKNCUyMiUyQyUyMnJlZmVyZW5jZVR5cGUlMjIlM0ElMjJnb29nbGVfcGxhY2VzJTIyJTJDJTIybGF0aXR1ZGUlMjIlM0EzNS41OTkwNzIxOTk5OTk5OSUyQyUyMmxvbmdpdHVkZSUyMiUzQTEzOS42MTEwMTAyJTdE"  # noqa
MIZONOKUCHI_SHOP_URL = SHOP_BASE_URL + MIZONOKUCHI_PLID

MUSASHISHINJO_PLID = "JTdCJTIyYWRkcmVzcyUyMiUzQSUyMiVFNiVBRCVBNiVFOCU5NCVCNSVFNiU5NiVCMCVFNSU5RiU4RSVFOSVBNyU4NSUyMiUyQyUyMnJlZmVyZW5jZSUyMiUzQSUyMkNoSUpMNFVUS2NqMUdHQVJHWW5CYjMweG13byUyMiUyQyUyMnJlZmVyZW5jZVR5cGUlMjIlM0ElMjJnb29nbGVfcGxhY2VzJTIyJTJDJTIybGF0aXR1ZGUlMjIlM0EzNS41ODcxOCUyQyUyMmxvbmdpdHVkZSUyMiUzQTEzOS42Mjk4NDI0JTdE"  # noqa
MUSASHISHINJO_SHOP_URL = SHOP_BASE_URL + MUSASHISHINJO_PLID

MUSASHIKOSUGI_PLID = "JTdCJTIyYWRkcmVzcyUyMiUzQSUyMiVFNiVBRCVBNiVFOCU5NCVCNSVFNSVCMCU4RiVFNiU5RCU4OSVFOSVBNyU4NSUyMiUyQyUyMnJlZmVyZW5jZSUyMiUzQSUyMkNoSUpOLVptMzNyMUdHQVJmZ3NWT3czYnptYyUyMiUyQyUyMnJlZmVyZW5jZVR5cGUlMjIlM0ElMjJnb29nbGVfcGxhY2VzJTIyJTJDJTIybGF0aXR1ZGUlMjIlM0EzNS41NzY2MzM1JTJDJTIybG9uZ2l0dWRlJTIyJTNBMTM5LjY1OTQ2NiU3RA%3D%3D"  # noqa
MUSASHIKOSUGI_SHOP_URL = SHOP_BASE_URL + MUSASHIKOSUGI_PLID
