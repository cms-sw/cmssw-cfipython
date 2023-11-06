import FWCore.ParameterSet.Config as cms

simClusterAssociatorByEnergyScore = cms.EDProducer('LCToSCAssociatorByEnergyScoreProducer',
  hitMapTag = cms.InputTag('hgcalRecHitMapProducer'),
  hardScatterOnly = cms.bool(True),
  mightGet = cms.optional.untracked.vstring
)
