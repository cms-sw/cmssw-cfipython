import FWCore.ParameterSet.Config as cms

def RPCDcsInfoClient(**kwargs):
  mod = cms.EDProducer('RPCDcsInfoClient',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
