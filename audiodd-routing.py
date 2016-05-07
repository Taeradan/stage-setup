from mididings import *

config(
        backend = 'jack',
        client_name = 'audiodd_routing',
        out_ports = ['taurus','polybass','mellotron','calfcontrols']
)

taurus = Print('taurus: ') >> Output('taurus', 1)
polybass = Print('polybass: ') >> Output('polybass', 1)
mellotron = Print('mellotron: ') >> Output('mellotron', 1)

pk5 = taurus
clavier = KeySplit('c2', polybass, mellotron)

run(
        patch = ChannelSplit({1: pk5, 2: clavier})
)
