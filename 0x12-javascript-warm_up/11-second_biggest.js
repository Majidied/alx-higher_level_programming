#!/usr/bin/node
if (process.argv.length >= 3) {
  let biggest = parseInt(process.argv[2]);
  let Second_biggest = parseInt(process.argv[2]);
  for (let i = 2; i < process.argv.length; i++) {
    if (biggest < parseInt(process.argv[i])) {
      Second_biggest = biggest;
      biggest = parseInt(process.argv[i]);
    } else if (Second_biggest < parseInt(process.argv[i])) {
      Second_biggest = parseInt(process.argv[i]);
    }
  }
  console.log(Second_biggest);
} else {
  console.log(0);
}
