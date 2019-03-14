import FWCore.ParameterSet.Config as cms

ctppsPixelRecHits = cms.EDProducer('CTPPSPixelRecHitProducer',
  RPixVerbosity = cms.untracked.int32(0),
  RPixClusterTag = cms.InputTag('ctppsPixelClusters')
)
