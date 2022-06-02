function solution(operations) {
  var answer = [];
  const q = [];
  for (const operation of operations) {
    let [op, num] = operation.split(" ");
    console.log(op, num);
    if (op === "I") {
      q.push(Number(num));
    } else {
      if (num === "1") {
        const val = Math.max(...q);
        console.log(val);
        const idx = q.indexOf(val);
        q.splice(idx, 1);
      } else {
        const val = Math.min(...q);
        console.log(val);
        const idx = q.indexOf(val);
        q.splice(idx, 1);
      }
    }
    console.log(q);
  }
  if (q.length) {
    return [Math.max(...q), Math.min(...q)];
  } else {
    return [0, 0];
  }
}

console.log(
  solution([
    "I -45",
    "I 653",
    "D 1",
    "I -642",
    "I 45",
    "I 97",
    "D 1",
    "D -1",
    "I 333",
  ]),
);
