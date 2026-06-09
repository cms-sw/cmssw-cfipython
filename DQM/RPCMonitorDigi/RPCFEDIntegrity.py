import FWCore.ParameterSet.Config as cms

def RPCFEDIntegrity(*args, **kwargs):
  mod = cms.EDProducer('RPCFEDIntegrity',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
