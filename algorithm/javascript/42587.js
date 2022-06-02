function solution(priorities, location) {
  const prioritiesMap = priorities.map((item, key) => [key, item]);

  let cnt = 0;
  while (true) {
    let v = prioritiesMap.shift();
    if (
      prioritiesMap.some((item) => {
        return item[1] > v[1];
      })
    ) {
      prioritiesMap.push(v);
    } else {
      cnt += 1;
      if (v[0] === location) {
        return cnt;
      }
    }
  }
}

console.log(solution([2, 1, 3, 2], 2));
