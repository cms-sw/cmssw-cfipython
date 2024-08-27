import FWCore.ParameterSet.Config as cms

def trackerTFP_ProducerGP(**kwargs):
  mod = cms.EDProducer('trackerTFP::ProducerGP',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
