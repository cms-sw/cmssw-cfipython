import FWCore.ParameterSet.Config as cms

def GoodSeedProducer(**kwargs):
  mod = cms.EDProducer('GoodSeedProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
