import FWCore.ParameterSet.Config as cms

def PATTriggerObjectStandAloneUnpacker(*args, **kwargs):
  mod = cms.EDProducer('PATTriggerObjectStandAloneUnpacker',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
