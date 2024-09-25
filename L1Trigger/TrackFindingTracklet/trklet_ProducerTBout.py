import FWCore.ParameterSet.Config as cms

def trklet_ProducerTBout(*args, **kwargs):
  mod = cms.EDProducer('trklet::ProducerTBout',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
