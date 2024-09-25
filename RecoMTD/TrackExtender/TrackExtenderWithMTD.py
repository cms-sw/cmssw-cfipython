import FWCore.ParameterSet.Config as cms

def TrackExtenderWithMTD(*args, **kwargs):
  mod = cms.EDProducer('TrackExtenderWithMTD',
    tracksSrc = cms.InputTag('generalTracks'),
    trjtrkAssSrc = cms.InputTag('generalTracks'),
    hitsSrc = cms.InputTag('mtdTrackingRecHits'),
    beamSpotSrc = cms.InputTag('offlineBeamSpot'),
    genVtxPositionSrc = cms.InputTag('genParticles', 'xyz0'),
    genVtxTimeSrc = cms.InputTag('genParticles', 't0'),
    vtxSrc = cms.InputTag('offlinePrimaryVertices4D'),
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
    estimatorMaxChi2 = cms.double(500),
    estimatorMaxNSigma = cms.double(10),
    btlChi2Cut = cms.double(50),
    btlTimeChi2Cut = cms.double(10),
    etlChi2Cut = cms.double(50),
    etlTimeChi2Cut = cms.double(10),
    useVertex = cms.bool(False),
    useSimVertex = cms.bool(False),
    dZCut = cms.double(0.1),
    bsTimeSpread = cms.double(0.2),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
