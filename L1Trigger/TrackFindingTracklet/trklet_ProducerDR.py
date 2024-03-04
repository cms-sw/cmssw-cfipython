import FWCore.ParameterSet.Config as cms

def trklet_ProducerDR(**kwargs):
  mod = cms.EDProducer('trklet::ProducerDR',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
