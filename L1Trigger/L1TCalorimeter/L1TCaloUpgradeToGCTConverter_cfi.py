import FWCore.ParameterSet.Config as cms

L1TCaloUpgradeToGCTConverter = cms.EDProducer('L1TCaloUpgradeToGCTConverter',
  bxMin = cms.int32(0),
  bxMax = cms.int32(0),
  InputCollection = cms.InputTag('caloStage1Digis'),
  InputRlxTauCollection = cms.InputTag('caloStage1Digis', 'rlxTaus'),
  InputIsoTauCollection = cms.InputTag('caloStage1Digis', 'isoTaus'),
  InputHFSumsCollection = cms.InputTag('caloStage1Digis', 'HFRingSums'),
  InputHFCountsCollection = cms.InputTag('caloStage1Digis', 'HFBitCounts')
)
