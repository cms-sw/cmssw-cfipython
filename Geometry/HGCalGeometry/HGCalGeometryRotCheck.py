import FWCore.ParameterSet.Config as cms

def HGCalGeometryRotCheck(**kwargs):
  mod = cms.EDAnalyzer('HGCalGeometryRotCheck',
    detectorName = cms.string('HGCalHESiliconSensitive'),
    layers = cms.vint32(
      27,
      28,
      29,
      30,
      31,
      32,
      33
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
