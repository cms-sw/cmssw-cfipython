import FWCore.ParameterSet.Config as cms

hltMonoJetFilterRecoPFJet = cms.EDFilter('HLTMonoPFJetFilter',
  saveTags = cms.bool(False),
  inputJetTag = cms.InputTag('hltAntiKT5ConvPFJets'),
  maxPtSecondJet = cms.double(9999),
  maxDeltaPhi = cms.double(99),
  triggerType = cms.int32(85)
)
