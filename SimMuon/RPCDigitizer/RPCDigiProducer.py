import FWCore.ParameterSet.Config as cms

def RPCDigiProducer(*args, **kwargs):
  mod = cms.EDProducer('RPCDigiProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
