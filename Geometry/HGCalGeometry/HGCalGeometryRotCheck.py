import FWCore.ParameterSet.Config as cms

def HGCalGeometryRotCheck(*args, **kwargs):
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
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
