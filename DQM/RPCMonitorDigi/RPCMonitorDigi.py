import FWCore.ParameterSet.Config as cms

def RPCMonitorDigi(**kwargs):
  mod = cms.EDProducer('RPCMonitorDigi',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
