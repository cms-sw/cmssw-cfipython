import FWCore.ParameterSet.Config as cms

def PreshowerPhiClusterProducer(*args, **kwargs):
  mod = cms.EDProducer('PreshowerPhiClusterProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
