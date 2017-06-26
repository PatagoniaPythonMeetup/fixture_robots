import unittest
import random 

from server import Robot

class TestBase(unittest.TestCase):
    def setUp(self):
        self.robots = [
            Robot("Ultron I", "Los Avengers","Nick Fury"),
            Robot("Wall-e I","Pixar","Sr. Disney"),
            Robot("EVA I","Pixar","Sr. Disney"),
            Robot("Sony I","R&H Mecanicos","Dt. Spooner"),
            Robot("Robocop I","O.C.P.","Bob Morthon"),
            Robot("Terminator I","Skynet","Jhon Connor"),
            Robot("R2-D2 I","La Republica","Obiwan Kenobi"),
            Robot("3-CPO I","La Republica","Anakin Skywalker"),
            Robot("BB-8 I","La Republica","Poe Dameron"),
            Robot("Ultron II", "Los Avengers","Nick Fury"),
            Robot("Wall-e II","Pixar","Sr. Disney"),
            Robot("EVA II","Pixar","Sr. Disney"),
            Robot("Sony II","R&H Mecanicos","Dt. Spooner"),
            Robot("Robocop II","O.C.P.","Bob Morthon"),
            Robot("Terminator II","Skynet","Jhon Connor"),
            Robot("R2-D2 II","La Republica","Obiwan Kenobi"),
            Robot("3-CPO II","La Republica","Anakin Skywalker"),
            Robot("BB-8 II","La Republica","Poe Dameron"),
            Robot("Rodney I", "Robots", "Sr. Ewan McGregor"),
            Robot("Rodney II", "Robots", "Sr. Ewan McGregor"),
            Robot("ED 209 I", "O.C.P.", "Bob Morthon"),
            Robot("ED 209 II", "O.C.P.", "Bob Morthon"),
            Robot("Johnny 5 I", "Cortocircuito", "Ally Sheedy"),
            Robot("Johnny 5 II", "Cortocircuito", "Ally Sheedy"),
            Robot("T-800 I", "Cyberdyne Systems", "Jhon Connor"),
            Robot("T-800 II", "Cyberdyne Systems", "Jhon Connor"),
            Robot("T-1000 I", "Cyberdyne Systems", "Arnie"),
            Robot("T-1000 II", "Cyberdyne Systems", "Arnie"),
            Robot("Roy Batty I", "Blade Runner", "Roy"),
            Robot("Roy Batty II", "Blade Runner", "Roy"),
            Robot("HAL 9000 I", "Discovery Uno", "David Bowman"),
            Robot("HAL 9000 II", "Discovery Uno", "David Bowman"),
            Robot("Ash I", "Nostromo", "Ellen Ripley"),
            Robot("Ash II", "Nostromo", "Ellen Ripley"),
            Robot("Optimus Prime I", "Transformers", "Ellen Ripley"),
            Robot("Optimus Prime II", "Transformers", "Ellen Ripley"),
            Robot("David Swinton I", "IA", "Ellen Ripley"),
            Robot("David Swinton II", "IA", "Ellen Ripley"),
            Robot("Teddy I", "IA", "Haley Joel Osment"),
            Robot("Teddy II", "IA", "Haley Joel Osment"),
            Robot("Centinelas I", "Matrix", "Neo"),
            Robot("Centinelas II", "Matrix", "Neo"),
            Robot("Bender I", "Futurama", "Philip J. Fry"),
            Robot("Bender II", "Futurama", "Philip J. Fry")
        ]
        random.shuffle(self.robots)