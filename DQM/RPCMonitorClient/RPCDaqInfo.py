import FWCore.ParameterSet.Config as cms

def RPCDaqInfo(**kwargs):
  mod = cms.EDProducer('RPCDaqInfo',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
