import FWCore.ParameterSet.Config as cms

def ArbitraryLogError(**kwargs):
  mod = cms.EDAnalyzer('ArbitraryLogError',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
