from UI import UI
from Controller import Controller
from Problem import Problem
from State import State

problem = Problem(State())

ctrl = Controller(problem)
ui = UI(ctrl)
ui.mainMenu()