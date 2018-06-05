import FWCore.ParameterSet.Config as cms

hltL1TSeed = cms.EDFilter('HLTL1TSeed',
  saveTags = cms.bool(True),
  L1SeedsLogicalExpression = cms.string(''),
  L1ObjectMapInputTag = cms.InputTag('hltGtStage2ObjectMap'),
  L1GlobalInputTag = cms.InputTag('hltGtStage2Digis'),
  L1MuonInputTag = cms.InputTag('hltGmtStage2Digis', 'Muon'),
  L1EGammaInputTag = cms.InputTag('hltCaloStage2Digis', 'EGamma'),
  L1JetInputTag = cms.InputTag('hltCaloStage2Digis', 'Jet'),
  L1TauInputTag = cms.InputTag('hltCaloStage2Digis', 'Tau'),
  L1EtSumInputTag = cms.InputTag('hltCaloStage2Digis', 'EtSum')
)
