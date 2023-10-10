const { spawn } = require('child_process');

// Spawn the MQTT process handling child process
const mqttProcess = spawn('node', ['mqtt_program.js'], { stdio: 'inherit' });

// Spawn the loop child process
const loopProcess = spawn('node', ['loop.js'], { stdio: 'inherit' });

// Handle errors if needed
mqttProcess.on('error', (error) => {
  console.error(`MQTT Process Error: ${error}`);
});

loopProcess.on('error', (error) => {
  console.error(`Loop Process Error: ${error}`);
});

// Listen for the exit event, if needed
mqttProcess.on('exit', (code, signal) => {
  console.log(`MQTT Process exited with code ${code} and signal ${signal}`);
});

loopProcess.on('exit', (code, signal) => {
  console.log(`Loop Process exited with code ${code} and signal ${signal}`);
});
