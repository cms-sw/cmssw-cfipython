import FWCore.ParameterSet.Config as cms

def TrackProbabilityAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('TrackProbabilityAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
