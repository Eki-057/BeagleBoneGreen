// blinkledjava.js
const fs = require('fs').promises;

const LED = 'beaglebone:green:usr3'; // change to usr1/usr2/usr3 as needed
const LED_BASE = `/sys/class/leds/${LED}`;

async function writeSysfs(path, value) {
  await fs.writeFile(path, value);
}

async function setup() {
  // Ensure the kernel isn't driving the LED
  await writeSysfs(`${LED_BASE}/trigger`, 'none\n');
}

let on = false;
let timer;

async function toggle() {
  on = !on;
  await writeSysfs(`${LED_BASE}/brightness`, on ? '255\n' : '0\n');
}

async function main() {
  await setup();
  timer = setInterval(toggle, 500); // 500 ms on/off
}

process.on('SIGINT', async () => {
  clearInterval(timer);
  try {
    await writeSysfs(`${LED_BASE}/brightness`, '0\n'); // ensure off
  } catch {}
  process.exit(0);
});

main().catch(err => {
  console.error(err);
  process.exit(1);
});
