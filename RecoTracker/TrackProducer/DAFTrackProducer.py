import FWCore.ParameterSet.Config as cms

def DAFTrackProducer(*args, **kwargs):
  mod = cms.EDProducer('DAFTrackProducer',
    TrajectoryInEvent = cms.bool(False),
    src = cms.InputTag('DAFTrackCandidateMaker'),
    TrajAnnealingSaving = cms.bool(False),
    MeasurementCollector = cms.string('simpleMultiRecHitCollector'),
    UpdatorName = cms.string('SiTrackerMultiRecHitUpdator'),
    beamSpot = cms.InputTag('offlineBeamSpot'),
    MeasurementTrackerEvent = cms.InputTag('MeasurementTrackerEvent'),
    useSimpleMF = cms.bool(False),
    SimpleMagneticField = cms.string(''),
    Fitter = cms.string('KFFittingSmootherWithOutliersRejectionAndRK'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    MeasurementTracker = cms.string(''),
    MinHits = cms.int32(3),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
