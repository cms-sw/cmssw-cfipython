import FWCore.ParameterSet.Config as cms

def DTNoiseCalibration(**kwargs):
  mod = cms.EDAnalyzer('DTNoiseCalibration',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
