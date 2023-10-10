import IOTContext from "./iot-context";
import { useEffect, useState } from "react";

const IOTProvider = (props) => {
  const [buttonset, setButtonset] = useState({
    led1: false,
    led2: false,
    led3: false,
    led4: false,
    led5: false,
  });

  useEffect(() => {
    async function fetchLedStatusData() {
      const apiUrl =
        "https://apli2-flask-api-95f63c57f3cd.herokuapp.com/api/led-status";
      const response = await fetch(apiUrl);
      const data = await response.json();

      data.map((led) => {
        setButtonset((buttonset) => ({
          ...buttonset,
          [`led${led.ledNumber}`]: led.status === "ON" ? true : false,
        }));
      });
    }
    fetchLedStatusData();
  }, []);

  const handleLed = (led = "") => {
    // Toggle the LED status in the state
    setButtonset((buttonset) => ({
      ...buttonset,
      [led]: !buttonset[led],
    }));
  };

  const iotContext = {
    leds: buttonset,
    handleLed: handleLed,
  };

  return (
    <IOTContext.Provider value={iotContext}>
      {props.children}
    </IOTContext.Provider>
  );
};

export default IOTProvider;
