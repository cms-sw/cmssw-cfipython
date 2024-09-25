import FWCore.ParameterSet.Config as cms

def trackerTFP_ProducerGP(*args, **kwargs):
  mod = cms.EDProducer('trackerTFP::ProducerGP',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
