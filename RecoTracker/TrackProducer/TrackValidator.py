import FWCore.ParameterSet.Config as cms

def TrackValidator(*args, **kwargs):
  mod = cms.EDAnalyzer('TrackValidator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
