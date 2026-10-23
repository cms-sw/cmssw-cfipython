import FWCore.ParameterSet.Config as cms

def HGCalWaferIDTester(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalWaferIDTester',
    nameSense = cms.string('HGCalHESiliconSensitive'),
    fileName = cms.string('cellIDHEF.txt'),
    mode = cms.int32(1),
    shift = cms.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
