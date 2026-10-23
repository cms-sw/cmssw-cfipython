import FWCore.ParameterSet.Config as cms

def TotemRPRecHitProducer(*args, **kwargs):
  mod = cms.EDProducer('TotemRPRecHitProducer',
    tagCluster = cms.InputTag('totemRPClusterProducer'),
    verbosity = cms.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
