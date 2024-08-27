import FWCore.ParameterSet.Config as cms

def EventWithHistoryProducer(**kwargs):
  mod = cms.EDProducer('EventWithHistoryProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
