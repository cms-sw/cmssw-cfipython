import FWCore.ParameterSet.Config as cms

def trklet_ProducerKFin(**kwargs):
  mod = cms.EDProducer('trklet::ProducerKFin',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
