import FWCore.ParameterSet.Config as cms

def HEBRecHitFromSoA(**kwargs):
  mod = cms.EDProducer('HEBRecHitFromSoA',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
