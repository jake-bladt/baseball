# Valuation Notes

One of the harder problems in automated draft help is the question of player valuation or, in turn-based drafts, player selection. The question, "given the current league makeup, which available player gives me the best chance of victory?" is a complex one, even if you assume a robust, accurate predictive model.

## The naive model

The most obvious model to use is a naive one. In the naive model, we calculate the average of each statistic for draftable players and then value the projected output of available players as a ratio of their outputs to the average. We then add up those ratios across categories for a total score.
