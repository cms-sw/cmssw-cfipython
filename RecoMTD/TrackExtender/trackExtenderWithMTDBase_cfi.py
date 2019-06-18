import FWCore.ParameterSet.Config as cms

trackExtenderWithMTDBase = cms.EDProducer('TrackExtenderWithMTD',
  tracksSrc = cms.InputTag('generalTracks'),
  hitsSrc = cms.InputTag('mtdTrackingRecHits'),
  beamSpotSrc = cms.InputTag('offlineBeamSpot'),
  updateTrackTrajectory = cms.bool(True),
  updateTrackExtra = cms.bool(True),
  updateTrackHitPattern = cms.bool(True),
  TransientTrackBuilder = cms.string('TransientTrackBuilder'),
  MTDRecHitBuilder = cms.string('MTDRecHitBuilder'),
  Propagator = cms.string('PropagatorWithMaterialForMTD'),
  TrackTransformer = cms.PSet(
    DoPredictionsOnly = cms.bool(False),
    Fitter = cms.string('KFFitterForRefitInsideOut'),
    Smoother = cms.string('KFSmootherForRefitInsideOut'),
    Propagator = cms.string('PropagatorWithMaterialForMTD'),
    RefitDirection = cms.string('alongMomentum'),
    RefitRPCHits = cms.bool(True),
    TrackerRecHitBuilder = cms.string('WithTrackAngle'),
    MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
    MTDRecHitBuilder = cms.string('MTDRecHitBuilder')
  ),
  mightGet = cms.optional.untracked.vstring
)
