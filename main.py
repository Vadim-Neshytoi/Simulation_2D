import sys
from controller.controller import Controller
from map.map import Map
from rendering.renderer import Renderer
from simulation.simulation import Simulation
from controller.input.windows_input import WindowsInputProvider
from controller.input.unix_input import UnixInputProvider



if __name__ == "__main__":
    my_map = Map(20, 20)
    simulate = Simulation(my_map)
    renderer = Renderer(my_map)
    input_provider = WindowsInputProvider() if sys.platform == "win32" else UnixInputProvider()
    controller = Controller(simulate, renderer, input_provider)
    controller.run()









