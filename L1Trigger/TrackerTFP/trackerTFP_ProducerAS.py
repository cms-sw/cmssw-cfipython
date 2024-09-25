import FWCore.ParameterSet.Config as cms

def trackerTFP_ProducerAS(*args, **kwargs):
  mod = cms.EDProducer('trackerTFP::ProducerAS',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
