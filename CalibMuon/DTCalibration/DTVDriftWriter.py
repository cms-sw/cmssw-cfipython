import FWCore.ParameterSet.Config as cms

def DTVDriftWriter(**kwargs):
  mod = cms.EDAnalyzer('DTVDriftWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
