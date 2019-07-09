from gym.envs.registration import register

register(id='briscola-sp-v0',
         entry_point='gym_briscola.envs:BriscolaSelfPlayEnv')
