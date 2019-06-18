import FWCore.ParameterSet.Config as cms

HcalIsoTrackAnalysis = cms.EDAnalyzer('HcalIsoTrackAnalysis',
  trackQuality = cms.string('highPurity'),
  minTrackPt = cms.double(1),
  maxDxyPV = cms.vdouble(
    0.02,
    0.01,
    0.05,
    0.1
  ),
  maxDzPV = cms.vdouble(
    0.02,
    0.01,
    0.04,
    0.5
  ),
  maxChi2 = cms.vdouble(
    5,
    2,
    10,
    20
  ),
  maxDpOverP = cms.vdouble(
    0.1,
    0.02,
    0.05,
    0.4
  ),
  minOuterHit = cms.vint32(
    4,
    2,
    1,
    0
  ),
  minLayerCrossed = cms.vint32(
    8,
    4,
    2,
    0
  ),
  maxInMiss = cms.vint32(
    0,
    1,
    2,
    4
  ),
  maxOutMiss = cms.vint32(
    0,
    1,
    2,
    4
  ),
  coneRadius = cms.double(34.98),
  coneRadiusMIP = cms.double(14),
  EBHitEnergyThreshold = cms.double(0.08),
  EEHitEnergyThreshold0 = cms.double(0.3),
  EEHitEnergyThreshold1 = cms.double(0),
  EEHitEnergyThreshold2 = cms.double(0),
  EEHitEnergyThreshold3 = cms.double(0),
  EEHitEnergyThresholdLow = cms.double(0.3),
  EEHitEnergyThresholdHigh = cms.double(0.3),
  momentumLow = cms.double(40),
  momentumHigh = cms.double(60),
  labelTrack = cms.string('generalTracks'),
  labelVertex = cms.string('offlinePrimaryVertices'),
  labelEBRecHit = cms.string('EcalRecHitsEB'),
  labelEERecHit = cms.string('EcalRecHitsEE'),
  labelHBHERecHit = cms.string('hbhereco'),
  labelBeamSpot = cms.string('offlineBeamSpot'),
  useRaw = cms.untracked.int32(0),
  dataType = cms.untracked.int32(0),
  etaMin = cms.untracked.int32(-1),
  etaMax = cms.untracked.int32(10),
  mightGet = cms.optional.untracked.vstring
)
