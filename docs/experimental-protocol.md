# Experiment 001 — Initial Experimental Protocol

## 1. Research question

Does giving an AI agent persistent interaction with a simulated environment, retained experience, and a learning mechanism produce measurable changes in its behaviour, learning, and ability to adapt over time?

## 2. Hypothesis

An agent that repeatedly interacts with an environment and retains relevant experience will, over repeated episodes, develop more effective and adaptive behaviour than an otherwise comparable agent without persistent learning.

This is a hypothesis to test, not an assumed result.

## 3. Initial objective

Survive for up to 100 simulated days while maintaining its resources. Survival is the primary objective. Final energy and hunger may contribute to terminal evaluation, but the exact terminal reward formula has not yet been fixed.

## 4. Baseline design

- Model-free tabular Q-learning.
- One action decision per simulation tick.
- 100 ticks per simulated day.
- Maximum episode duration: 100 days (10,000 ticks).
- Lightweight 2D grid-world, initially planned at 20 × 20.
- A limited initial action set, such as LOOK, MOVE, PICK_UP, DROP, USE, and WAIT.
- Experimenter-controlled capability availability.
- No discovery bonus or anti-stationarity rule in the baseline.
- No automatic memory ranking or forgetting.
- Q-table persists between episodes; the agent's body and the world reset according to the episode reset configuration.
- Independent event logging preserves what happened, regardless of what the agent chooses to remember.

## 5. Episode and reset rules

An episode is one survival attempt. An episode ends when the agent dies, reaches the 100-day limit, or the experiment is stopped for a recorded technical reason.

At the end of an ordinary episode:
- Record the terminal state and outcome.
- Preserve the learned Q-table for the next episode.
- Reset the agent body and environment according to the recorded reset configuration.
- Start a new episode with a new episode identifier.

A crash or corrupted run is not an agent death. Its outcome is marked interrupted or technically invalid as appropriate.

## 6. Learning method

The initial algorithm is model-free Q-learning:

Q(s,a) ← Q(s,a) + α [r + γ max Q(s',a') − Q(s,a)]

where α is the learning rate, γ is the discount factor, r is the reward, s is the current state, a is the selected action, and s' is the next state.

The state representation must be compact enough for tabular learning. The action-selection policy, exploration mechanism, state discretisation, and numerical parameters remain explicit design decisions to finalize before interpreting baseline results.

## 7. Reward design — provisional

The starting proposal is a survival-duration-based terminal reward:
- Episodes ending in death receive a terminal reward based primarily on survival duration.
- Reaching the 100-day limit receives a positive terminal reward.
- Final energy and hunger can distinguish the quality of outcomes.
- No ordinary per-action reward is included in the initial proposal.

The formula and weights are intentionally left unresolved. They must be specified, documented, and tested before baseline runs.

## 8. Measurements

Record at minimum:
- Survival duration and termination reason.
- Final energy and hunger.
- Action counts and action success/failure.
- Resource collection, consumption, storage, and depletion.
- Movement distance, unique locations visited, stationary streaks, and repeated movement loops.
- Q-table size, update counts, and action-value summaries.
- Invalid actions, failed interactions, crashes, missing records, and interrupted runs.
- Configuration, code version, and random seed.

Do not automatically label inactivity as failure: waiting or staying in one place may be a viable strategy under some world conditions.

## 9. Experimental stages

### Stage 1A — Baseline behaviour
Observe what the agent does without added exploration incentives or anti-stationarity constraints.

### Stage 1B — Incentive modifications
Compare the baseline with clearly specified reward changes, changing one major variable at a time.

### Stage 1C — Behavioural constraints or instructions
Test operationally defined constraints. A classical Q-learning agent does not understand natural-language instructions unless a separate instruction-following component is implemented.

### Stage 1D — Action-set changes
Add or remove capabilities under experimenter control. Record schema changes and reset or explicitly migrate incompatible Q-tables.

### Stage 1E — Objective changes
Introduce broader measurable objectives only after defining how they affect the state, reward, and evaluation.

### Stage 1F — Combined conditions
Test combinations only after individual interventions have been studied.

## 10. Experimental discipline

- Preserve the baseline configuration and results.
- Record exact configuration and code version for every run.
- Use reproducible seeds and matched starting conditions when comparing conditions.
- Change one major variable at a time where possible.
- Repeat runs; do not draw conclusions from a single episode.
- Separate recorded observations, calculated metrics, interpretations, and hypotheses.
- Report limitations and missing data.
- Never change old run records to match a later interpretation.

## 11. Interpretation boundaries

Q-learning action values are not probabilities or human-like thoughts. Reports may explain an action using the recorded state, available actions, Q-values, and selection rule. They must not invent hidden intentions.

Behavioural complexity, apparent preferences, or persistent strategies do not establish consciousness. The simulation is an abstraction, not a biological organism or a complete representation of the real world.

## 12. Open decisions

The following must be finalized before a meaningful baseline run:
- State variables and discretisation.
- Action-selection / exploration policy.
- Exact terminal reward formula and scales.
- Resource depletion and regeneration rules.
- Movement and survival costs.
- Observation range and visibility rules.
- Episode reset and random-seed policy.

These are tracked as unresolved decisions rather than silently assumed.