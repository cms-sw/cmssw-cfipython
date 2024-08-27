import FWCore.ParameterSet.Config as cms

def trackerTFP_ProducerKFin(**kwargs):
  mod = cms.EDProducer('trackerTFP::ProducerKFin',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
