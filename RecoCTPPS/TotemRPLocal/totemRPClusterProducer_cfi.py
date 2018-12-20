import FWCore.ParameterSet.Config as cms

totemRPClusterProducer = cms.EDProducer('TotemRPClusterProducer',
  tagDigi = cms.InputTag('totemRPRawToDigi', 'TrackingStrip'),
  verbosity = cms.int32(0)
)
