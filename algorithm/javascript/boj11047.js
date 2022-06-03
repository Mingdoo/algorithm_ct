const input = require("fs")
  .readFileSync(0, "utf-8")
  .toString()
  .trim()
  .split("\n");

let [_, cost] = input
  .shift()
  .split(" ")
  .map((el) => +el);

const coins = [];
for (let i = 0; i < _; i++) {
  coins.push(+input.shift());
}

let ans = 0;
while (cost !== 0) {
  const filtered = coins.filter((e) => e <= cost);
  filtered.sort((a, b) => b - a);
  ans += (cost / filtered[0]) >> 0;
  cost -= ((cost / filtered[0]) >> 0) * filtered[0];
}

console.log(ans);
