import FWCore.ParameterSet.Config as cms

def RPCNeutronWriter(*args, **kwargs):
  mod = cms.EDProducer('RPCNeutronWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
