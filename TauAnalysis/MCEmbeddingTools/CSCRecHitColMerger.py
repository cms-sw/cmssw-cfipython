import FWCore.ParameterSet.Config as cms

def CSCRecHitColMerger(**kwargs):
  mod = cms.EDProducer('CSCRecHitColMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
