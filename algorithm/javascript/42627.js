function solution(jobs) {
  jobs.sort((a, b) => a[1] - b[1]);
  let time = 0,
    amount = 0,
    q = [],
    n = jobs.length;

  while (jobs.length || q.length) {
    if (q.length && q[0][2] === time) {
      const v = q.shift();
      amount += v[2] - v[0];
    }

    if (q.length === 0 && jobs.length) {
      for (const i in jobs) {
        if (jobs[i][0] <= time) {
          const v = jobs.splice(i, 1)[0];
          q.push([...v, time + v[1]]);
          break;
        }
      }
    }

    time++;
  }
  return Math.floor(amount / n);
}

console.log(
  solution([
    [0, 3],
    [1, 9],
    [2, 6],
  ]),
);
