import FWCore.ParameterSet.Config as cms

def GsfTrackProducer(**kwargs):
  mod = cms.EDProducer('GsfTrackProducer',
    src = cms.InputTag('CkfElectronCandidates'),
    beamSpot = cms.InputTag('offlineBeamSpot'),
    producer = cms.string(''),
    Fitter = cms.string('GsfElectronFittingSmoother'),
    useHitsSplitting = cms.bool(False),
    TrajectoryInEvent = cms.bool(False),
    TTRHBuilder = cms.string('WithTrackAngle'),
    Propagator = cms.string('fwdElectronPropagator'),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag('MeasurementTrackerEvent'),
    GeometricInnerState = cms.bool(False),
    AlgorithmName = cms.string('gsf'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
