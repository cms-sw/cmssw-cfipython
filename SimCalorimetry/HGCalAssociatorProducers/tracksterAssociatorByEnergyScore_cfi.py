import FWCore.ParameterSet.Config as cms

tracksterAssociatorByEnergyScore = cms.EDProducer('TracksterAssociatorByEnergyScoreProducer',
  hitMapTag = cms.InputTag('hgcalRecHitMapProducer'),
  hardScatterOnly = cms.bool(True),
  mightGet = cms.optional.untracked.vstring
)
