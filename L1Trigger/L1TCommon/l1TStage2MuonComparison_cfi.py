import FWCore.ParameterSet.Config as cms

l1TStage2MuonComparison = cms.EDProducer('L1TStage2MuonComparison',
  collection1 = cms.InputTag('collection1'),
  collection2 = cms.InputTag('collection2'),
  checkBxRange = cms.bool(True),
  checkCollSizePerBx = cms.bool(True),
  checkObject = cms.bool(True),
  mightGet = cms.optional.untracked.vstring
)
