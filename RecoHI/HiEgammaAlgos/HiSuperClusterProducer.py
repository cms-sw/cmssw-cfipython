import FWCore.ParameterSet.Config as cms

def HiSuperClusterProducer(**kwargs):
  mod = cms.EDProducer('HiSuperClusterProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
