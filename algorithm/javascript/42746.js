function solution(numbers) {
  var answer = numbers
    .sort((a, b) => `${a}${b}` - `${b}${a}`)
    .reverse()
    .join("");
  return answer > 0 ? answer : "0";
}

console.log(solution([3, 30, 34, 5, 9]));
