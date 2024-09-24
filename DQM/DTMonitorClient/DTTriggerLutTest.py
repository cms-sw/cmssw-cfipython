import FWCore.ParameterSet.Config as cms

def DTTriggerLutTest(*args, **kwargs):
  mod = cms.EDProducer('DTTriggerLutTest',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
