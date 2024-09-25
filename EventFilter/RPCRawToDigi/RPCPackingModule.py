import FWCore.ParameterSet.Config as cms

def RPCPackingModule(*args, **kwargs):
  mod = cms.EDProducer('RPCPackingModule',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
