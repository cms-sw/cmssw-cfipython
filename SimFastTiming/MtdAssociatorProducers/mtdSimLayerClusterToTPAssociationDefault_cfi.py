import FWCore.ParameterSet.Config as cms

mtdSimLayerClusterToTPAssociationDefault = cms.EDProducer('MtdSimLayerClusterToTPAssociatorEDProducer',
  associator = cms.InputTag('mtdSimLayerClusterToTPAssociatorByTrackId'),
  mtdSimClustersTag = cms.InputTag('mix', 'MergedMtdTruthLC'),
  trackingParticlesTag = cms.InputTag('mix', 'MergedTrackTruth'),
  mightGet = cms.optional.untracked.vstring
)
