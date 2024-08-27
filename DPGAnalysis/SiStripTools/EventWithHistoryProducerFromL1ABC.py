import FWCore.ParameterSet.Config as cms

def EventWithHistoryProducerFromL1ABC(**kwargs):
  mod = cms.EDProducer('EventWithHistoryProducerFromL1ABC',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
