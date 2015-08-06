# Streamboat PubSub
Really easy PubSub for servers, mobile apps, and web clients

## Publishing
requires Auth token
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

## Subscribe a WebHook
requires Auth token
```
>>> import requests
>>> data = {'hook_url': "https://example.com/webhook"}
>>> auth = {'Authorization': "Token 12345"}
>>> requests.post("https://streamboat.tv/hook/MyChannel", data=data, headers=auth)
```
Messages published to `MyChannel` will be `POST`'d to `https://example.com/webhook`

## Unsubscribe a WebHook
requires Auth token
```
>>> import requests
>>> data = {'hook_url': "https://example.com/webhook"}
>>> auth = {'Authorization': "Token 12345"}
>>> requests.post("https://streamboat.tv/unhook/MyChannel", data=data, headers=auth)
```
Messages published to `MyChannel` will no longer be `POST`'d to `https://example.com/webhook`

## Channels
Channel names can be of any length and must be validated by the following regex:
```
^[\w\d\-_:|]+$
```
Basically, any combination of alpha-numeric characters, hyphens, underscores, colons, and pipes.

## Channel Privacy
Anyone can publish or subscribe to any channel if they know the name.  If you would like to make sure your channels are private then you should make them unguessable.  A simple way to do this is to use a UUID or crypto hash of some secret value.  For example, the `MyChannel` name could be hashed with some secret making it `5923bf288ef5f0b068fd5a23d0f5aa3d851dce7a`.  Just namespace your channels like `5923bf288ef5f0b068fd5a23d0f5aa3d851dce7a:MyChannel` so no one can publish/subscribe to your channels except you.