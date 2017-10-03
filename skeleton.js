const mqtt = require("mqtt")
const client = mqtt.connect("mqtt://broker.hivemq.com")


client.on("connect", () => {
  // TODO fill this in
})

client.on("message", (topic, message) => {
  // TODO fill this in
})
