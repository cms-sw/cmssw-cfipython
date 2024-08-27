import FWCore.ParameterSet.Config as cms

def TrackAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('TrackAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
