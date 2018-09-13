import FWCore.ParameterSet.Config as cms

L2MuonProducer = cms.EDProducer('L2MuonProducer',
  ServiceParameters = cms.PSet(
    Propagators = cms.untracked.vstring('hltESPFastSteppingHelixPropagatorAnyhltESPFastSteppingHelixPropagatorOpposite'),
    RPCLayers = cms.bool(True),
    UseMuonNavigation = cms.untracked.bool(True)
  ),
  InputObjects = cms.InputTag('hltL2MuonSeeds'),
  SeedTransformerParameters = cms.PSet(
    Fitter = cms.string('hltESPKFFittingSmootherForL2Muon'),
    MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
    NMinRecHits = cms.uint32(2),
    UseSubRecHits = cms.bool(False),
    Propagator = cms.string('hltESPFastSteppingHelixPropagatorAny'),
    RescaleError = cms.double(100)
  ),
  L2TrajBuilderParameters = cms.PSet(
    DoRefit = cms.bool(False),
    SeedPropagator = cms.string('hltESPFastSteppingHelixPropagatorAny'),
    FilterParameters = cms.PSet(
      NumberOfSigma = cms.double(3),
      FitDirection = cms.string('insideOut'),
      DTRecSegmentLabel = cms.InputTag('hltDt4DSegments'),
      MaxChi2 = cms.double(1000),
      MuonTrajectoryUpdatorParameters = cms.PSet(
        MaxChi2 = cms.double(25),
        RescaleErrorFactor = cms.double(100),
        Granularity = cms.int32(0),
        ExcludeRPCFromFit = cms.bool(False),
        UseInvalidHits = cms.bool(True),
        RescaleError = cms.bool(False)
      ),
      EnableRPCMeasurement = cms.bool(True),
      CSCRecSegmentLabel = cms.InputTag('hltCscSegments'),
      EnableDTMeasurement = cms.bool(True),
      RPCRecSegmentLabel = cms.InputTag('hltRpcRecHits'),
      Propagator = cms.string('hltESPFastSteppingHelixPropagatorAny'),
      EnableGEMMeasurement = cms.bool(False),
      GEMRecSegmentLabel = cms.InputTag('gemRecHits'),
      EnableCSCMeasurement = cms.bool(True)
    ),
    NavigationType = cms.string('Standard'),
    SeedTransformerParameters = cms.PSet(
      Fitter = cms.string('hltESPKFFittingSmootherForL2Muon'),
      MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
      NMinRecHits = cms.uint32(2),
      UseSubRecHits = cms.bool(False),
      Propagator = cms.string('hltESPFastSteppingHelixPropagatorAny'),
      RescaleError = cms.double(100)
    ),
    DoBackwardFilter = cms.bool(True),
    SeedPosition = cms.string('in'),
    BWFilterParameters = cms.PSet(
      NumberOfSigma = cms.double(3),
      CSCRecSegmentLabel = cms.InputTag('hltCscSegments'),
      FitDirection = cms.string('outsideIn'),
      DTRecSegmentLabel = cms.InputTag('hltDt4DSegments'),
      MaxChi2 = cms.double(100),
      MuonTrajectoryUpdatorParameters = cms.PSet(
        MaxChi2 = cms.double(25),
        RescaleErrorFactor = cms.double(100),
        Granularity = cms.int32(0),
        ExcludeRPCFromFit = cms.bool(False),
        UseInvalidHits = cms.bool(True),
        RescaleError = cms.bool(False)
      ),
      EnableRPCMeasurement = cms.bool(True),
      BWSeedType = cms.string('fromGenerator'),
      EnableDTMeasurement = cms.bool(True),
      RPCRecSegmentLabel = cms.InputTag('hltRpcRecHits'),
      Propagator = cms.string('hltESPFastSteppingHelixPropagatorAny'),
      EnableGEMMeasurement = cms.bool(False),
      GEMRecSegmentLabel = cms.InputTag('gemRecHits'),
      EnableCSCMeasurement = cms.bool(True)
    ),
    DoSeedRefit = cms.bool(False)
  ),
  DoSeedRefit = cms.bool(False),
  TrackLoaderParameters = cms.PSet(
    Smoother = cms.string('hltESPKFTrajectorySmootherForMuonTrackLoader'),
    DoSmoothing = cms.bool(False),
    beamSpot = cms.InputTag('hltOnlineBeamSpot'),
    MuonUpdatorAtVertexParameters = cms.PSet(
      MaxChi2 = cms.double(1000000),
      BeamSpotPosition = cms.vdouble(
        0,
        0,
        0
      ),
      Propagator = cms.string('hltESPFastSteppingHelixPropagatorOpposite'),
      BeamSpotPositionErrors = cms.vdouble(
        0.1,
        0.1,
        5.3
      )
    ),
    VertexConstraint = cms.bool(True),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle')
  ),
  MuonTrajectoryBuilder = cms.string('Exhaustive')
)
