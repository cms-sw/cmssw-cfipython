import FWCore.ParameterSet.Config as cms

def RandomEngineStateProducer(**kwargs):
  mod = cms.EDProducer('RandomEngineStateProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
