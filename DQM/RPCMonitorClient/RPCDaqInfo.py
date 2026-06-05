import FWCore.ParameterSet.Config as cms

def RPCDaqInfo(*args, **kwargs):
  mod = cms.EDProducer('RPCDaqInfo',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
