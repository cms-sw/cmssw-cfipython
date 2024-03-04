import FWCore.ParameterSet.Config as cms

def RPCMonitorLinkSynchro(**kwargs):
  mod = cms.EDProducer('RPCMonitorLinkSynchro',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
