import FWCore.ParameterSet.Config as cms

def RPCTnPEfficiencyTask(*args, **kwargs):
  mod = cms.EDProducer('RPCTnPEfficiencyTask',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
