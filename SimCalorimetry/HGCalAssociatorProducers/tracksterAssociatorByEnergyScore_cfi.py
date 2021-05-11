import FWCore.ParameterSet.Config as cms

tracksterAssociatorByEnergyScore = cms.EDProducer('TSToSCAssociatorByEnergyScoreProducer',
  hitMapTag = cms.InputTag('hgcalRecHitMapProducer'),
  hardScatterOnly = cms.bool(True),
  mightGet = cms.optional.untracked.vstring
)
