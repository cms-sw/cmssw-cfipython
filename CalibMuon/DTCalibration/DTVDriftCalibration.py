import FWCore.ParameterSet.Config as cms

def DTVDriftCalibration(**kwargs):
  mod = cms.EDAnalyzer('DTVDriftCalibration',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
