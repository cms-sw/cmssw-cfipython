import FWCore.ParameterSet.Config as cms

def trklet_ProducerTT(**kwargs):
  mod = cms.EDProducer('trklet::ProducerTT',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
