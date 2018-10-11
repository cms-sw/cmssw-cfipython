import FWCore.ParameterSet.Config as cms

hcalIsoTrackStudy = cms.EDAnalyzer('HcalIsoTrackStudy',
  triggers = cms.vstring(
    'HLT_PFJet40',
    'HLT_PFJet60',
    'HLT_PFJet80',
    'HLT_PFJet140',
    'HLT_PFJet200',
    'HLT_PFJet260',
    'HLT_PFJet320',
    'HLT_PFJet400',
    'HLT_PFJet450',
    'HLT_PFJet500'
  ),
  processName = cms.string('HLT'),
  l1Filter = cms.string(''),
  l2Filter = cms.string('L2Filter'),
  l3Filter = cms.string('Filter'),
  trackQuality = cms.string('highPurity'),
  minTrackPt = cms.double(1),
  maxDxyPV = cms.double(0.02),
  maxDzPV = cms.double(0.02),
  maxChi2 = cms.double(5),
  maxDpOverP = cms.double(0.1),
  minOuterHit = cms.int32(4),
  minLayerCrossed = cms.int32(8),
  maxInMiss = cms.int32(0),
  maxOutMiss = cms.int32(0),
  minimumTrackP = cms.double(20),
  coneRadius = cms.double(34.98),
  coneRadiusMIP = cms.double(14),
  maximumEcalEnergy = cms.double(2),
  maxTrackP = cms.double(8),
  slopeTrackP = cms.double(0.05090504066),
  isolationEnergyTight = cms.double(2),
  isolationEnergyLoose = cms.double(10),
  EBHitEnergyThreshold = cms.double(0.1),
  EEHitEnergyThreshold0 = cms.double(-41.0664),
  EEHitEnergyThreshold1 = cms.double(68.795),
  EEHitEnergyThreshold2 = cms.double(-38.1483),
  EEHitEnergyThreshold3 = cms.double(7.04303),
  momentumLow = cms.double(40),
  momentumHigh = cms.double(60),
  prescaleLow = cms.int32(1),
  prescaleHigh = cms.int32(1),
  labelTriggerEvent = cms.InputTag('hltTriggerSummaryAOD', '', 'HLT'),
  labelTriggerResult = cms.InputTag('TriggerResults', '', 'HLT'),
  labelTrack = cms.string('generalTracks'),
  labelVertex = cms.string('offlinePrimaryVertices'),
  labelEBRecHit = cms.string('EcalRecHitsEB'),
  labelEERecHit = cms.string('EcalRecHitsEE'),
  labelHBHERecHit = cms.string('hbhereco'),
  labelBeamSpot = cms.string('offlineBeamSpot'),
  labelCaloTower = cms.string('towerMaker'),
  algInputTag = cms.InputTag('gtStage2Digis'),
  extInputTag = cms.InputTag('gtStage2Digis'),
  moduleName = cms.untracked.string(''),
  producerName = cms.untracked.string(''),
  useRaw = cms.untracked.int32(0),
  ignoreTriggers = cms.untracked.bool(False),
  useL1Trigger = cms.untracked.bool(False),
  hcalScale = cms.untracked.double(1),
  dataType = cms.untracked.int32(0),
  outMode = cms.untracked.int32(11),
  unCorrect = cms.untracked.bool(False),
  collapseDepth = cms.untracked.bool(False),
  l1TrigName = cms.untracked.string('L1_SingleJet60'),
  matrixECAL = cms.untracked.int32(5),
  matrixHCAL = cms.untracked.int32(3)
)
