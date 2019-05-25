import FWCore.ParameterSet.Config as cms

hltL1MuonSelector = cms.EDProducer('HLTL1MuonSelector',
  InputObjects = cms.InputTag(''),
  L1MinPt = cms.double(-1),
  L1MaxEta = cms.double(5),
  L1MinQuality = cms.uint32(0)
)
