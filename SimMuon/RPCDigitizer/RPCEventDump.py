import FWCore.ParameterSet.Config as cms

def RPCEventDump(*args, **kwargs):
  mod = cms.EDProducer('RPCEventDump',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
