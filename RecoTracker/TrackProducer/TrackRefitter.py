import FWCore.ParameterSet.Config as cms

def TrackRefitter(*args, **kwargs):
  mod = cms.EDProducer('TrackRefitter',
    TrajectoryInEvent = cms.bool(False),
    useHitsSplitting = cms.bool(False),
    src = cms.InputTag(''),
    constraint = cms.string(''),
    srcConstr = cms.InputTag(''),
    AlgorithmName = cms.string('undefAlgorithm'),
    GeometricInnerState = cms.bool(True),
    reMatchSplitHits = cms.bool(False),
    usePropagatorForPCA = cms.bool(False),
    beamSpot = cms.InputTag('offlineBeamSpot'),
    MeasurementTrackerEvent = cms.InputTag('MeasurementTrackerEvent'),
    useSimpleMF = cms.bool(False),
    SimpleMagneticField = cms.string(''),
    Fitter = cms.string('KFFittingSmootherWithOutliersRejectionAndRK'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    MeasurementTracker = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
