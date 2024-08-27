import FWCore.ParameterSet.Config as cms

def PPSTimingCalibrationLUTWriter(**kwargs):
  mod = cms.EDAnalyzer('PPSTimingCalibrationLUTWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
