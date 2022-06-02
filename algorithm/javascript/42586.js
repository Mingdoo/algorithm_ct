function solution(progresses, speeds) {
  const answer = [];
  while (progresses.length) {
    for (let i in speeds) {
      if (progresses[i] < 100) {
        progresses[i] += speeds[i];
      }
    }

    let cnt = 0;
    while (progresses.length && progresses[0] >= 100) {
      progresses.shift();
      speeds.shift();
      cnt++;
    }
    if (cnt) {
      answer.push(cnt);
    }
  }
  return answer;
}

console.log(solution([93, 30, 55], [1, 30, 5]));
