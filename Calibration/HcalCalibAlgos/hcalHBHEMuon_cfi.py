import FWCore.ParameterSet.Config as cms

hcalHBHEMuon = cms.EDAnalyzer('HcalHBHEMuonAnalyzer',
  hlTriggerResults = cms.InputTag('TriggerResults', '', 'HLT'),
  labelEBRecHit = cms.InputTag('ecalRecHit', 'EcalRecHitsEB'),
  labelEERecHit = cms.InputTag('ecalRecHit', 'EcalRecHitsEE'),
  labelHBHERecHit = cms.InputTag('hbhereco'),
  labelVertex = cms.string('offlinePrimaryVertices'),
  labelMuon = cms.string('muons'),
  triggers = cms.vstring(
    'HLT_IsoMu17',
    'HLT_IsoMu20',
    'HLT_IsoMu24',
    'HLT_IsoMu27',
    'HLT_Mu45',
    'HLT_Mu50'
  ),
  verbosity = cms.untracked.int32(0),
  useRaw = cms.int32(0),
  unCorrect = cms.bool(False),
  getCharge = cms.bool(False),
  collapseDepth = cms.bool(False),
  isItPlan1 = cms.bool(False),
  ignoreHECorr = cms.untracked.bool(False),
  isItPreRecHit = cms.untracked.bool(False),
  moduleName = cms.untracked.string(''),
  processName = cms.untracked.string(''),
  maxDepth = cms.untracked.int32(4),
  fileInCorr = cms.untracked.string(''),
  writeRespCorr = cms.untracked.bool(False),
  mightGet = cms.optional.untracked.vstring
)
