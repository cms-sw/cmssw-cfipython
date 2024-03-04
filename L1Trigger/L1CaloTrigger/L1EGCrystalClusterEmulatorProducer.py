import FWCore.ParameterSet.Config as cms

def L1EGCrystalClusterEmulatorProducer(**kwargs):
  mod = cms.EDProducer('L1EGCrystalClusterEmulatorProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
