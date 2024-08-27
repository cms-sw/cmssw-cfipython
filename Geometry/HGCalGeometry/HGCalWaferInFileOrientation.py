import FWCore.ParameterSet.Config as cms

def HGCalWaferInFileOrientation(**kwargs):
  mod = cms.EDAnalyzer('HGCalWaferInFileOrientation',
    detectorName = cms.string('HGCalHESiliconSensitive'),
    layers = cms.vint32(
      33,
      33,
      33,
      33,
      33,
      33
    ),
    waferUs = cms.vint32(
      12,
      12,
      -3,
      -3,
      -9,
      -9
    ),
    waferVs = cms.vint32(
      3,
      9,
      9,
      -12,
      3,
      -12
    ),
    types = cms.vint32(
      2,
      2,
      2,
      2,
      2,
      2
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
