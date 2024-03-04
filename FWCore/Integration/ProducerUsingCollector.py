import FWCore.ParameterSet.Config as cms

def ProducerUsingCollector(**kwargs):
  mod = cms.EDProducer('ProducerUsingCollector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
