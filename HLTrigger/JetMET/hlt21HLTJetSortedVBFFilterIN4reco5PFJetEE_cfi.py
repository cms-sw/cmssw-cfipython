import FWCore.ParameterSet.Config as cms

hlt21HLTJetSortedVBFFilterIN4reco5PFJetEE = cms.EDFilter('HLTPFJetSortedVBFFilter',
  saveTags = cms.bool(False),
  inputJets = cms.InputTag('hltJetCollection'),
  inputJetTags = cms.InputTag(''),
  Mqq = cms.double(200),
  Detaqq = cms.double(2.5),
  Detabb = cms.double(10),
  Ptsumqq = cms.double(0),
  Ptsumbb = cms.double(0),
  Etaq1Etaq2 = cms.double(40),
  value = cms.string('second'),
  triggerType = cms.int32(85)
)
