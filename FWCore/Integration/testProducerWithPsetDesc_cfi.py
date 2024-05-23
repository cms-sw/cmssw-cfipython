import FWCore.ParameterSet.Config as cms

from .ProducerWithPSetDesc import ProducerWithPSetDesc

testProducerWithPsetDesc = ProducerWithPSetDesc(
  testingAutoGeneratedCfi = True,
  p_int = 2147483647,
  p_int_untracked = -2147483647,
  p_int_opt = 0,
  p_int_optuntracked = 7,
  vint1 = [],
  vint2 = [2147483647],
  vint3 = [
    2147483647,
    -2147483647
  ],
  vint4 = [
    2147483647,
    -2147483647,
    0
  ],
  uint1 = 4294967295,
  uint2 = 0,
  vuint1 = [],
  vuint2 = [4294967295],
  vuint3 = [
    4294967295,
    0
  ],
  vuint4 = [
    4294967295,
    0,
    11
  ],
  vuint5 = [
    4294967295,
    0,
    11,
    21,
    31,
    41
  ],
  int64v1 = 9000000000000000000,
  int64v2 = -9000000000000000000,
  int64v3 = 0,
  vint64v1 = [],
  vint64v2 = [9000000000000000000],
  vint64v3 = [
    9000000000000000000,
    -9000000000000000000
  ],
  vint64v4 = [
    9000000000000000000,
    -9000000000000000000,
    0
  ],
  uint64v1 = 18000000000000000000,
  uint64v2 = 0,
  vuint64v1 = [],
  vuint64v2 = [18000000000000000000],
  vuint64v3 = [
    18000000000000000000,
    0
  ],
  vuint64v4 = [
    18000000000000000000,
    0,
    11
  ],
  doublev1 = 2.2250738585072014e-308,
  doublev2 = 0,
  doublev3 = 0.3,
  vdoublev1 = [],
  vdoublev2 = [1e+300],
  vdoublev3 = [
    1e+300,
    0
  ],
  vdoublev4 = [
    1e+300,
    0,
    11
  ],
  vdoublev5 = [
    1e+300,
    0,
    11,
    0.3
  ],
  boolv1 = True,
  boolv2 = False,
  stringv1 = 'Hello',
  stringv2 = '',
  vstringv1 = [],
  vstringv2 = ['Hello'],
  vstringv3 = [
    'Hello',
    'World'
  ],
  vstringv4 = [
    'Hello',
    'World',
    ''
  ],
  eventIDv1 = (11, 0, 12),
  eventIDv2 = (101, 0, 102),
  vEventIDv1 = [],
  vEventIDv2 = ['1000:1100'],
  vEventIDv3 = [
    '1000:1100',
    '10000:11000'
  ],
  vEventIDv4 = [
    '1000:1100',
    '10000:11000',
    '100000:110000'
  ],
  luminosityIDv1 = (11, 12),
  luminosityIDv2 = (101, 102),
  vLuminosityBlockIDv1 = [],
  vLuminosityBlockIDv2 = ['1000:1100'],
  vLuminosityBlockIDv3 = [
    '1000:1100',
    '10000:11000'
  ],
  vLuminosityBlockIDv4 = [
    '1000:1100',
    '10000:11000',
    '100000:110000'
  ],
  lumiRangev1 = ('1:1-9:9'),
  lumiRangev2 = ('3:4-1000:1000'),
  vLumiRangev1 = [],
  vLumiRangev2 = ['1:1-9:9'],
  vLumiRangev3 = [
    '1:1-9:9',
    '3:4-1000:1000'
  ],
  eventRangev1 = ('1:1-8:8'),
  eventRangev2 = ('3:4-1001:1002'),
  vEventRangev1 = [],
  vEventRangev2 = ['1:1-8:8'],
  vEventRangev3 = [
    '1:1-8:8',
    '3:4-1001:1002'
  ],
  inputTagv1 = ('One', 'Two', 'Three'),
  inputTagv2 = ('One', 'Two'),
  inputTagv3 = ('One'),
  inputTagv4 = ('One', '', 'Three'),
  vInputTagv1 = [],
  vInputTagv2 = ['One:Two:Three'],
  vInputTagv3 = [
    'One:Two:Three',
    'One:Two'
  ],
  vInputTagv4 = [
    'One:Two:Three',
    'One:Two',
    'One'
  ],
  vInputTagv5 = [
    'One:Two:Three',
    'One:Two',
    'One',
    'One::Three'
  ],
  esinputTagv1 = ('One', 'Two'),
  esinputTagv2 = ('One', ''),
  esinputTagv3 = ('', 'Two'),
  vESInputTagv1 = [],
  vESInputTagv2 = ['One:Two'],
  vESInputTagv3 = [
    'One:Two',
    'One:'
  ],
  vESInputTagv4 = [
    'One:Two',
    'One:',
    ':Two'
  ],
  fileInPath = 'FWCore/Integration/plugins/ProducerWithPSetDesc.cc',
  bar = dict(
    Drinks = 5,
    uDrinks = 5,
    oDrinks = 5,
    ouDrinks = 5
  ),
  test104 = [
    cms.PSet()
  ],
  test105 = [
  ],
  test1 = 0.1,
  test2 = 0.2,
  testA = 'fooA',
  testB = 100,
  testC = 101,
  oiswitch = 1,
  oivalue1 = cms.double(101),
  oivalue2 = cms.double(101),
  testDeeplyNested2 = dict(
    bswitch = False,
    bvalue1 = 101,
    bvalue2 = 101,
    iswitch = 1,
    ivalue1 = 101,
    ivalue2 = 101,
    sswitch = '1',
    svalue1 = 101,
    svalue2 = 101,
    testint = 1000
  ),
  bars = [
    cms.PSet(
      oDrinks = cms.uint32(11)
    ),
    cms.PSet(
      ndouDrinks = cms.untracked.uint32(11),
      oDrinks = cms.uint32(11),
      ouDrinks = cms.untracked.uint32(11),
      testDeeplyNested = cms.PSet(
        testint = cms.int32(2)
      ),
      anotherVPSet = cms.VPSet(
        cms.PSet(),
        cms.PSet(
          xvalue = cms.int32(17)
        )
      )
    )
  ],
  subpset = dict(
    xvalue = 11,
    bar = dict(
      Drinks = 5,
      uDrinks = 5,
      oDrinks = 5,
      ouDrinks = 5
    )
  ),
  wildcardPset = cms.PSet(
    p_uint_opt = cms.uint32(0),
    allowAnyLabel_ = cms.optional.int32
  ),
  switchPset = dict(
    iswitch = 1,
    ivalue1 = 101,
    ivalue2 = 101,
    addTeVRefits = True,
    pickySrc = (''),
    tpfmsSrc = ('')
  ),
  xorPset = cms.PSet(
    name = cms.string('11'),
    name1 = cms.string('11'),
    name3 = cms.string('11')
  ),
  orPset = cms.PSet(
    x1 = cms.string('11'),
    y1 = cms.string('11')
  ),
  andPset = cms.PSet(
    x1 = cms.string('11'),
    x2 = cms.uint32(11),
    y1 = cms.string('11'),
    y2 = cms.uint32(11),
    z1 = cms.string('11'),
    z2 = cms.uint32(11),
    b1 = cms.string('11'),
    b2 = cms.uint32(11),
    b3 = cms.uint32(11),
    b4 = cms.uint32(11),
    b5 = cms.uint32(11),
    b6 = cms.uint32(11)
  ),
  ifExistsPset = cms.PSet(
    x1 = cms.uint32(11),
    x2 = cms.string('11'),
    z1 = cms.uint32(11),
    z2 = cms.string('11')
  ),
  allowedLabelsPset = cms.PSet(
    p_int_opt = cms.int32(0),
    testAllowedLabels = cms.vstring(),
    testAllowedLabelsUntracked = cms.untracked.vstring(),
    testWithSet = cms.untracked.vstring(),
    testWithVectorOfSets = cms.untracked.vstring()
  ),
  noDefaultPset3 = dict(),
  noDefaultPset4 = dict(),
  plugin = cms.PSet(
    value = cms.int32(5),
    type = cms.string('edmtestAnotherValueMaker')
  
  ),
  plugin1 = cms.PSet(),
  plugin2 = [
  ],
  plugin3 = [
    cms.PSet(
      type = cms.string('edmtestAnotherOneMaker')
    ),
    cms.PSet(
      type = cms.string('edmtestAnotherValueMaker'),
      value = cms.int32(11)
    )
  ],
  plugin4 = cms.PSet(
    value = cms.int32(5),
    pluginRecursive = cms.PSet(),
    type = cms.string('edmtestAnotherMakerWithRecursivePlugin')
  
  ),
  plugin5 = [
    cms.PSet(
      type = cms.string('edmtestAnotherOneMaker')
    ),
    cms.PSet(
      type = cms.string('edmtestAnotherMakerWithRecursivePlugin'),
      value = cms.int32(11)
    )
  ]
)
