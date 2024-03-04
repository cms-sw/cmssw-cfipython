import FWCore.ParameterSet.Config as cms

def trackerTFP_ProducerZHTout(**kwargs):
  mod = cms.EDProducer('trackerTFP::ProducerZHTout',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
