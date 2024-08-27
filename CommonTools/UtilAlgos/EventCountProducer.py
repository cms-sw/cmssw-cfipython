import FWCore.ParameterSet.Config as cms

def EventCountProducer(**kwargs):
  mod = cms.EDProducer('EventCountProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
