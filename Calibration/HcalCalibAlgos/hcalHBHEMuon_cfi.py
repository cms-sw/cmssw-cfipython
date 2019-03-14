import FWCore.ParameterSet.Config as cms

hcalHBHEMuon = cms.EDAnalyzer('HcalHBHEMuonAnalyzer',
  HLTriggerResults = cms.InputTag('TriggerResults', '', 'HLT'),
  LabelBeamSpot = cms.string('offlineBeamSpot'),
  LabelVertex = cms.string('offlinePrimaryVertices'),
  LabelEBRecHit = cms.InputTag('ecalRecHit', 'EcalRecHitsEB'),
  LabelEERecHit = cms.InputTag('ecalRecHit', 'EcalRecHitsEE'),
  LabelHBHERecHit = cms.InputTag('hbhereco'),
  LabelMuon = cms.string('muons'),
  Triggers = cms.vstring(
    'HLT_IsoMu17',
    'HLT_IsoMu20',
    'HLT_IsoMu24',
    'HLT_IsoMu27',
    'HLT_Mu45',
    'HLT_Mu50'
  ),
  UseRaw = cms.bool(False),
  UnCorrect = cms.bool(False),
  GetCharge = cms.bool(False),
  CollapseDepth = cms.bool(False),
  IsItPlan1 = cms.bool(False),
  IgnoreHECorr = cms.untracked.bool(False),
  IsItPreRecHit = cms.untracked.bool(False),
  ModuleName = cms.untracked.string(''),
  ProcessName = cms.untracked.string(''),
  Verbosity = cms.untracked.int32(0),
  MaxDepth = cms.untracked.int32(4),
  FileInCorr = cms.untracked.string(''),
  WriteRespCorr = cms.untracked.bool(False)
)
