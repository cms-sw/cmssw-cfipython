import FWCore.ParameterSet.Config as cms

def PPSTimingCalibrationLUTAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('PPSTimingCalibrationLUTAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
