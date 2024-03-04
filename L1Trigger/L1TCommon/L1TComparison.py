import FWCore.ParameterSet.Config as cms

def L1TComparison(**kwargs):
  mod = cms.EDAnalyzer('L1TComparison',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
