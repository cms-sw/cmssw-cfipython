import FWCore.ParameterSet.Config as cms

def MtdSimLayerClusterToTPAssociatorEDProducer(*args, **kwargs):
  mod = cms.EDProducer('MtdSimLayerClusterToTPAssociatorEDProducer',
    associator = cms.InputTag('mtdSimLayerClusterToTPAssociatorByTrackId'),
    mtdSimClustersTag = cms.InputTag('mix', 'MergedMtdTruthLC'),
    trackingParticlesTag = cms.InputTag('mix', 'MergedTrackTruth'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
