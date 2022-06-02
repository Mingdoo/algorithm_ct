function solution(s) {
  const stack = [];
  if (s.length % 2 != 0) {
    return 0;
  }
  for (let i = 1; i < s.length; i++) {
    if (s[i] === stack[stack.length - 1]) {
      stack.pop();
    } else {
      stack.push(s[i]);
    }
  }
  return stack.length ? 0 : 1;
}

console.log(solution("cdcd"));
