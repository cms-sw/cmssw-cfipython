import FWCore.ParameterSet.Config as cms

def PPSTimingCalibrationLUTAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('PPSTimingCalibrationLUTAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
