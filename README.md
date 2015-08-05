# Streamboat PubSub
Really easy PubSub for servers, mobile apps, and web clients

## Publishing
```
  $ curl -X POST -H "Authorization: Token 12345" \
      https://streamboat.tv/pub/MyChannel \
      -d "My message"
```

## Subscribing
```
  $ curl -s https://streamboat.tv/sub/MyChannel
  My message
```

## WebSocket subscriptions
```
var ws = new WebSocket("wss://streamboat.tv/sub/MyChannel");
ws.onmessage = function(event) {
    console.log(event.data);
    // "My message"
};
```

## Python subscriptions
```
>>> import requests
>>> r = requests.get("https://streamboat.tv/sub/MyChannel", stream=True)
>>> for msg in r.iter_lines():
>>>   print msg
My message
...
```

## NodeJS subscriptions
```
var request = require("request");
request.get("https://streamboat.tv/sub/MyChannel")
  .on("data", function(data) {
     console.log(data.toString());
     // My message
  });
```