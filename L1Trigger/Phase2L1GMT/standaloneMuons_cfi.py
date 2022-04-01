import FWCore.ParameterSet.Config as cms

standaloneMuons = cms.EDProducer('Phase2L1TGMTSAMuonProducer',
  muonToken = cms.InputTag('simGmtStage2Digis'),
  Nprompt = cms.uint32(12),
  Ndisplaced = cms.uint32(12),
  mightGet = cms.optional.untracked.vstring
)
