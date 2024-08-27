import FWCore.ParameterSet.Config as cms

def TestTrackHits(**kwargs):
  mod = cms.EDAnalyzer('TestTrackHits',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
