# from textRepr import prettyPrint as pr
# from abaqus import *
# from abaqusConstants import *
# from caeModules import *
#import odbAccess
#odbAccess.openOdb(path='myOdb.odb')                                # Abq/Vie
#session.openOdb(name='myOdb', path='stress.odb', readOnly=True)    # Abq/Cae
def main():
    # CubeHelix (http://www.mrao.cam.ac.uk/~dag/CUBEHELIX/)
    # UniformRainbow (https://peterkovesi.com/projects/colourmaps/index.html rainbow_bgyr_35-85_c72_n256)
    # Moreland (https://www.kennethmoreland.com/color-maps/)
    # Viridis (https://cran.r-project.org/web/packages/viridis/vignettes/intro-to-viridis.html)
    spectrums = {'CubeHelix': ['#2C2145', '#2B446D', '#226D74', '#2C905F',
                               '#56A244', '#96A242', '#D59B66', '#F99CA4',
                               '#FDADE1'],
                 'UniformRainbow': ['#0034F9', '#2A7F82', '#55A915', '#B9C11C',
                                    '#FDBC20', '#FE8212', '#FD482B'],
                 'Moreland': ['#3B4CC0', '#6282EA', '#8DB0FE', '#B8D0F9',
                              '#DDDDDD', '#F5C4AD', '#F49A7B', '#DE604D', '#B40426'],
                 'Viridis': ['#440154', '#472D7B', '#3B528B', '#2C728E', '#21918C',
                             '#28AE80', '#5EC962', '#ADDC30', '#FDE725'],
                 
                 }
    
    for name, colours in spectrums.items():
        session.Spectrum(name, colours)
        
if __name__ == '__main__':
    main()
