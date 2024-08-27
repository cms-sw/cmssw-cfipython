import FWCore.ParameterSet.Config as cms

def trackerTFP_ProducerHT(**kwargs):
  mod = cms.EDProducer('trackerTFP::ProducerHT',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
