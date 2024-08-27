import FWCore.ParameterSet.Config as cms

def DTLocalTriggerTPTest(**kwargs):
  mod = cms.EDProducer('DTLocalTriggerTPTest',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
