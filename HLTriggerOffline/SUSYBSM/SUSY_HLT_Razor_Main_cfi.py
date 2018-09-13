import FWCore.ParameterSet.Config as cms

SUSY_HLT_Razor_Main = cms.EDAnalyzer('SUSY_HLT_Razor',
  jetCollection = cms.InputTag('ak4PFJetsCHS'),
  CaloFilter = cms.InputTag('hltRsqMR200Rsq0p01MR100Calo', '', 'HLT'),
  METCollection = cms.InputTag('pfMet'),
  hemispheres = cms.InputTag('hemispheres'),
  TriggerPath = cms.string('HLT_RsqMR300_Rsq0p09_MR200_v'),
  DenomPath = cms.string('HLT_Ele40_eta2p1_WP85_Gsf_v'),
  DenomPathLoose = cms.string('HLT_Ele35_eta2p1_WP85_Gsf_v'),
  TriggerFilter = cms.InputTag('hltRsqMR300Rsq0p09MR200', '', 'HLT'),
  TriggerResults = cms.InputTag('TriggerResults', '', 'HLT'),
  trigSummary = cms.InputTag('hltTriggerSummaryAOD')
)
