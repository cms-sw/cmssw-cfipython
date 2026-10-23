import FWCore.ParameterSet.Config as cms

def trackerTFP_ProducerPP(*args, **kwargs):
  mod = cms.EDProducer('trackerTFP::ProducerPP',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
