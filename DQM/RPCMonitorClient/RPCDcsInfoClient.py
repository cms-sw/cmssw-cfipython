import FWCore.ParameterSet.Config as cms

def RPCDcsInfoClient(*args, **kwargs):
  mod = cms.EDProducer('RPCDcsInfoClient',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
