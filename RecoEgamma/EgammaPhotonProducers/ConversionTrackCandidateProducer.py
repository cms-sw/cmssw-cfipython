import FWCore.ParameterSet.Config as cms

def ConversionTrackCandidateProducer(*args, **kwargs):
  mod = cms.EDProducer('ConversionTrackCandidateProducer',
    bcBarrelCollection = cms.InputTag('particleFlowSuperClusterECAL', 'particleFlowBasicClusterECALBarrel'),
    bcEndcapCollection = cms.InputTag('particleFlowSuperClusterECAL', 'particleFlowBasicClusterECALEndcap'),
    scHybridBarrelProducer = cms.InputTag('particleFlowSuperClusterECAL', 'particleFlowSuperClusterECALBarrel'),
    scIslandEndcapProducer = cms.InputTag('particleFlowSuperClusterECAL', 'particleFlowSuperClusterECALEndcapWithPreshower'),
    outInTrackCandidateSCAssociationCollection = cms.string('outInTrackCandidateSCAssociationCollection'),
    inOutTrackCandidateSCAssociationCollection = cms.string('inOutTrackCandidateSCAssociationCollection'),
    outInTrackCandidateCollection = cms.string('outInTracksFromConversions'),
    inOutTrackCandidateCollection = cms.string('inOutTracksFromConversions'),
    barrelEcalRecHitCollection = cms.InputTag('ecalRecHit', 'EcalRecHitsEB'),
    endcapEcalRecHitCollection = cms.InputTag('ecalRecHit', 'EcalRecHitsEE'),
    MeasurementTrackerName = cms.string(''),
    OutInRedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    InOutRedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    useHitsSplitting = cms.bool(False),
    maxNumOfSeedsOutIn = cms.int32(50),
    maxNumOfSeedsInOut = cms.int32(50),
    bcEtCut = cms.double(1.5),
    bcECut = cms.double(1.5),
    useEtCut = cms.bool(True),
    hbheRecHits = cms.InputTag('hbhereco'),
    recHitEThresholdHB = cms.vdouble(
      0,
      0,
      0,
      0
    ),
    recHitEThresholdHE = cms.vdouble(
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ),
    usePFThresholdsFromDB = cms.bool(False),
    maxHcalRecHitSeverity = cms.int32(999999),
    minSCEt = cms.double(20),
    hOverEConeSize = cms.double(0.15),
    maxHOverE = cms.double(0.15),
    isoInnerConeR = cms.double(3.5),
    isoConeR = cms.double(0.4),
    isoEtaSlice = cms.double(2.5),
    isoEtMin = cms.double(0),
    isoEMin = cms.double(0.08),
    vetoClusteredHits = cms.bool(False),
    useNumXstals = cms.bool(True),
    ecalIsoCut_offset = cms.double(999999999),
    ecalIsoCut_slope = cms.double(0),
    RecHitFlagToBeExcludedEB = cms.vstring(),
    RecHitSeverityToBeExcludedEB = cms.vstring(),
    RecHitFlagToBeExcludedEE = cms.vstring(),
    RecHitSeverityToBeExcludedEE = cms.vstring(),
    fractionShared = cms.double(0.5),
    TrajectoryBuilder = cms.string('TrajectoryBuilderForConversions'),
    TrajectoryBuilderPSet = cms.PSet(),
    TransientInitialStateEstimatorParameters = cms.PSet(
      propagatorAlongTISE = cms.string('alongMomElePropagator'),
      numberMeasurementsForFit = cms.int32(4),
      propagatorOppositeTISE = cms.string('oppositeToMomElePropagator')
    ),
    allowSharedFirstHit = cms.bool(True),
    ValidHitBonus = cms.double(5),
    MissingHitPenalty = cms.double(20),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
