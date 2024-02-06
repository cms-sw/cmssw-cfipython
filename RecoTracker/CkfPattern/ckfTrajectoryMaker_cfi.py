import FWCore.ParameterSet.Config as cms

ckfTrajectoryMaker = cms.EDProducer('CkfTrajectoryMaker',
  trackCandidateAlso = cms.bool(False),
  cleanTrajectoryAfterInOut = cms.bool(True),
  doSeedingRegionRebuilding = cms.bool(True),
  onlyPixelHitsForSeedCleaner = cms.bool(False),
  reverseTrajectories = cms.bool(False),
  useHitsSplitting = cms.bool(True),
  MeasurementTrackerEvent = cms.InputTag('MeasurementTrackerEvent'),
  src = cms.InputTag('globalMixedSeeds'),
  clustersToSkip = cms.InputTag(''),
  phase2clustersToSkip = cms.InputTag(''),
  TrajectoryBuilderPSet = cms.PSet(),
  TransientInitialStateEstimatorParameters = cms.PSet(
    propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
    propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite'),
    numberMeasurementsForFit = cms.int32(4)
  ),
  numHitsForSeedCleaner = cms.int32(4),
  NavigationSchool = cms.string('SimpleNavigationSchool'),
  RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
  TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
  maxNSeeds = cms.uint32(500000),
  maxSeedsBeforeCleaning = cms.uint32(0),
  mightGet = cms.optional.untracked.vstring
)
