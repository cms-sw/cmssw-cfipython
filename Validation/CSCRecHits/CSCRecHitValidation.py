import FWCore.ParameterSet.Config as cms

def CSCRecHitValidation(**kwargs):
  mod = cms.EDProducer('CSCRecHitValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
