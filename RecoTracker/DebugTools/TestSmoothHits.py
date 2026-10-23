import FWCore.ParameterSet.Config as cms

def TestSmoothHits(*args, **kwargs):
  mod = cms.EDAnalyzer('TestSmoothHits',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
