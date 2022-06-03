const input = require("fs")
  .readFileSync("boj1931.txt", "utf-8")
  .toString()
  .trim()
  .split("\n");

console.log(input);
const N = +input.shift();
const conference = [];
for (let tc = 0; tc < N; tc++) {
  conference.push(
    input
      .shift()
      .split(" ")
      .map((el) => +el),
  );
}
conference.sort((a, b) => a[1] - b[1] || a[0] - b[0]);
const maximum = Math.max(...conference.map((a) => a[0]));
let time = 0;
let answer = 0;
while (time <= maximum) {
  for (let conf of conference) {
    if (time <= conf[0]) {
      time = conf[1];
      answer++;
      continue;
    }
  }
  time++;
}

console.log(answer);
