import FWCore.ParameterSet.Config as cms

def RPCNoise(*args, **kwargs):
  mod = cms.EDFilter('RPCNoise',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
