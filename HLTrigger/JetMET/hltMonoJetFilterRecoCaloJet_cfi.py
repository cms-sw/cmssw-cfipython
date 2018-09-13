import FWCore.ParameterSet.Config as cms

hltMonoJetFilterRecoCaloJet = cms.EDFilter('HLTMonoCaloJetFilter',
  saveTags = cms.bool(False),
  inputJetTag = cms.InputTag('hltAntiKT5ConvPFJets'),
  maxPtSecondJet = cms.double(9999),
  maxDeltaPhi = cms.double(99),
  triggerType = cms.int32(85)
)
