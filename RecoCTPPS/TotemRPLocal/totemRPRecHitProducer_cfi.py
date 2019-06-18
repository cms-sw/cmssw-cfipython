import FWCore.ParameterSet.Config as cms

totemRPRecHitProducer = cms.EDProducer('TotemRPRecHitProducer',
  tagCluster = cms.InputTag('totemRPClusterProducer'),
  verbosity = cms.int32(0),
  mightGet = cms.optional.untracked.vstring
)
