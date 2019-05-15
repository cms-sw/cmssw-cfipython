import FWCore.ParameterSet.Config as cms

multiHitFromChi2EDProducerDefault = cms.EDProducer('MultiHitFromChi2EDProducer',
  doublets = cms.InputTag('hitPairEDProducer'),
  maxElement = cms.uint32(1000000),
  useFixedPreFiltering = cms.bool(False),
  phiPreFiltering = cms.double(0.3),
  extraHitRPhitolerance = cms.double(0),
  extraHitRZtolerance = cms.double(0),
  extraZKDBox = cms.double(0.2),
  extraRKDBox = cms.double(0.2),
  extraPhiKDBox = cms.double(0.005),
  fnSigmaRZ = cms.double(2),
  refitHits = cms.bool(True),
  ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
  TTRHBuilder = cms.string('WithTrackAngle'),
  maxChi2 = cms.double(5),
  chi2VsPtCut = cms.bool(True),
  pt_interv = cms.vdouble(
    0.4,
    0.7,
    1,
    2
  ),
  chi2_cuts = cms.vdouble(
    3,
    4,
    5,
    5
  ),
  detIdsToDebug = cms.vint32(
    0,
    0,
    0
  )
)
