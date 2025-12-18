import FWCore.ParameterSet.Config as cms

def TrackProducerWithSCAssociation(*args, **kwargs):
  mod = cms.EDProducer('TrackProducerWithSCAssociation',
    TrajectoryInEvent = cms.bool(False),
    src = cms.InputTag('conversionTrackCandidates', 'inOutTracksFromConversions'),
    ComponentName = cms.string('ckfInOutTracksFromConversions'),
    producer = cms.string('conversionTrackCandidates'),
    trackCandidateSCAssociationCollection = cms.string('inOutTrackCandidateSCAssociationCollection'),
    recoTrackSCAssociationCollection = cms.string('inOutTrackSCAssociationCollection'),
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
