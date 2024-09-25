import FWCore.ParameterSet.Config as cms

def RPCEMapDBWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('RPCEMapDBWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
