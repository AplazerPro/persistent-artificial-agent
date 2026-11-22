# Architecture — Modular Simulation Platform

## Design principle

Keep the environment, agent, learning algorithm, reward rules, experiment controller, configuration, storage, and reporting independent. Prefer changing validated configuration over editing source code for ordinary experiments.

## Components

### 1. Experiment controller
Owns episode lifecycle, tick order, run identifiers, reset behaviour, checkpoints, and experiment orchestration. It records the authoritative event history.

### 2. Environment
Owns the grid, terrain, resources, object state, world rules, resource regeneration/depletion, and action execution. It does not decide what the agent should do.

### 3. Agent body and perception
Tracks position, energy, hunger, inventory, carrying capacity, and observations available at the current location. Perception must not silently reveal the entire world if visibility is meant to be limited.

### 4. Action interface and capability control
Defines supported actions, validates requests, checks permissions and preconditions, and returns explicit success/failure results. The experimenter controls which capabilities are available. A capability may exist in the simulation but be unavailable to the agent, or available but not yet understood by it.

### 5. Learning module
Implements the selected learning algorithm. Initial implementation: model-free tabular Q-learning. It should be replaceable without rewriting the environment.

### 6. Reward module
Calculates rewards from explicit, versioned rules. Reward changes must be recorded as experimental interventions.

### 7. Configuration manager
Loads and validates configuration, rejects invalid ranges and incompatible settings, and records a snapshot of the exact configuration used by each run.

### 8. Storage
Stores structured episode summaries, Q-table checkpoints, and append-only event records. SQLite is suitable for indexed records; JSONL is suitable for streaming event logs; CSV is suitable for analysis exports.

### 9. Reporting and diagnostics
Generates an episode report and a master experiment report. It distinguishes agent performance problems from simulation defects, technical failures, and measurement problems.

### 10. Visualization
Optional lightweight 2D display and plots. The simulation must be able to run without visualization to conserve resources.

## Tick order

1. Environment requests an action for the current tick.
2. Agent receives its permitted observation.
3. Learning module selects an available action.
4. Action interface validates and executes it.
5. Environment advances world state and time.
6. Reward module calculates the reward for the transition.
7. Learning module updates its Q-value.
8. Controller records the event and checks termination.
9. Repeat until the episode ends.

One decision is made per tick. WAIT is an ordinary action; the world still advances.

## Data separation

Keep these concepts distinct:
- **World truth:** actual environment state, recorded by the controller.
- **Observation:** what the agent was allowed to perceive.
- **Agent knowledge/memory:** what the agent chose to record or infer.
- **Learned values:** numerical values such as Q(s,a).
- **Experiment record:** independent evidence of what occurred.

The agent must not be able to rewrite the authoritative experiment log.

## Memory approach

No automatic importance ranking or forgetting system is part of the design. The agent may choose what knowledge to record and how to use it. The system separately preserves the full event history. Retrieval should return matching records transparently and allow further inspection; it must not silently discard information.

## Configuration and reproducibility

Each run records:
- Configuration identifier and complete configuration snapshot.
- Source revision / code version.
- Random seed.
- Learning algorithm and parameters.
- State and action schema versions.
- Reward definition version.
- Start and end timestamps.
- Episode outcome and data-integrity status.

When state or action schemas change, do not silently reuse an incompatible Q-table. Start a new table or implement and document a migration.

## Resource constraints

Target low-memory local execution on a modest computer. Begin with a small grid, sparse tabular Q-values, compact event records, and no local language model. Benchmark before adding dependencies or visual effects.

## Safety boundary

The agent's authority ends at the simulation API. No host OS, shell, personal files, accounts, unrestricted network, installation, spending, or self-modification permissions. The controller validates every action and retains pause, reset, checkpoint, and resource-limit authority.