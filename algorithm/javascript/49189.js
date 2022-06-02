const p = (a) => console.log(a);

function solution(n, edge) {
  var answer = 0;
  const connected = new Array(n + 1).fill(0).map(() => []);
  const visited = new Array(n + 1).fill(50001);
  for (const [from, to] of edge) {
    connected[from].push(to);
    connected[to].push(from);
  }
  const q = [[1, 0]];
  visited[1] = 0;
  visited[0] = 0;
  while (q.length) {
    console.log(q);
    const [v, dist] = q.shift();
    for (const node of connected[v]) {
      if (dist + 1 < visited[node]) {
        visited[node] = dist + 1;
        q.push([node, dist + 1]);
      }
    }
  }
  return visited.filter((v) => v === Math.max(...visited)).length;
  return answer;
}

p(
  solution(6, [
    [3, 6],
    [4, 3],
    [3, 2],
    [1, 3],
    [1, 2],
    [2, 4],
    [5, 2],
  ]),
);
