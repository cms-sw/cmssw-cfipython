import FWCore.ParameterSet.Config as cms

def testEcalRingCalibrationTools(*args, **kwargs):
  mod = cms.EDAnalyzer('testEcalRingCalibrationTools',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
