import FWCore.ParameterSet.Config as cms

def RPCDigiValid(**kwargs):
  mod = cms.EDProducer('RPCDigiValid',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
