# Streamboat PubSub
Really easy PubSub for servers, mobile apps, and web clients


## Subscribing
```
  $ curl -s https://streamboat.tv/sub/MyChannel
```

## Publishing
```
  $ curl -X POST -H "Authorization: Token 12345" \
      https://streamboat.tv/pub/MyChannel \
      -d "My message"
```

