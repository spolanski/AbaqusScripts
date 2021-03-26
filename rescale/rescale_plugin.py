from abaqusGui import getAFXApp, FXXPMIcon
import os
import i18n

toolset = getAFXApp().getAFXMainWindow().getPluginToolset()

toolset.registerKernelMenuButton(
    moduleName='rescale',
    functionName='rescale_current_frame()',
    buttonText=i18n.tr('Rescale|Rescale from frame'),
    version='1.0',
    author='spolanski',
    description='',
)

toolset.registerKernelMenuButton(
    moduleName='rescale',
    functionName='rescale_all_frames()',
    buttonText=i18n.tr('Rescale|Rescale from all frames'),
    version='1.0',
    author='spolanski',
    description='',
)

toolset.registerKernelMenuButton(
    moduleName='rescale',
    functionName='set_uniform()',
    buttonText=i18n.tr('Rescale|Set uniform'),
    version='1.0',
    author='spolanski',
    description='',
)