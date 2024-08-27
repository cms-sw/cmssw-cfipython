import FWCore.ParameterSet.Config as cms

def DTVDriftAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('DTVDriftAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
