from app.ingestion.transform import transform_candles


sample_candles = [
    [
        "2018-01-25T00:00:00+05:30",
        461.3,
        463.25,
        455.7,
        460.35,
        13112506,
        0,
    ],
    [
        "2018-01-24T00:00:00+05:30",
        467.9,
        467.9,
        458.8,
        460.55,
        13706826,
        0,
    ],
]


result = transform_candles(sample_candles)

for price in result:
    print(price)