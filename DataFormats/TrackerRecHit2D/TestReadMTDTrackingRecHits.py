import FWCore.ParameterSet.Config as cms

def TestReadMTDTrackingRecHits(*args, **kwargs):
  mod = cms.EDAnalyzer('TestReadMTDTrackingRecHits',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
