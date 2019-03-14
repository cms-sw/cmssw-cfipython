import FWCore.ParameterSet.Config as cms

totemRPLocalTrackFitter = cms.EDProducer('TotemRPLocalTrackFitter',
  tagUVPattern = cms.InputTag('totemRPUVPatternFinder'),
  verbosity = cms.int32(0)
)
