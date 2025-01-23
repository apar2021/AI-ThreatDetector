# backend/services/rl_anomaly_detector.py
import gymnasium as gym
import numpy as np
from stable_baselines3 import PPO
from typing import Dict, Any, List

class CybersecurityEnv(gym.Env):
    def __init__(self, network_data):
        super().__init__()
        self.network_data = network_data
        self.action_space = gym.spaces.Discrete(4)  
        self.observation_space = gym.spaces.Box(
            low=-np.inf, high=np.inf, 
            shape=(4,)  # Number of features
        )
        
        self.current_step = 0

    def reset(self):
        self.current_step = 0
        return self._extract_features()

    def _extract_features(self):
        return np.array([
            self.network_data['total_packets'],
            len(self.network_data['protocol_distribution']),
            sum(self.network_data['ip_traffic'].values()),
            self.current_step
        ])

    def step(self, action):
        # Simulate threat response
        reward = self._calculate_reward(action)
        
        self.current_step += 1
        done = self.current_step >= 100  # Max steps
        
        return self._extract_features(), reward, done, {}

    def _calculate_reward(self, action):
        # Reward based on mitigating potential threats
        risk_factor = len(self.network_data['protocol_distribution'])
        return -risk_factor if action == 0 else 1

def detect_anomalies(network_data: Dict[str, Any]) -> Dict[str, Any]:
    # Create environment
    env = CybersecurityEnv(network_data)
    
    # Load or train model
    try:
        model = PPO.load("ml_models/cybersecurity_model")
    except:
        # Train if no existing model
        model = PPO("MlpPolicy", env)
        model.learn(total_timesteps=10000)
        model.save("ml_models/cybersecurity_model")
    
    # Run inference
    obs = env.reset()
    done = False
    anomalies = []
    
    while not done:
        action, _ = model.predict(obs)
        obs, reward, done, _ = env.step(action)
        
        if reward < 0:
            anomalies.append({
                'action': int(action),
                'reward': float(reward)
            })
    
    return {
        'detected_anomalies': anomalies,
        'total_anomalies': len(anomalies)
    }