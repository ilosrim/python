let min, max: number;
min = 2;
max = 10;

function tubSon(min: number, max: number) {
  // let tubSonlar: number[];
  for (let i = min; i <= max; i++) {
    let tubSonmi: boolean = true;
    for (let j = 2; j < i; j++) {
      if (i % j == 0) {
        tubSonmi = false;
        break;
      }
    }
    if (tubSonmi) console.log(i);
  }
}
tubSon(min, max);
// let tub_son = tubSon(min, max);
// console.log(tub_son);
