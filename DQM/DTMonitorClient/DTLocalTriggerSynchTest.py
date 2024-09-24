import FWCore.ParameterSet.Config as cms

def DTLocalTriggerSynchTest(*args, **kwargs):
  mod = cms.EDProducer('DTLocalTriggerSynchTest',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
