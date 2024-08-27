import FWCore.ParameterSet.Config as cms

def RPCPackingModule(**kwargs):
  mod = cms.EDProducer('RPCPackingModule',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
