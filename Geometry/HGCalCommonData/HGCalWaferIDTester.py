import FWCore.ParameterSet.Config as cms

def HGCalWaferIDTester(**kwargs):
  mod = cms.EDAnalyzer('HGCalWaferIDTester',
    nameSense = cms.string('HGCalHESiliconSensitive'),
    fileName = cms.string('cellIDHEF.txt'),
    mode = cms.int32(1),
    shift = cms.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
