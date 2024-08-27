import FWCore.ParameterSet.Config as cms

def MTDRecHitProducer(**kwargs):
  mod = cms.EDProducer('MTDRecHitProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
