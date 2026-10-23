import FWCore.ParameterSet.Config as cms

def TrackCount(*args, **kwargs):
  mod = cms.EDAnalyzer('TrackCount',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
