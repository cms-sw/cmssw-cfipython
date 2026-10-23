import FWCore.ParameterSet.Config as cms

def SimClusterToCaloParticleAssociatorProducer(*args, **kwargs):
  mod = cms.EDProducer('SimClusterToCaloParticleAssociatorProducer',
    simClusters = cms.InputTag('mix', 'MergedCaloTruth'),
    caloParticles = cms.InputTag('mix', 'MergedCaloTruth'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
