import FWCore.ParameterSet.Config as cms

def TrackMix(*args, **kwargs):
  mod = cms.EDAnalyzer('TrackMix',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
