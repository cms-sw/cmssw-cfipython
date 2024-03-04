import FWCore.ParameterSet.Config as cms

def DTLocalTriggerSynchTask(**kwargs):
  mod = cms.EDProducer('DTLocalTriggerSynchTask',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
