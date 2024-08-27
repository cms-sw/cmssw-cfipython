import FWCore.ParameterSet.Config as cms

def DTLocalTriggerLutTask(**kwargs):
  mod = cms.EDProducer('DTLocalTriggerLutTask',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
