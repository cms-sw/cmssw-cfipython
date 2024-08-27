import FWCore.ParameterSet.Config as cms

def trklet_ProducerKFout(**kwargs):
  mod = cms.EDProducer('trklet::ProducerKFout',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
