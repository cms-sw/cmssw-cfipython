import FWCore.ParameterSet.Config as cms

def CSCRecHitColCleaner(**kwargs):
  mod = cms.EDProducer('CSCRecHitColCleaner',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
