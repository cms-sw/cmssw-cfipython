import FWCore.ParameterSet.Config as cms

def PPSTimingCalibrationWriter(**kwargs):
  mod = cms.EDAnalyzer('PPSTimingCalibrationWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
