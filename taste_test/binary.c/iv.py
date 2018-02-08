#! /usr/bin/python

Ada, C, GUI, SIMULINK, VHDL, OG, RTDS, SYSTEM_C, SCADE6, VDM, CPP = range(11)
thread, passive, unknown = range(3)
PI, RI = range(2)
synch, asynch = range(2)
param_in, param_out = range(2)
UPER, NATIVE, ACN = range(3)
cyclic, sporadic, variator, protected, unprotected = range(5)
enumerated, sequenceof, sequence, set, setof, integer, boolean, real, choice, octetstring, string = range(11)
functions = {}

functions['console'] = {
    'name_with_case' : 'console',
    'runtime_nature': thread,
    'language': C,
    'zipfile': '',
    'interfaces': {},
    'functional_states' : {}
}

functions['console']['interfaces']['trigger'] = {
    'port_name': 'trigger',
    'parent_fv': 'console',
    'direction': PI,
    'in': {},
    'out': {},
    'synchronism': asynch,
    'rcm': cyclic,
    'period': 2000,
    'wcet_low': 0,
    'wcet_low_unit': 'ms',
    'wcet_high': 0,
    'wcet_high_unit': 'ms',
    'distant_fv': '',
    'calling_threads': {},
    'distant_name': '',
    'queue_size': 1
}

functions['console']['interfaces']['trigger']['paramsInOrdered'] = []

functions['console']['interfaces']['trigger']['paramsOutOrdered'] = []

functions['console']['interfaces']['tm'] = {
    'port_name': 'tm',
    'parent_fv': 'console',
    'direction': PI,
    'in': {},
    'out': {},
    'synchronism': asynch,
    'rcm': variator,
    'period': 0,
    'wcet_low': 0,
    'wcet_low_unit': 'ms',
    'wcet_high': 0,
    'wcet_high_unit': 'ms',
    'distant_fv': '',
    'calling_threads': {},
    'distant_name': '',
    'queue_size': 1
}

functions['console']['interfaces']['tm']['paramsInOrdered'] = ['packet']

functions['console']['interfaces']['tm']['paramsOutOrdered'] = []

functions['console']['interfaces']['tm']['in']['packet'] = {
    'type': 'PusPacket',
    'asn1_module': 'PUS_CcsdsPacket',
    'basic_type': sequence,
    'asn1_filename': '/tmp/uniqhomeesrocosDesktoptaste_test__iv_1_3.aadl/dataview-uniq.asn',
    'encoding': NATIVE,
    'interface': 'tm',
    'param_direction': param_in
}

functions['console']['interfaces']['tc'] = {
    'port_name': 'tc',
    'parent_fv': 'console',
    'direction': RI,
    'in': {},
    'out': {},
    'synchronism': asynch,
    'rcm': sporadic,
    'period': 0,
    'wcet_low': 0,
    'wcet_low_unit': '',
    'wcet_high': 0,
    'wcet_high_unit': '',
    'distant_fv': 'roberto',
    'calling_threads': {},
    'distant_name': 'tc',
    'queue_size': 1
}

functions['console']['interfaces']['tc']['paramsInOrdered'] = ['packet']

functions['console']['interfaces']['tc']['paramsOutOrdered'] = []

functions['console']['interfaces']['tc']['in']['packet'] = {
    'type': 'PusPacket',
    'asn1_module': 'PUS_CcsdsPacket',
    'basic_type': sequence,
    'asn1_filename': '/tmp/uniqhomeesrocosDesktoptaste_test__iv_1_3.aadl/dataview-uniq.asn',
    'encoding': NATIVE,
    'interface': 'tc',
    'param_direction': param_in
}

functions['roberto'] = {
    'name_with_case' : 'roberTO',
    'runtime_nature': thread,
    'language': C,
    'zipfile': '',
    'interfaces': {},
    'functional_states' : {}
}

functions['roberto']['interfaces']['tc'] = {
    'port_name': 'tc',
    'parent_fv': 'roberto',
    'direction': PI,
    'in': {},
    'out': {},
    'synchronism': asynch,
    'rcm': sporadic,
    'period': 0,
    'wcet_low': 0,
    'wcet_low_unit': 'ms',
    'wcet_high': 0,
    'wcet_high_unit': 'ms',
    'distant_fv': '',
    'calling_threads': {},
    'distant_name': '',
    'queue_size': 1
}

functions['roberto']['interfaces']['tc']['paramsInOrdered'] = ['packet']

functions['roberto']['interfaces']['tc']['paramsOutOrdered'] = []

functions['roberto']['interfaces']['tc']['in']['packet'] = {
    'type': 'PusPacket',
    'asn1_module': 'PUS_CcsdsPacket',
    'basic_type': sequence,
    'asn1_filename': '/tmp/uniqhomeesrocosDesktoptaste_test__iv_1_3.aadl/dataview-uniq.asn',
    'encoding': NATIVE,
    'interface': 'tc',
    'param_direction': param_in
}

functions['roberto']['interfaces']['trigger'] = {
    'port_name': 'trigger',
    'parent_fv': 'roberto',
    'direction': PI,
    'in': {},
    'out': {},
    'synchronism': asynch,
    'rcm': cyclic,
    'period': 5000,
    'wcet_low': 0,
    'wcet_low_unit': 'ms',
    'wcet_high': 0,
    'wcet_high_unit': 'ms',
    'distant_fv': '',
    'calling_threads': {},
    'distant_name': '',
    'queue_size': 1
}

functions['roberto']['interfaces']['trigger']['paramsInOrdered'] = []

functions['roberto']['interfaces']['trigger']['paramsOutOrdered'] = []

functions['roberto']['interfaces']['tm'] = {
    'port_name': 'tm',
    'parent_fv': 'roberto',
    'direction': RI,
    'in': {},
    'out': {},
    'synchronism': asynch,
    'rcm': sporadic,
    'period': 0,
    'wcet_low': 0,
    'wcet_low_unit': '',
    'wcet_high': 0,
    'wcet_high_unit': '',
    'distant_fv': 'console',
    'calling_threads': {},
    'distant_name': 'tm',
    'queue_size': 1
}

functions['roberto']['interfaces']['tm']['paramsInOrdered'] = ['packet']

functions['roberto']['interfaces']['tm']['paramsOutOrdered'] = []

functions['roberto']['interfaces']['tm']['in']['packet'] = {
    'type': 'PusPacket',
    'asn1_module': 'PUS_CcsdsPacket',
    'basic_type': sequence,
    'asn1_filename': '/tmp/uniqhomeesrocosDesktoptaste_test__iv_1_3.aadl/dataview-uniq.asn',
    'encoding': NATIVE,
    'interface': 'tm',
    'param_direction': param_in
}
