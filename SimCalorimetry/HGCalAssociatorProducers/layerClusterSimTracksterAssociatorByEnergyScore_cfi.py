import FWCore.ParameterSet.Config as cms

layerClusterSimTracksterAssociatorByEnergyScore = cms.EDProducer('LCToSimTSAssociatorByEnergyScoreProducer',
  mightGet = cms.optional.untracked.vstring
)
