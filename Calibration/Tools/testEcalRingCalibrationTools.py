import FWCore.ParameterSet.Config as cms

def testEcalRingCalibrationTools(**kwargs):
  mod = cms.EDAnalyzer('testEcalRingCalibrationTools',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
