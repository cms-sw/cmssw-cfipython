import FWCore.ParameterSet.Config as cms

def trklet_ProducerTBout(**kwargs):
  mod = cms.EDProducer('trklet::ProducerTBout',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
