import FWCore.ParameterSet.Config as cms

def TrackProbabilityAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('TrackProbabilityAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
