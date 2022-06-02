function solution(maps) {
  var answer = 0;
  const n = maps.length,
    m = maps[0].length,
    dr = [0, 0, -1, 1],
    dc = [1, -1, 0, 0],
    visited = Array(n)
      .fill(0)
      .map(() => new Array(m).fill(0));

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (!maps[i][j]) {
        visited[i][j] = -1;
      }
    }
  }

  if (visited[n - 2][m - 1] !== 0 && visited[n - 1][m - 2] !== 0) {
    return -1;
  }

  const stack = [[0, 0, 1]];
  while (stack.length) {
    const v = stack.pop();
    for (let i = 0; i < 4; i++) {
      const nr = v[0] + dr[i],
        nc = v[1] + dc[i];
      if (nr >= 0 && nr < n && nc >= 0 && nc < m) {
        if (visited[nr][nc] === 0 || visited[nr][nc] > v[2] + 1) {
          visited[nr][nc] = v[2] + 1;
          stack.push([nr, nc, v[2] + 1]);
        }
      }
    }
  }
  return visited[n - 1][m - 1] > 0 ? visited[n - 1][m - 1] : -1;
}

console.log(
  solution([
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 1],
  ]),
);
