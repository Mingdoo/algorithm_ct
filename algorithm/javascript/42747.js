function solution(citations) {
  var answer = 0;
  for (let i = 0; i < Math.max(...citations); i++) {
    if (
      citations.filter((citation) => citation >= answer + 1).length >=
      answer + 1
    ) {
      answer++;
    } else {
      break;
    }
  }
  return answer;
}

console.log(solution([3, 0, 6, 1, 5]));
