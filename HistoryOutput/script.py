# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 15:36:03 2020

To run script requires the History Output to be
requested before running the job. The History Output
definition is based on Set RF_POINT containing a point
where RF and U will be read from.
"""
from odbAccess import *

def main():
    odb = openOdb('00_test.odb', readOnly=True)
    rfPointSet = odb.rootAssembly.nodeSets['RF_POINT']
    histPoint = HistoryPoint(node=rfPointSet.nodes[0][0])
    tipHistories = odb.steps['Step-1'].getHistoryRegion(
            point=histPoint)
    
    RP_disp = [i[1] for i in tipHistories.historyOutputs['U2'].data]
    RP_force = [i[1] for i in tipHistories.historyOutputs['RF2'].data]
    
    # Following function can be used to create session XYDATA
    # newData = session.XYData(data = zip(RP_disp,RP_force),
    #                          name = 'REACTION_FORCE_VS_DISP',
    #                          legendLabel = 'REACTION_FORCE_VS_DISP',
    #                          xValuesLabel = 'Displacement [m]',
    #                          yValuesLabel = 'Reaction Force [N]',
    #                          axis1QuantityType = xyPlot.QuantityType(type=DISPLACEMENT),
    #                          axis2QuantityType = xyPlot.QuantityType(type=FORCE))
    
    combined = zip(RP_disp, RP_force)
    output = "\n".join("%.6f, \t%.6f" % tup for tup in combined)
    with open('data.csv', 'w') as f:
        f.write(output)
        
if __name__ == '__main__':
    main()
