#! /bin/sh

curl http://10.40.71.118/zodiac/western -X GET -v

curl http://10.40.71.118/zodiac/western/Libra -X GET -v

curl http://10.40.71.118/zodiac/western/Ram -X GET -v

curl http://10.40.71.118/zodiac/western/Libra -X DELETE -v

curl http://10.40.71.118/zodiac/western/Libra -X GET -v

curl http://10.40.71.118/zodiac/western -X POST -v \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-d '{ "symbol": "Libra",
    "start": {
        "month": "September",
        "day": 23
    },
    "end": {
        "month": "October",
        "day": 22
    },
    "reading": "If you have doubts, you need to have confidence in yourself." }'

curl http://10.40.71.118/zodiac/western/Libra -X GET -v

curl http://10.40.71.118/zodiac/western/Aries -X PUT -v \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-d '{ "symbol": "Ram" }'

curl http://10.40.71.118/zodiac/western/Ram -X GET -v

curl http://10.40.71.118/zodiac/western/Aries -X GET -v
