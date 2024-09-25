import FWCore.ParameterSet.Config as cms

def trackerTFP_ProducerZHTout(*args, **kwargs):
  mod = cms.EDProducer('trackerTFP::ProducerZHTout',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
