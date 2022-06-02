function solution(n, computers) {
  var answer = 0;
  const visited = new Array(n).fill(0);
  const connected = new Array(n).fill(0).map(() => []);
  for (let i = 0; i < n; i++) {
    computers[i].forEach((el, idx) => {
      if (idx !== i && el > 0) {
        connected[i].push(idx);
      }
    });
  }
  const stack = [];
  while (visited.some((el) => el === 0)) {
    for (let i = 0; i < n; i++) {
      if (visited[i] === 0) {
        stack.push(i);
        answer++;
        break;
      }
    }
    while (stack.length) {
      const v = stack.pop();
      visited[v] = 1;
      for (const node of connected[v]) {
        if (!visited[node]) {
          stack.push(node);
        }
      }
    }
  }
  return answer;
}

console.log(
  solution(3, [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1],
  ]),
  "expected: 2",
);
