import FWCore.ParameterSet.Config as cms

def CSCRecHitValidation(*args, **kwargs):
  mod = cms.EDProducer('CSCRecHitValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
