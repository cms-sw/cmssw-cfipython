import FWCore.ParameterSet.Config as cms

def TestSmoothHits(**kwargs):
  mod = cms.EDAnalyzer('TestSmoothHits',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
