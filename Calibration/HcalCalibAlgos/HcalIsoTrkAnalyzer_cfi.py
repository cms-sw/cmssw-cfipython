import FWCore.ParameterSet.Config as cms

HcalIsoTrkAnalyzer = cms.EDAnalyzer('HcalIsoTrkAnalyzer',
  Triggers = cms.vstring(
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
  ProcessName = cms.string('HLT'),
  L1Filter = cms.string(''),
  L2Filter = cms.string('L2Filter'),
  L3Filter = cms.string('Filter'),
  TrackQuality = cms.string('highPurity'),
  MinTrackPt = cms.double(1),
  MaxDxyPV = cms.double(0.02),
  MaxDzPV = cms.double(0.02),
  MaxChi2 = cms.double(5),
  MaxDpOverP = cms.double(0.1),
  MinOuterHit = cms.int32(4),
  MinLayerCrossed = cms.int32(8),
  MaxInMiss = cms.int32(0),
  MaxOutMiss = cms.int32(0),
  MinimumTrackP = cms.double(20),
  ConeRadius = cms.double(34.98),
  ConeRadiusMIP = cms.double(14),
  MaximumEcalEnergy = cms.double(2),
  MaxTrackP = cms.double(8),
  SlopeTrackP = cms.double(0.05090504066),
  IsolationEnergyStr = cms.double(2),
  IsolationEnergySft = cms.double(10),
  TriggerEventLabel = cms.InputTag('hltTriggerSummaryAOD', '', 'HLT'),
  TriggerResultLabel = cms.InputTag('TriggerResults', '', 'HLT'),
  TrackLabel = cms.string('generalTracks'),
  VertexLabel = cms.string('offlinePrimaryVertices'),
  EBRecHitLabel = cms.string('EcalRecHitsEB'),
  EERecHitLabel = cms.string('EcalRecHitsEE'),
  HBHERecHitLabel = cms.string('hbhereco'),
  BeamSpotLabel = cms.string('offlineBeamSpot'),
  CaloTowerLabel = cms.string('towerMaker'),
  AlgInputTag = cms.InputTag('gtStage2Digis'),
  ExtInputTag = cms.InputTag('gtStage2Digis'),
  ModuleName = cms.untracked.string(''),
  ProducerName = cms.untracked.string(''),
  IgnoreTriggers = cms.untracked.bool(False),
  UseRaw = cms.untracked.bool(False),
  HcalScale = cms.untracked.double(1),
  DataType = cms.untracked.int32(0),
  OutMode = cms.untracked.int32(11),
  UnCorrect = cms.untracked.bool(False),
  CollapseDepth = cms.untracked.bool(False),
  L1TrigName = cms.untracked.string('L1_SingleJet60')
)
