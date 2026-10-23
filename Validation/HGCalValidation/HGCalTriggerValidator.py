import FWCore.ParameterSet.Config as cms

def HGCalTriggerValidator(*args, **kwargs):
  mod = cms.EDProducer('HGCalTriggerValidator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
