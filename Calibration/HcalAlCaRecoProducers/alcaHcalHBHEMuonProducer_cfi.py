import FWCore.ParameterSet.Config as cms

alcaHcalHBHEMuonProducer = cms.EDProducer('AlCaHcalHBHEMuonProducer',
  triggers = cms.vstring(
    'HLT_IsoMu',
    'HLT_Mu'
  ),
  processName = cms.string('HLT'),
  triggerResults = cms.InputTag('TriggerResults', '', 'HLT'),
  labelEBRecHit = cms.InputTag('ecalRecHit', 'EcalRecHitsEB'),
  labelEERecHit = cms.InputTag('ecalRecHit', 'EcalRecHitsEE'),
  labelHBHERecHit = cms.InputTag('hbhereco'),
  labelVertex = cms.string('offlinePrimaryVertices'),
  labelMuon = cms.string('muons'),
  labelHBHEMuon = cms.string('hbheMuon'),
  collapseDepth = cms.bool(False),
  isItPlan1 = cms.bool(False),
  verbosity = cms.untracked.int32(0),
  isItPreRecHit = cms.untracked.bool(False),
  writeRespCorr = cms.untracked.bool(False),
  fileInCorr = cms.untracked.string(''),
  maxDepth = cms.untracked.int32(4),
  mightGet = cms.optional.untracked.vstring
)
