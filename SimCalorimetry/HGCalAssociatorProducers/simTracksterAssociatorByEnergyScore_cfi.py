import FWCore.ParameterSet.Config as cms

simTracksterAssociatorByEnergyScore = cms.EDProducer('TSToSimTSAssociatorByEnergyScoreProducer',
  hitMapTag = cms.InputTag('hgcalRecHitMapProducer'),
  hardScatterOnly = cms.bool(True),
  mightGet = cms.optional.untracked.vstring
)
