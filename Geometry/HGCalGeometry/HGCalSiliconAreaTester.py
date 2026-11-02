import FWCore.ParameterSet.Config as cms

def HGCalSiliconAreaTester(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalSiliconAreaTester',
    nameDetector = cms.string('HGCalHESiliconSensitive'),
    nSkip = cms.int32(1000),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
