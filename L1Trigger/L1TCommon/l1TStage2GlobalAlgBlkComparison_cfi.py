import FWCore.ParameterSet.Config as cms

l1TStage2GlobalAlgBlkComparison = cms.EDProducer('L1TStage2GlobalAlgBlkComparison',
  collection1 = cms.InputTag('collection1'),
  collection2 = cms.InputTag('collection2'),
  checkBxRange = cms.bool(True),
  checkCollSizePerBx = cms.bool(True),
  checkObject = cms.bool(True)
)
