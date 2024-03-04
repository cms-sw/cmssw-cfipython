import FWCore.ParameterSet.Config as cms

def trklet_ProducerDRin(**kwargs):
  mod = cms.EDProducer('trklet::ProducerDRin',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
