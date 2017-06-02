module.exports = (firstName, lastName) => { 
  let ret = {firstName, lastName };
  ret.toString = () => `${firstName} ${lastName}`;
  return ret;
}
