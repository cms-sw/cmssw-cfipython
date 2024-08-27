import FWCore.ParameterSet.Config as cms

def trackerTFP_ProducerMHT(**kwargs):
  mod = cms.EDProducer('trackerTFP::ProducerMHT',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
