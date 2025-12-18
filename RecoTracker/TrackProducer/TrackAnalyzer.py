import FWCore.ParameterSet.Config as cms

def TrackAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('TrackAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
