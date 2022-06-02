var answer = 0;
function solution(numbers, target) {
  dfs(target, numbers[0], [...numbers].splice(1, numbers.length));
  dfs(target, -numbers[0], [...numbers].splice(1, numbers.length));
  return answer;
}

function dfs(target, sum, array) {
  if (array.length === 0) {
    if (sum === target) {
      answer++;
    }
    return;
  }

  dfs(target, sum + array[0], [...array].splice(1, array.length));
  dfs(target, sum - array[0], [...array].splice(1, array.length));

  return;
}

console.log(solution([1, 1, 1, 1, 1], 3));
