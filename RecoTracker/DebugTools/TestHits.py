import FWCore.ParameterSet.Config as cms

def TestHits(**kwargs):
  mod = cms.EDAnalyzer('TestHits',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
