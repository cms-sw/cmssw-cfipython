import FWCore.ParameterSet.Config as cms

def DTLocalTriggerLutTask(*args, **kwargs):
  mod = cms.EDProducer('DTLocalTriggerLutTask',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
