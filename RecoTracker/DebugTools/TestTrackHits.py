import FWCore.ParameterSet.Config as cms

def TestTrackHits(*args, **kwargs):
  mod = cms.EDAnalyzer('TestTrackHits',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
