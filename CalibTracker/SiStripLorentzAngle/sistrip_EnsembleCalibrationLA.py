import FWCore.ParameterSet.Config as cms

def sistrip_EnsembleCalibrationLA(*args, **kwargs):
  mod = cms.EDAnalyzer('sistrip::EnsembleCalibrationLA',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
