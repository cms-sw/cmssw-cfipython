import FWCore.ParameterSet.Config as cms

alcaisotrk = cms.EDProducer('AlCaIsoTracksProducer',
  TrackLabel = cms.InputTag('generalTracks'),
  VertexLabel = cms.InputTag('offlinePrimaryVertices'),
  BeamSpotLabel = cms.InputTag('offlineBeamSpot'),
  EBRecHitLabel = cms.InputTag('ecalRecHit', 'EcalRecHitsEB'),
  EERecHitLabel = cms.InputTag('ecalRecHit', 'EcalRecHitsEE'),
  HBHERecHitLabel = cms.InputTag('hbhereco'),
  L1GTSeedLabel = cms.InputTag('hltL1sV0SingleJet60'),
  TriggerEventLabel = cms.InputTag('hltTriggerSummaryAOD', '', 'HLT'),
  TriggerResultLabel = cms.InputTag('TriggerResults', '', 'HLT'),
  IsoTrackLabel = cms.string('HcalIsolatedTrackCollection'),
  triggers = cms.vstring(
    'HLT_IsoTrackHB',
    'HLT_IsoTrackHE'
  ),
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
  momentumRangeLow = cms.double(20),
  momentumRangeHigh = cms.double(40),
  preScaleFactor = cms.int32(10),
  mightGet = cms.optional.untracked.vstring
)
