import FWCore.ParameterSet.Config as cms

mtdSimLayerClusterToTPAssociatorByTrackId = cms.EDProducer('MtdSimLayerClusterToTPAssociatorByTrackIdProducer',
  mightGet = cms.optional.untracked.vstring
)
