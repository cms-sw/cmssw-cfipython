import FWCore.ParameterSet.Config as cms

multiClusterAssociatorByEnergyScore = cms.EDProducer('MultiClusterAssociatorByEnergyScoreProducer',
  hitMapTag = cms.InputTag('hgcalRecHitMapProducer'),
  hardScatterOnly = cms.bool(True),
  mightGet = cms.optional.untracked.vstring
)
