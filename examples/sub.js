var request = require("request"),
     chan = process.argv[2];

request.get("https://streamboat.tv/sub/" + chan)
  .on("data", function(data) {
    console.log(data.toString());
  });