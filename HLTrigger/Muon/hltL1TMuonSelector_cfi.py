import FWCore.ParameterSet.Config as cms

hltL1TMuonSelector = cms.EDProducer('HLTL1TMuonSelector',
  InputObjects = cms.InputTag('hltGmtStage2Digis'),
  L1MinPt = cms.double(-1),
  L1MaxEta = cms.double(5),
  L1MinQuality = cms.uint32(0),
  CentralBxOnly = cms.bool(True)
)
