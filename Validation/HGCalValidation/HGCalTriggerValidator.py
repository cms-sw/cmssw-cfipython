import FWCore.ParameterSet.Config as cms

def HGCalTriggerValidator(**kwargs):
  mod = cms.EDProducer('HGCalTriggerValidator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
