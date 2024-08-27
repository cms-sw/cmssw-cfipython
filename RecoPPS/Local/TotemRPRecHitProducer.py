import FWCore.ParameterSet.Config as cms

def TotemRPRecHitProducer(**kwargs):
  mod = cms.EDProducer('TotemRPRecHitProducer',
    tagCluster = cms.InputTag('totemRPClusterProducer'),
    verbosity = cms.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
