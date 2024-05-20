import FWCore.ParameterSet.Config as cms

def MtdSimLayerClusterToTPAssociatorEDProducer(**kwargs):
  mod = cms.EDProducer('MtdSimLayerClusterToTPAssociatorEDProducer',
    associator = cms.InputTag('mtdSimLayerClusterToTPAssociatorByTrackId'),
    mtdSimClustersTag = cms.InputTag('mix', 'MergedMtdTruthLC'),
    trackingParticlesTag = cms.InputTag('mix', 'MergedTrackTruth'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
