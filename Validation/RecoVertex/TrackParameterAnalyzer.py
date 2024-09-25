import FWCore.ParameterSet.Config as cms

def TrackParameterAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('TrackParameterAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
