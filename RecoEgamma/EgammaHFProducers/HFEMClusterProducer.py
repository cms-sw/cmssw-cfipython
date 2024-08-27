import FWCore.ParameterSet.Config as cms

def HFEMClusterProducer(**kwargs):
  mod = cms.EDProducer('HFEMClusterProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
