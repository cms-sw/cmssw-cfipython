import FWCore.ParameterSet.Config as cms

def RandomIntProducer(**kwargs):
  mod = cms.EDProducer('RandomIntProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
