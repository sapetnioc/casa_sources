'''
Read components in components.yaml keeping items order even in Python 3.6
This script is called from CMake with the appropriate current directory.
'''

import yaml
from collections import OrderedDict

def ordered_load(stream, Loader=yaml.SafeLoader, object_pairs_hook=OrderedDict):
    class OrderedLoader(Loader):
        pass
    def construct_mapping(loader, node):
        loader.flatten_mapping(node)
        return object_pairs_hook(loader.construct_pairs(node))
    OrderedLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        construct_mapping)
    return yaml.load(stream, OrderedLoader)


components = ordered_load(open('components.yaml'))
print(';'.join(name for name, component in components['repositories'].items() if component.get('brainvisa-cmake') != 'ignore'),end='')
