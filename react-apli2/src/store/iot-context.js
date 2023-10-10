import React from "react"

const IOTContext = React.createContext({
    leds: [],
    handleLed: () => {},
})

export default IOTContext