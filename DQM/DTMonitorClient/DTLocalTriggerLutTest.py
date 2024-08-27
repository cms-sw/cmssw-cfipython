import FWCore.ParameterSet.Config as cms

def DTLocalTriggerLutTest(**kwargs):
  mod = cms.EDProducer('DTLocalTriggerLutTest',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
