from abaqus import session
from abaqusConstants import *
import numpy as np
vname = session.currentViewportName
vp1 = session.viewports[vname]
odbname = vp1.odbDisplay.name
contour_opt = vp1.odbDisplay.contourOptions

def define_spectrums():
    test = list(set(session.spectrums.keys()).difference(['BuPu', "BuPu_RdOrYl", "RdOr", "RdOrYl"]))
    if len(test) > 0:
        session.Spectrum(name="BuPu", colors =('#023858', '#02395a', '#023a5b', '#023b5d', '#023c5f', '#023d60', '#023e62', '#023f64', '#034166', '#034267', '#034369', '#03446b', '#03456c', '#03466e', '#034770', '#034871', '#034973', '#034a75', '#034b76', '#034c78', '#034d7a', '#034e7b', '#034f7d', '#03517f', '#045280', '#045382', '#045483', '#045585', '#045687', '#045788', '#04588a', '#04598c', '#045a8d', '#045b8e', '#045b8f', '#045c91', '#045d92', '#045e93', '#045e94', '#045f95', '#056096', '#056097', '#056198', '#05629a', '#05629b', '#05639c', '#05649d', '#05649e', '#05659f', '#0566a0', '#0567a1', '#0567a2', '#0568a3', '#0569a5', '#0569a6', '#056aa7', '#056ba8', '#056ba9', '#056caa', '#056dab', '#056dac', '#056ead', '#056fae', '#056faf', '#0570b0', '#0771b1', '#0972b1', '#0a73b2', '#0c74b2', '#0d75b3', '#0f76b3', '#1077b4', '#1278b4', '#1479b5', '#157ab5', '#177bb6', '#187cb6', '#1a7db7', '#1b7eb7', '#1d7fb8', '#1e80b8', '#2081b9', '#2282b9', '#2383ba', '#2584ba', '#2685bb', '#2886bb', '#2987bc', '#2b88bc', '#2d89bd', '#2e8abd', '#308bbe', '#318cbe', '#338dbf', '#348ebf', '#368fc0', '#3890c0', '#3a91c1', '#3c92c1', '#3e93c2', '#4094c2', '#4194c3', '#4395c3', '#4596c4', '#4797c4', '#4998c5', '#4b98c5', '#4d99c6', '#4f9ac6', '#519bc7', '#539cc7', '#559dc8', '#579dc8', '#599ec9', '#5b9fc9', '#5da0ca', '#5fa0ca', '#61a1ca', '#63a2cb', '#64a3cb', '#66a3cc', '#68a4cc', '#6aa5cd', '#6ca6cd', '#6ea6cd', '#70a7ce', '#72a8ce', '#74a9cf', '#76a9cf', '#77aad0', '#79abd0', '#7aabd0', '#7cacd1', '#7eacd1', '#7fadd1', '#81aed2', '#82aed2', '#84afd3', '#85b0d3', '#87b0d3', '#89b1d4', '#8ab1d4', '#8cb2d4', '#8db3d5', '#8fb3d5', '#90b4d6', '#92b5d6', '#94b5d6', '#95b6d7', '#97b6d7', '#98b7d7', '#9ab8d8', '#9bb8d8', '#9db9d9', '#9fbad9', '#a0bad9', '#a2bbda', '#a3bcda', '#a5bcda', '#a6bddb', '#a8bddb', '#a9bedc', '#aabfdc', '#acbfdc', '#adc0dd', '#aec1dd', '#b0c1dd', '#b1c2de', '#b2c2de', '#b4c3df', '#b5c4df', '#b6c4df', '#b8c5e0', '#b9c6e0', '#bac6e1', '#bcc7e1', '#bdc7e1', '#bec8e2', '#c0c9e2', '#c1cae2', '#c2cae2', '#c3cbe3', '#c5cce3', '#c6cce3', '#c7cde4', '#c9cee4', '#cacee4', '#cbcfe5', '#cdd0e5', '#ced0e5', '#cfd1e6', '#d1d2e6', '#d2d3e6', '#d3d3e7', '#d3d4e7', '#d4d5e7', '#d5d5e8', '#d6d6e8', '#d7d7e9', '#d8d7e9', '#d9d8e9', '#dad9ea', '#dad9ea', '#dbdaea', '#dcdbeb', '#dddbeb', '#dedcec', '#dfddec', '#e0deec', '#e1deed', '#e1dfed', '#e2dfed', '#e3e0ee', '#e4e1ee', '#e5e1ef', '#e6e2ef', '#e7e3ef', '#e8e3f0', '#e8e4f0', '#e9e4f0', '#eae5f1', '#ebe6f1', '#ece6f2', '#ede7f2', '#ede7f2', '#eee8f3', '#efe8f3', '#efe9f3', '#f0e9f4', '#f0eaf4', '#f1eaf4', '#f1ebf4', '#f2ebf5', '#f3ecf5', '#f3ecf5', '#f4edf6', '#f4edf6', '#f5eef6', '#f5eef7', '#f6eff7', '#f7eff7', '#f7f0f7', '#f8f0f8', '#f8f1f8', '#f9f1f8', '#f9f2f8', '#faf2f9', '#faf3f9', '#fbf3f9', '#fcf4f9', '#fcf4fa', '#fdf5fa', '#fdf5fa', '#fef6fa', '#fef6fb', '#fff7fb'))
        session.Spectrum(name="BuPu_RdOrYl", colors =['#023858', '#034973', '#045a8d', '#05659f', '#0570b0', '#1e80b8', '#3790c0', '#569dc8', '#75a9cf', '#8eb3d5', '#a7bddb', '#bcc7e1', '#d1d2e6', '#dfddec', '#ede7f2', '#f6eff7', '#fff7fb', '#ffffcc', '#fff7b7', '#ffeda1', '#ffe48c', '#fed977', '#fec662', '#feb34d', '#fea044', '#fd8e3c', '#fd6e33', '#fc4f2a', '#f03523', '#e31a1c', '#d00d21', '#bd0026', '#9f0026', '#800026'])
        session.Spectrum(name="RdOr", colors =('#fff7ec', '#fff2e0', '#ffedd4', '#fee7c8', '#fee1b9', '#fedaab', '#fdd29d', '#fdca94', '#fdc08a', '#fdb57f', '#fda670', '#fc9661', '#fa8757', '#f67951', '#f16b4a', '#ea5a40', '#e14630', '#d93422', '#cd2317', '#c1120c', '#b40201', '#a30000', '#910000', '#7f0000'))
        session.Spectrum(name="RdOrYl", colors =('#ffffcc', '#fff9be', '#fff3af', '#ffeca0', '#ffe691', '#ffdf83', '#fed674', '#fec966', '#febb56', '#feae4b', '#fea144', '#fd943f', '#fd8339', '#fd6d33', '#fc582c', '#f74427', '#ee3022', '#e51e1d', '#d9131f', '#cb0a22', '#be0126', '#aa0026', '#950026', '#800026'))

