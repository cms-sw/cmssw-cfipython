import FWCore.ParameterSet.Config as cms

def RPCNeutronWriter(**kwargs):
  mod = cms.EDProducer('RPCNeutronWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
