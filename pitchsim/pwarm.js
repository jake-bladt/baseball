let player = require('./lib/player');
let pitcher = require('./lib/pitcher');

let bobSmith = player('Bob', 'Smith');
pitcher(bobSmith);
console.log(`${bobSmith.toString()} is taking the field.`);
console.log(`${bobSmith.firstName} has ${bobSmith.pitchesAvailable.map(p => p.pitchName)}`);
