function solution(people, limit) {
  var answer = 0;
  people.sort((a, b) => a - b);
  while (people.length) {
    const v = people.pop();
    if (v + people[0] <= limit) {
      people.shift();
    }
    answer++;
  }
  return answer;
}

console.log(solution([70, 50, 80, 50], 100), "expected: 3");
