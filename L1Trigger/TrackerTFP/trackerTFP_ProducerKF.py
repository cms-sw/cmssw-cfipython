import FWCore.ParameterSet.Config as cms

def trackerTFP_ProducerKF(**kwargs):
  mod = cms.EDProducer('trackerTFP::ProducerKF',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
