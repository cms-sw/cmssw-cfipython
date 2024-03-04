import FWCore.ParameterSet.Config as cms

def UnifiedSCCollectionProducer(**kwargs):
  mod = cms.EDProducer('UnifiedSCCollectionProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
