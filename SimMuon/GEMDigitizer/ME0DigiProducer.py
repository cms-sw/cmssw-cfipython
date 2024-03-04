import FWCore.ParameterSet.Config as cms

def ME0DigiProducer(**kwargs):
  mod = cms.EDProducer('ME0DigiProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
