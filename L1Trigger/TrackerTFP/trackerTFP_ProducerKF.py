import FWCore.ParameterSet.Config as cms

def trackerTFP_ProducerKF(*args, **kwargs):
  mod = cms.EDProducer('trackerTFP::ProducerKF',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
