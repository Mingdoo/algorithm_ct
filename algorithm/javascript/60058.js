function solution(p) {
  const newP = p.split("");
  console.log(newP);
  function recursive(p) {
    let u = [],
      v = [];
    for (let i = 0; i < p.length; i++) {
      if (p[i] === "(") {
        u.push("(");
      } else {
        if (u[u.length - 1] === "(") {
          u.push(")");
        } else {
          v.push(...p.splice(i, p.length));
          return [u, v];
        }
      }
    }
  }
  console.log(recursive(newP));
  var answer = "";
  return answer;
}

console.log(solution("()))((()"));
