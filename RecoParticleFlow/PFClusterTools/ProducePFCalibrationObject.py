import FWCore.ParameterSet.Config as cms

def ProducePFCalibrationObject(*args, **kwargs):
  mod = cms.EDAnalyzer('ProducePFCalibrationObject',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
