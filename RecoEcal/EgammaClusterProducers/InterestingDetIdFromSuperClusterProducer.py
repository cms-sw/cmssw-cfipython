import FWCore.ParameterSet.Config as cms

def InterestingDetIdFromSuperClusterProducer(**kwargs):
  mod = cms.EDProducer('InterestingDetIdFromSuperClusterProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
