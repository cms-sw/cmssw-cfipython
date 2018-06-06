import FWCore.ParameterSet.Config as cms

hltJetSortedVBFFilterRecoCaloJet = cms.EDFilter('HLTCaloJetSortedVBFFilter',
  saveTags = cms.bool(True),
  inputJets = cms.InputTag('hltJetCollection'),
  inputJetTags = cms.InputTag(''),
  Mqq = cms.double(200),
  Detaqq = cms.double(2.5),
  Detabb = cms.double(10),
  Dphibb = cms.double(10),
  Ptsumqq = cms.double(0),
  Ptsumbb = cms.double(0),
  Etaq1Etaq2 = cms.double(40),
  value = cms.string('second'),
  triggerType = cms.int32(85),
  njets = cms.int32(4)
)
