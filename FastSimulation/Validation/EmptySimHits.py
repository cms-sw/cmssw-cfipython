import FWCore.ParameterSet.Config as cms

def EmptySimHits(**kwargs):
  mod = cms.EDProducer('EmptySimHits',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
