import FWCore.ParameterSet.Config as cms

def RPCEventSummary(**kwargs):
  mod = cms.EDProducer('RPCEventSummary',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
