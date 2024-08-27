import FWCore.ParameterSet.Config as cms

def RPCDqmClient(**kwargs):
  mod = cms.EDProducer('RPCDqmClient',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
