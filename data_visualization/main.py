import multiprocessing

import gui
import data


def main():
    
    app = gui.TankLevelRegulatorGui()
        
    app.start()


if __name__ == "__main__":
    main()