import FWCore.ParameterSet.Config as cms

def FlavorHistoryProducer(**kwargs):
  mod = cms.EDProducer('FlavorHistoryProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