def rescale_all_frames():
    define_spectrums()
    contour_opt.setValues(intervalType=UNIFORM,
                          maxAutoCompute=ON,
                          minAutoCompute=ON)
    steps = session.odbs[odbname].steps.values()
    
    min_list = []
    max_list = []
    for s in steps:
        for f in s.frames:
            vp1.odbDisplay.setFrame(frame = f)
            min_val, max_val = contour_opt.autoMinValue, contour_opt.autoMaxValue
            min_list.append(min_val)
            max_list.append(max_val)
    min_val, max_val = min(min_list), max(max_list)

    if min_val < 0.0 and max_val > 0.0:
        lower_list = list(np.linspace(min_val, 0.0, 6, endpoint=False))
        upper_list = list(np.linspace(0.0, max_val, 7))
        
        lower_list.extend(upper_list)
        vp1.odbDisplay.contourOptions.setValues(spectrum='BuPu_RdOrYl',
                                                intervalType=USER_DEFINED,
                                                intervalValues=lower_list)
    elif min_val >= 0.0:
        upper_list = list(np.linspace(0.0, max_val, 13))
        vp1.odbDisplay.contourOptions.setValues(spectrum='RdOrYl',
                                                intervalType=USER_DEFINED,
                                                intervalValues=upper_list)
    elif max_val <= 0.0:
        lower_list = list(np.linspace(min_val, 0.0, 13))
        vp1.odbDisplay.contourOptions.setValues(spectrum='BuPu',
                                                intervalType=USER_DEFINED,
                                                intervalValues=lower_list)

def rescale_current_frame():
    define_spectrums()
    contour_opt.setValues(intervalType=UNIFORM,
                            maxAutoCompute=ON,
                            minAutoCompute=ON)
    
    min_val, max_val = contour_opt.autoMinValue, contour_opt.autoMaxValue

    if min_val < 0.0 and max_val > 0.0:
        lower_list = list(np.linspace(min_val, 0.0, 6, endpoint=False))
        upper_list = list(np.linspace(0.0, max_val, 7))
        
        lower_list.extend(upper_list)
        vp1.odbDisplay.contourOptions.setValues(spectrum='sp_custom2',
                                                intervalType=USER_DEFINED,
                                                intervalValues=lower_list)
    elif min_val >= 0.0:
        upper_list = list(np.linspace(0.0, max_val, 13))
        vp1.odbDisplay.contourOptions.setValues(spectrum='RdOrYl',
                                                intervalType=USER_DEFINED,
                                                intervalValues=upper_list)
    elif max_val <= 0.0:
        lower_list = list(np.linspace(min_val, 0.0, 13))
        vp1.odbDisplay.contourOptions.setValues(spectrum='BuPu',
                                                intervalType=USER_DEFINED,
                                                intervalValues=lower_list)

def set_uniform():
    define_spectrums()
    contour_opt.setValues(intervalType=UNIFORM,
                          maxAutoCompute=ON,
                          minAutoCompute=ON)