function solution(genres, plays) {
  const answer = [];
  const map = new Map();
  const cntMap = new Map();
  for (let i = 0; i < genres.length; i++) {
    const genreData = map.get(genres[i]) || [];
    genreData.push([i, plays[i]]);
    map.set(genres[i], genreData);
  }
  for (const [genre, arr] of map) {
    arr.sort(function (a, b) {
      return b[1] >= a[1] ? 1 : -1;
    });
    arr.forEach((item) => {
      cntMap.set(genre, (cntMap.get(genre) || 0) + item[1]);
    });
  }
  const sortedCntMap = new Map(
    [...cntMap.entries()].sort((a, b) => b[1] - a[1]),
  );
  for (const [genre, _] of sortedCntMap) {
    for (let i = 0; i < 2; i++) {
      if (map.get(genre)[i]) {
        answer.push(map.get(genre)[i][0]);
      }
    }
  }
  return answer;
}

solution(
  ["classic", "pop", "classic", "classic", "pop"],
  [500, 600, 150, 800, 2500],
);
