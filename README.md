# ChiaSignature
Chia Plots signature service

# use
``` 
docker-compose up -d
```

Load balancing:
``` 
docker-compose scale chia_signature=10
```

# api
``` 
curl --location --request POST 'http://youservername:8181/signature' \
--header 'Content-Type: application/json' \
--data-raw '{
    "farmer_public_key": "farmer_public_key",
    "pool_key": "pool_key"
}'
```