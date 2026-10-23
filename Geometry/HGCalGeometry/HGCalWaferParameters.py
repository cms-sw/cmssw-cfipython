import FWCore.ParameterSet.Config as cms

def HGCalWaferParameters(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalWaferParameters',
    nameDetector = cms.string('HGCalHESiliconSensitive'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
