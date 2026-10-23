import FWCore.ParameterSet.Config as cms

def RPCMonitorDigi(*args, **kwargs):
  mod = cms.EDProducer('RPCMonitorDigi',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
