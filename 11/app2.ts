function isValid(s: string): boolean {
  if (s.length % 2 !== 0) return false;

  let stack: string[] = [];
  for (let i = 0; i < s.length; i++) {
    if (s[i] === "(" || s[i] === "{" || s[i] === "[") {
      stack.push(s[i]);
    } else {
      let top: string = stack[stack.length - 1];
      if (
        (top === "(" && s[i] === ")") ||
        (top === "{" && s[i] === "}") ||
        (top === "[" && s[i] === "]")
      ) {
        stack.pop();
      } else {
        return false;
      }
    }
  }
  return stack.length === 0;
}

let a = isValid("{1}");
console.log(a);

// let charSymbol: string[] = ["(", ")", "{", "}", "[", "]"];
// charSymbol.map((val) => console.log(val));
