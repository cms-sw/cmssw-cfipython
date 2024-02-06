import FWCore.ParameterSet.Config as cms

simTracksterHitLCAssociatorByEnergyScore = cms.EDProducer('TSToSimTSHitLCAssociatorByEnergyScoreProducer',
  hitMapTag = cms.InputTag('hgcalRecHitMapProducer'),
  hardScatterOnly = cms.bool(True),
  mightGet = cms.optional.untracked.vstring
)
