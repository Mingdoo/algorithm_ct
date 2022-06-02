const solution = (participant, completion) => {
  const map = new Map();

  for (let i = 0; i < participant.length; i++) {
    let person = participant[i];
    let end = completion[i];

    if (person !== undefined) {
      map.set(person, (map.get(person) || 0) + 1);
    }
    if (end !== undefined) {
      map.set(end, (map.get(end) || 0) - 1);
    }
  }

  for (const [person, count] of map) {
    console.log(person, count);
  }
};
console.log(solution(["leo", "kiki", "eden"], ["eden", "kiki"]));
