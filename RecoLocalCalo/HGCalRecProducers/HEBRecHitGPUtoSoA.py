import FWCore.ParameterSet.Config as cms

def HEBRecHitGPUtoSoA(**kwargs):
  mod = cms.EDProducer('HEBRecHitGPUtoSoA',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
