# DDQNTSCA-PER: A Double Deep Q-Network with Prioritized Experience Replay for Decentralized Traffic Signal Control: 
This project offers a framework for optimizing traffic flow at complex intersections using a Double Deep Q-network along with Experience replay. By intelligently selecting traffic light phases, the agent aims to maximize traffic efficiency.
****DDQNTSCA-PER**: 
**Framework**: DDQNTSCA-PER.
**Context**: Traffic signal control at a multiple intersection.
**Environment**: Features a 4-way intersection with two incoming and two outgoing lanes per arm, each 150 meters long. Traffic lights are positioned such that each arm has dedicated lanes for specific movements.
**Traffic Generation:** Each episode generates 2,000 and 4,000 cars using the Weibull distribution and the normal distribution, following a dynamic pattern that contributes to the complexity of the environment.
Agent (DDQNTSCA-PER):
**Combined State Index (CSI)**: Compact representation integrating vehicle presence, speed normalization, and signal phase context.
**Action**: Selection of traffic light phases from predetermined options, each lasting 10 seconds.**
**Reward**: Based on cumulative waiting time reduction, incentivizing efficient traffic management.**
**Learning Mechanism**: Utilizes the Q-learning equation and a double deep Q neural network to update action values and learn state-action relationships.
**Neighbor-Aware Coordination**: Facilitates decentralized interaction between intersections.
**Improved Convergence Behavior**: Demonstrated via added training curves and stability analysis.
