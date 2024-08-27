import FWCore.ParameterSet.Config as cms

def PPSTimingCalibrationAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('PPSTimingCalibrationAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
