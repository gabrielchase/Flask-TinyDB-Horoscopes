#! /bin/sh

curl http://10.40.71.118/zodiac/chinese -X GET -v

curl http://10.40.71.118/zodiac/chinese/horse -X GET -v

curl http://10.40.71.118/zodiac/chinese/ram -X GET -v

curl http://10.40.71.118/zodiac/chinese/horse -X DELETE -v

curl http://10.40.71.118/zodiac/chinese/horse -X GET -v

curl http://10.40.71.118/zodiac/chinese -X POST -v \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-d '{ "animal": "horse",
    "characteristics": "Energetic, Passionate, Upright, Aspirant.",
    "position": 6 }'

curl http://10.40.71.118/zodiac/chinese/horse -X GET -v

curl http://10.40.71.118/zodiac/chinese/sheep -X PUT -v \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-d '{ "animal": "ram" }'

curl http://10.40.71.118/zodiac/chinese/ram -X GET -v

curl http://10.40.71.118/zodiac/chinese/sheep -X GET -v