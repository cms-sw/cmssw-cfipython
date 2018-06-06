import FWCore.ParameterSet.Config as cms

hltForwardBackwardJetsFilterRecoPFJet = cms.EDFilter('HLTForwardBackwardPFJetsFilter',
  saveTags = cms.bool(True),
  inputTag = cms.InputTag('hltIterativeCone5CaloJetsRegional'),
  minPt = cms.double(15),
  minEta = cms.double(3),
  maxEta = cms.double(5.1),
  nNeg = cms.uint32(1),
  nPos = cms.uint32(1),
  nTot = cms.uint32(0),
  triggerType = cms.int32(85)
)
