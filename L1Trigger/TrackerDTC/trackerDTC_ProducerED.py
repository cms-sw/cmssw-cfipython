import FWCore.ParameterSet.Config as cms

def trackerDTC_ProducerED(**kwargs):
  mod = cms.EDProducer('trackerDTC::ProducerED',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
