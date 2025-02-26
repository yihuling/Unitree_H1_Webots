"""
A dict recording the important hyperparameters.
"""
from base_declaration import *

ppo_config = {
    "algo": "PPO",
    "actor_lr": 0.000001,
    "critic_lr": 0.00001,
    "num_episode": 10000,
    "num_iteration": 10,
    "gamma": 0.9,
    "lmbda": 0.9,
    "hidden_dim": 128,
    "epoch": 1,
    "epsilon": 0.2,
    "seed": 0,
    "env_name": 'UnitreeH1_Standing',
    "model_dir": './ckpts/ppo/',
    "result_dir": './results/ppo/',
    "device": DEVICE1,
}
