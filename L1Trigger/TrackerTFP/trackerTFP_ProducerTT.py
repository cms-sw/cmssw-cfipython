import FWCore.ParameterSet.Config as cms

def trackerTFP_ProducerTT(**kwargs):
  mod = cms.EDProducer('trackerTFP::ProducerTT',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
