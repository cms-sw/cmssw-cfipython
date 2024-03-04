import FWCore.ParameterSet.Config as cms

def ME0RecHitProducer(**kwargs):
  mod = cms.EDProducer('ME0RecHitProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
