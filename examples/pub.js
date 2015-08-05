var request = require("request"),
     chan = process.argv[2],
     msg = process.argv[3];

request({
    url: "https://streamboat.tv/pub/" + chan,
    method: "POST",
    headers: {"Authorization": "Token 12345"},
    body: msg,
    },
    function(err, res, body) {
        console.log(body);
    }
);