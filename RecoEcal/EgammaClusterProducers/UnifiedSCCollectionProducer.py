import FWCore.ParameterSet.Config as cms

def UnifiedSCCollectionProducer(*args, **kwargs):
  mod = cms.EDProducer('UnifiedSCCollectionProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
