# Experiment 001 — Persistent Artificial Agent

A zero-budget, modular research project exploring how a persistent learning agent behaves in a simulated environment over repeated experience.

**Research question:** Does persistent interaction with an environment, combined with retained experience and reinforcement learning, produce measurable changes in an agent's behaviour, learned action values, and ability to adapt?

## Current experimental baseline

- **Learning method:** model-free tabular Q-learning
- **Environment:** lightweight 2D grid-world (planned initial size: 20 × 20)
- **Objective:** survive for up to 100 simulated days
- **Time:** 100 ticks per simulated day; one action decision per tick
- **Reward:** survival-duration-based terminal reward is the starting proposal. The exact formula remains to be specified.
- **Memory:** persistent Q-table plus an independently recorded event history. No memory-priority or automatic forgetting system.
- **Capabilities:** experimenter-controlled; no automatic unlock milestones
- **Budget:** zero-cost local development; no paid APIs or hosted compute

This repository is the implementation workspace. The experimental protocol and architecture notes document design decisions and unresolved questions.

## Repository layout

```text
configs/       Versioned experiment configurations
docs/          Research protocol and architecture
src/           Simulation and learning implementation
tests/         Automated tests
reports/       Generated summaries (do not commit large raw logs)
data/          Local run data (ignored by Git)
```

## Status

<**Research design / implementation scaffold**>

The repository is being built in stages. A design decision is not considered implemented merely because it appears in documentation. The initial environment, reward formula, state representation, and learning policy must be implemented and tested before results are interpreted.

## Run

Implementation instructions will be added when the first runnable prototype is in place.

## Experimental integrity

Every run should record its configuration, code version, random seed, episode outcome, and event log. Preserve baseline runs. Change one major experimental variable at a time. Distinguish agent underperformance from simulation, data, or measurement failures.

## Safety boundary

The agent operates only through a restricted simulation interface. It must not receive access to the host operating system, personal files, accounts, unrestricted internet, software installation, spending, or the ability to modify its own code or disable safeguards.

## License

License not yet selected.