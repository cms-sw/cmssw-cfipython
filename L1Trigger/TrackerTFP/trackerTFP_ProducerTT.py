import FWCore.ParameterSet.Config as cms

def trackerTFP_ProducerTT(*args, **kwargs):
  mod = cms.EDProducer('trackerTFP::ProducerTT',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
