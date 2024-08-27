import FWCore.ParameterSet.Config as cms

def MTDUncalibratedRecHitProducer(**kwargs):
  mod = cms.EDProducer('MTDUncalibratedRecHitProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
