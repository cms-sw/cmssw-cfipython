import FWCore.ParameterSet.Config as cms

def TrackReader(*args, **kwargs):
  mod = cms.EDAnalyzer('TrackReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
