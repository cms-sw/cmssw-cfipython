import FWCore.ParameterSet.Config as cms

muonSeedGenerator = cms.EDProducer('MuonSeedGenerator',
  beamSpotTag = cms.InputTag('offlineBeamSpot'),
  scaleDT = cms.bool(True),
  CSCRecSegmentLabel = cms.InputTag('cscSegments'),
  DTRecSegmentLabel = cms.InputTag('dt4DSegments'),
  ME0RecSegmentLabel = cms.InputTag('me0Segments'),
  EnableDTMeasurement = cms.bool(True),
  EnableCSCMeasurement = cms.bool(True),
  EnableME0Measurement = cms.bool(False),
  crackEtas = cms.vdouble(
    0.2,
    1.6,
    1.7
  ),
  crackWindow = cms.double(0.04),
  deltaPhiSearchWindow = cms.double(0.25),
  deltaEtaSearchWindow = cms.double(0.2),
  deltaEtaCrackSearchWindow = cms.double(0.25),
  mightGet = cms.optional.untracked.vstring
)
