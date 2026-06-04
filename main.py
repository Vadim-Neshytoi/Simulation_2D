from controller.controller import Controller
from map.map import Map
from rendering.renderer import Renderer
from simulation.simulation import Simulation



if __name__ == "__main__":
    my_map = Map(20, 20)
    simulate = Simulation(my_map)
    renderer = Renderer(my_map)
    controller = Controller(simulate, renderer)
    controller.run()









