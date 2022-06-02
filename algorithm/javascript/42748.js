function solution(array, commands) {
  var answer = [];
  for (const command of commands) {
    const from = command[0] - 1,
      to = command[1];
    let arr = array.slice().slice(from, to);
    arr.sort((a, b) => a - b);
    console.log(arr);
    answer.push(arr[command[2] - 1]);
  }
  return answer;
}

console.log(
  solution(
    [1, 5, 2, 6, 3, 7, 4],
    [
      [2, 5, 3],
      [4, 4, 1],
      [1, 7, 3],
    ],
  ),
  "expected: [5, 6, 3]",
);
