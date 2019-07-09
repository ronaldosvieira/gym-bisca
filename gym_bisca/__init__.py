from gym.envs.registration import register

register(id='bisca-sp-v0',
         entry_point='gym_bisca.envs:BriscolaSelfPlayEnv')
