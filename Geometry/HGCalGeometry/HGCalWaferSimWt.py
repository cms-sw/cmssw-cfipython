import FWCore.ParameterSet.Config as cms

def HGCalWaferSimWt(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalWaferSimWt',
    detectorNames = cms.vstring(
      'HGCalEESensitive',
      'HGCalHESiliconSensitive'
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
