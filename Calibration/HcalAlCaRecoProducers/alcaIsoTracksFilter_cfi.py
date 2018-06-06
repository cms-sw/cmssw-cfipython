import FWCore.ParameterSet.Config as cms

alcaIsoTracksFilter = cms.EDFilter('AlCaIsoTracksFilter',
  labelTrack = cms.InputTag('generalTracks'),
  labelVertex = cms.InputTag('offlinePrimaryVertices'),
  labelBeamSpot = cms.InputTag('offlineBeamSpot'),
  labelEBRecHit = cms.InputTag('ecalRecHit', 'EcalRecHitsEB'),
  labelEERecHit = cms.InputTag('ecalRecHit', 'EcalRecHitsEE'),
  labelHBHERecHit = cms.InputTag('hbhereco'),
  labelTriggerEvent = cms.InputTag('hltTriggerSummaryAOD', '', 'HLT'),
  labelTriggerResult = cms.InputTag('TriggerResults', '', 'HLT'),
  triggers = cms.vstring(),
  processName = cms.string('HLT'),
  trackQuality = cms.string('highPurity'),
  minTrackPt = cms.double(1),
  maxDxyPV = cms.double(10),
  maxDzPV = cms.double(100),
  maxChi2 = cms.double(5),
  maxDpOverP = cms.double(0.1),
  minOuterHit = cms.int32(4),
  minLayerCrossed = cms.int32(8),
  maxInMiss = cms.int32(2),
  maxOutMiss = cms.int32(2),
  coneRadius = cms.double(34.98),
  minimumTrackP = cms.double(20),
  coneRadiusMIP = cms.double(14),
  maximumEcalEnergy = cms.double(2),
  maxTrackP = cms.double(8),
  slopeTrackP = cms.double(0.05090504066),
  isolationEnergy = cms.double(10),
  EBHitEnergyThreshold = cms.double(0.1),
  EEHitEnergyThreshold0 = cms.double(-41.0664),
  EEHitEnergyThreshold1 = cms.double(68.795),
  EEHitEnergyThreshold2 = cms.double(-38.1483),
  EEHitEnergyThreshold3 = cms.double(7.04303),
  momentumRangeLow = cms.double(20),
  momentumRangeHigh = cms.double(40),
  preScaleFactor = cms.int32(2)
)
