import FWCore.ParameterSet.Config as cms

simMuonGEMPadDigiClustersDef = cms.EDProducer('GEMPadDigiClusterProducer',
  InputCollection = cms.InputTag('simMuonGEMPadDigis'),
  maxClustersOHGE11 = cms.uint32(4),
  maxClustersOHGE21 = cms.uint32(5),
  nOHGE11 = cms.uint32(2),
  nOHGE21 = cms.uint32(4),
  maxClusterSize = cms.uint32(8),
  mightGet = cms.optional.untracked.vstring
)
