import FWCore.ParameterSet.Config as cms

def L1GtTriggerMenuLiteProducer(**kwargs):
  mod = cms.EDProducer('L1GtTriggerMenuLiteProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
