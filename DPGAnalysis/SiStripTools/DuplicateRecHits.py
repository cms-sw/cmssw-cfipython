import FWCore.ParameterSet.Config as cms

def DuplicateRecHits(*args, **kwargs):
  mod = cms.EDAnalyzer('DuplicateRecHits',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
