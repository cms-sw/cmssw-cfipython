import FWCore.ParameterSet.Config as cms

totemRPLocalTrackFitter = cms.EDProducer('TotemRPLocalTrackFitter',
  tagUVPattern = cms.InputTag('totemRPUVPatternFinder'),
  verbosity = cms.int32(0),
  mightGet = cms.optional.untracked.vstring
)
