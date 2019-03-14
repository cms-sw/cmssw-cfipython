import FWCore.ParameterSet.Config as cms

HotlineDQM = cms.EDAnalyzer('HotlineDQM',
  photonCollection = cms.InputTag('photons'),
  muonCollection = cms.InputTag('muons'),
  caloJetCollection = cms.InputTag('ak4CaloJets'),
  pfMetCollection = cms.InputTag('pfMet'),
  caloMetCollection = cms.InputTag('caloMet'),
  triggerResults = cms.InputTag('TriggerResults', '', 'HLT'),
  trigSummary = cms.InputTag('hltTriggerSummaryAOD'),
  triggerPath = cms.string('HLT_HT2000_v'),
  triggerFilter = cms.InputTag('hltHt2000', '', 'HLT'),
  useMuons = cms.bool(False),
  usePhotons = cms.bool(False),
  useMet = cms.bool(False),
  usePFMet = cms.bool(False),
  useHT = cms.bool(False)
)
