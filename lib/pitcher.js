module.exports = (player, params = {}) => {

  let randomPitchAvailability = () => {
    let paChances = [
        { pitchName: "fastball",    chanceToHave: 0.975 },
        { pitchName: "changeup",    chanceToHave: 0.888 },
        { pitchName: "curveball",   chanceToHave: 0.621 },
        { pitchName: "cutter",      chanceToHave: 0.333 },
        { pitchName: "slider",      chanceToHave: 0.303 },
        { pitchName: "knuckleball", chanceToHave: 0.075 }
      ]
    }

    return paChances.map(p => p.chanceToHave > Math.random())
  };

  if(params.selectPitchesAvailable) player.pitchesAvailable = params.selectPitchesAvailable();
  if(params.pitchesAvailable) player.pitchesAvailable = params.pitchesAvailable;
  if(!player.pitchesAvailable) player.pitchesAvailable = randomPitchAvailability();

  return player;  
};
