import FWCore.ParameterSet.Config as cms

def PATTriggerObjectStandAloneSlimmer(*args, **kwargs):
  mod = cms.EDProducer('PATTriggerObjectStandAloneSlimmer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
