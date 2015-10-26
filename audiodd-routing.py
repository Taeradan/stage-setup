from mididings import *

config(
        backend = 'jack',
        client_name = 'audiodd_routing',
        out_ports = ['taurus','polybass','calfcontrols']
)

taurus = Print('taurus: ') >> Output('taurus', 1)
polybass = Print('polybass: ') >> Output('polybass', 1)

run(
        patch = ChannelSplit({1: taurus, 2: polybass})
)
