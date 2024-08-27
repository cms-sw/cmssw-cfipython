import FWCore.ParameterSet.Config as cms

def HGCalGeometryRotTest(**kwargs):
  mod = cms.EDAnalyzer('HGCalGeometryRotTest',
    detectorName = cms.string('HGCalHESiliconSensitive'),
    layers = cms.vint32(
      27,
      28,
      29,
      30,
      31,
      32
    ),
    waferUs = cms.vint32(
      -2,
      -3,
      1,
      -8,
      2,
      8
    ),
    waferVs = cms.vint32(
      0,
      -2,
      3,
      0,
      9,
      0
    ),
    cellUs = cms.vint32(
      16,
      4,
      8,
      11,
      11,
      5
    ),
    cellVs = cms.vint32(
      20,
      10,
      17,
      13,
      9,
      2
    ),
    types = cms.vint32(
      0,
      0,
      0,
      2,
      2,
      2
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
