import FWCore.ParameterSet.Config as cms

hltJetHbbFilterRecoPFJet = cms.EDFilter('HLTPFJetHbbFilter',
  saveTags = cms.bool(True),
  inputJets = cms.InputTag('hltJetCollection'),
  inputJetTags = cms.InputTag(''),
  minMbb = cms.double(70),
  maxMbb = cms.double(200),
  minPtb1 = cms.double(-1),
  minPtb2 = cms.double(-1),
  maxEtab = cms.double(99999),
  minPtbb = cms.double(-1),
  maxPtbb = cms.double(-1),
  minTag1 = cms.double(0.5),
  minTag2 = cms.double(0.2),
  maxTag = cms.double(99999),
  triggerType = cms.int32(85)
)
