import FWCore.ParameterSet.Config as cms

def RPCEMapDBWriter(**kwargs):
  mod = cms.EDAnalyzer('RPCEMapDBWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
