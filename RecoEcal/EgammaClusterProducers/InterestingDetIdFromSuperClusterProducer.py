import FWCore.ParameterSet.Config as cms

def InterestingDetIdFromSuperClusterProducer(*args, **kwargs):
  mod = cms.EDProducer('InterestingDetIdFromSuperClusterProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
