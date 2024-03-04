import FWCore.ParameterSet.Config as cms

def DTT0PopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('DTT0PopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
