import FWCore.ParameterSet.Config as cms

def PatTrackAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('PatTrackAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
