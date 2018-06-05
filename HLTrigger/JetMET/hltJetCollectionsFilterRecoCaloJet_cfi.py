import FWCore.ParameterSet.Config as cms

hltJetCollectionsFilterRecoCaloJet = cms.EDFilter('HLTCaloJetCollectionsFilter',
  saveTags = cms.bool(True),
  inputTag = cms.InputTag('hltIterativeCone5CaloJets'),
  originalTag = cms.InputTag('hltIterativeCone5CaloJets'),
  MinJetPt = cms.double(30),
  MaxAbsJetEta = cms.double(2.6),
  MinNJets = cms.uint32(1),
  triggerType = cms.int32(85)
)
