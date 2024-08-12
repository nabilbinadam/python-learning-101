shirts = {
    "type": "polo",
    "color": ["red", "white", "black"],
    "id": 483948,
    "active": True,
    "stores": [
        {
            "address": "jalan langgar",
            "state": "Kedah"
        },
        {
            "address": "jalan perai",
            "state": "Penang"
        },
        {
            "address": "jalan kuching",
            "state": "Sarawak"
        },
        {
            "address": "jalan melaka",
            "state": "Melaka"
        }
    ]
}




for store in shirts["stores"]:
    print(store)