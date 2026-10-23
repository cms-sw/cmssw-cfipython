import FWCore.ParameterSet.Config as cms

def TestHits(*args, **kwargs):
  mod = cms.EDAnalyzer('TestHits',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
