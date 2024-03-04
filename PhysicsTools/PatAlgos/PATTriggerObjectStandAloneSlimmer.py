import FWCore.ParameterSet.Config as cms

def PATTriggerObjectStandAloneSlimmer(**kwargs):
  mod = cms.EDProducer('PATTriggerObjectStandAloneSlimmer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
