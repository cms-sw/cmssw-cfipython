import FWCore.ParameterSet.Config as cms

hltL1TSeed = cms.EDFilter('HLTL1TSeed',
  saveTags = cms.bool(True),
  L1SeedsLogicalExpression = cms.string(''),
  L1ObjectMapInputTag = cms.InputTag('hltGtStage2ObjectMap'),
  L1GlobalInputTag = cms.InputTag('hltGtStage2Digis'),
  L1MuonInputTag = cms.InputTag('hltGtStage2Digis', 'Muon'),
  L1MuonShowerInputTag = cms.InputTag('hltGtStage2Digis', 'MuonShower'),
  L1EGammaInputTag = cms.InputTag('hltGtStage2Digis', 'EGamma'),
  L1JetInputTag = cms.InputTag('hltGtStage2Digis', 'Jet'),
  L1TauInputTag = cms.InputTag('hltGtStage2Digis', 'Tau'),
  L1EtSumInputTag = cms.InputTag('hltGtStage2Digis', 'EtSum'),
  mightGet = cms.optional.untracked.vstring
)
