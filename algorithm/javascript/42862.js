function solution(n, lost, reserve) {
  var answer = 0;
  const students = new Array(n).fill(1);
  for (r of reserve) {
    students[r - 1] = 2;
  }
  for (l of lost) {
    if (students[l - 1] === 2) {
      students[l - 1]--;
    } else {
      students[l - 1] = 0;
    }
  }

  for (let i = 0; i < n; i++) {
    if (!students[i]) {
      if (students[i - 1] >= 2) {
        students[i]++;
        students[i - 1]--;
      } else if (students[i + 1] >= 2) {
        students[i]++;
        students[i + 1]--;
      }
    }
  }
  return students.filter((student) => student > 0).length;
}

console.log(solution(3, [3], [1]));
