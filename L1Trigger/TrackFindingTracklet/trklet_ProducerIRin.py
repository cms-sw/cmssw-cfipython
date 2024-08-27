import FWCore.ParameterSet.Config as cms

def trklet_ProducerIRin(**kwargs):
  mod = cms.EDProducer('trklet::ProducerIRin',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
