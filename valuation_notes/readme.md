# Valuation Notes

One of the harder problems in automated draft help is the question of player valuation or, in turn-based drafts, player selection. The question, "given the current league makeup, which available player gives me the best chance of victory?" is a complex one, even if you assume a robust, accurate predictive model.

## The naive model

The most obvious model to use is a naive one. In the naive model, we calculate the average of each statistic for draftable players and then value the projected output of available players as a ratio of their outputs to the average. We then add up those ratios across categories for a total score.

For example, in a theoretical league where batters are measured by home runs, stolen bases, and total bases, a batter with an average number of home runs, twice the average of stolen bases, and half the average of total bases is worth 3.5 points whereas a player with a quarter of the home runs, twice the stolen bases, and twice the total bases is worth 4.25 points.

While this model is valuable for initial valuation, it suffers numerous shortcomings. It fails to take into account diminishing returns, opportunity cost, or position scarcity. It can overvalue sparse categories and works particularly poorly for specialized statistics like saves.

## The simulation model

Simulation-based modeling has the potential to be the strongest approach, but it's also the most computationally intensive. Much like traditional chess-playing programs, the simulation model evaluates the strength of each potential pick by simulating the possible countermoves of the players' fellow draftees and recommends the choice with the strongest possible outcome.

While great advances have been made in chess-playing software (ie Big Blue,) they still require large amounts of computation power running on specialized hardware. Beside that, the number of possible moves in fantasy baseball is much larger than that in chess. Where a decision tree in chess has a total solution space of 1.0E120 moves, one in a twelve-team fantasy baseball league can run as large as 500! nodes (almost 1.E1000 times larger.)

The computational requirements can be greatly decreased by applying a primary valuation model to choices and limiting the simulation in candidates and depth, but this exposes the simulation model to both weaknesses in the primary valuation and failure to predict high-delta perturbations in late rounds.

## Position scarcity and second-best options

Some weaknesses of the naive model can be addressed by considering both position scarcity and second-best options. 
