import React, { useState, useEffect, useContext } from "react";
import Button from "../components/UI/Button";
import IOTContext from "../store/iot-context";

const HomePage = () => {
  const iotCtx = useContext(IOTContext);

  const { leds: buttonSet } = iotCtx;

  const [ledStatusData, setLedStatusData] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  const handleLed = (led = "") => {
    // Toggle the LED status in the state

    iotCtx.handleLed(led);

    // Define the API endpoint
    const apiUrl =
      "https://apli2-flask-api-95f63c57f3cd.herokuapp.com/api/control-led";

    // Define the LED status (e.g., 'on' or 'off')
    const newStatus = buttonSet[led] ? "OFF" : "ON";

    // Create the request body as JSON
    const requestBody = {
      ledNumber: parseInt(led.slice(3)),
      status: newStatus,
    };

    // Send a POST request to the API using the fetch API
    console.log(JSON.stringify(requestBody));

    fetch(apiUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(requestBody),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then((data) => {
        console.log("API response:", data);

        // After sending the request, trigger a refresh of the LED status data
        refreshLedStatusData();
        console.log("WAITING....");
      })
      .catch((error) => {
        console.error("API error:", error);
      });
  };

  // Function to refresh LED status data
  const refreshLedStatusData = () => {
    // Make a GET request to the /api/all-led-status endpoint
    fetch(
      "https://apli2-flask-api-95f63c57f3cd.herokuapp.com/api/all-led-status"
    )
      .then((response) => response.json())
      .then((data) => {
        setLedStatusData(data);
        setIsLoading(false);
      })
      .catch((error) => {
        console.error("Error fetching LED status data:", error);
        setIsLoading(false);
      });
  };

  useEffect(() => {
    // Refresh the LED status data when the component mounts
    refreshLedStatusData();
  }, []);

  return (
    <div>
      <div className="text-4xl my-8 text-center text-violet-900">Dashboard</div>
      <div className="flex justify-center max-w-[90%] mx-auto gap-8">
        <div className="w-1/4 bg-gray-100 p-4 shadow-xl shadow-black/50">
          <h3 className="text-center text-violet-900 text-2xl">
            Control de Luces
          </h3>
          <div className="flex flex-col gap-4 p-2 ">
            <Button
              onClick={handleLed.bind(null, "led2")}
              className={
                buttonSet.led2
                  ? "bg-green-600 duration-300 hover:bg-green-700"
                  : "bg-red-600 duration-300 hover:bg-red-700"
              }
            >
              Led 2
            </Button>
            <Button
              onClick={handleLed.bind(null, "led12")}
              className={
                buttonSet.led12
                  ? "bg-green-600 duration-300 hover:bg-green-700"
                  : "bg-red-600 duration-300 hover:bg-red-700"
              }
            >
              Led 12
            </Button>
            <Button
              onClick={handleLed.bind(null, "led13")}
              className={
                buttonSet.led13
                  ? "bg-green-600 duration-300 hover:bg-green-700"
                  : "bg-red-600 duration-300 hover:bg-red-700"
              }
            >
              Led 13
            </Button>
            <Button
              onClick={handleLed.bind(null, "led14")}
              className={
                buttonSet.led14
                  ? "bg-green-600 duration-300 hover:bg-green-700"
                  : "bg-red-600 duration-300 hover:bg-red-700"
              }
            >
              Led 14
            </Button>
            <Button
              onClick={handleLed.bind(null, "led15")}
              className={
                buttonSet.led15
                  ? "bg-green-600 duration-300 hover:bg-green-700"
                  : "bg-red-600 duration-300 hover:bg-red-700"
              }
            >
              Led 15
            </Button>
            {/* Add similar buttons for other LEDs */}
          </div>
        </div>
        <div className="w-2/4 bg-gray-100 p-4 max-h-[400px] shadow-xl shadow-black/50">
          <h3 className="text-center text-violet-900 text-2xl">Registro</h3>
          {isLoading ? (
            <p>Loading...</p>
          ) : (
            <ul className="flex flex-col items-left gap-1 p-4 max-h-[340px] overflow-auto">
              {ledStatusData.map((entry, index) => (
                <li
                  key={index}
                  className="bg-gray-200 text-gray-950 cursor-pointer duration-300 hover:text-yellow-400"
                >
                  {/* LED {entry.ledNumber}: {entry.status} (Timestamp: {entry.timestamp}) */}
                  <h1 className="text-slate-700 font-bold my-2">
                    LED {entry.ledNumber}
                  </h1>
                  <div className="flex justify-evenly">
                    <p>
                      Status: <span className="font-bold">{entry.status}</span>
                    </p>
                    <p>
                      Timestamp:
                      <span className="font-bold">{entry.timestamp}</span>
                    </p>
                  </div>
                </li>
              ))}
            </ul>
          )}
        </div>
      </div>
    </div>
  );
};

export default HomePage;
