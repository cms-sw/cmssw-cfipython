import FWCore.ParameterSet.Config as cms

def PATTriggerObjectStandAloneUnpacker(**kwargs):
  mod = cms.EDProducer('PATTriggerObjectStandAloneUnpacker',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
