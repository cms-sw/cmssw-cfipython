import FWCore.ParameterSet.Config as cms

simMuonGEMPadDigiClustersDef = cms.EDProducer('GEMPadDigiClusterProducer',
  InputCollection = cms.InputTag('simMuonGEMPadDigis'),
  maxClusters = cms.uint32(8),
  maxClusterSize = cms.uint32(8),
  mightGet = cms.optional.untracked.vstring
)
