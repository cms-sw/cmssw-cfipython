import FWCore.ParameterSet.Config as cms

def InterestingDetIdCollectionProducer(*args, **kwargs):
  mod = cms.EDProducer('InterestingDetIdCollectionProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
