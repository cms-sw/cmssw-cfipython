import FWCore.ParameterSet.Config as cms

def GlobalTrackQualityProducer(**kwargs):
  mod = cms.EDProducer('GlobalTrackQualityProducer',
    ServiceParameters = cms.PSet(),
    GlobalMuonTrackMatcher = cms.PSet(),
    InputCollection = cms.InputTag('globalMuons'),
    InputLinksCollection = cms.InputTag('globalMuons'),
    BaseLabel = cms.string('GLB'),
    RefitterParameters = cms.PSet(
      DTRecSegmentLabel = cms.InputTag('dt1DRecHits'),
      CSCRecSegmentLabel = cms.InputTag('csc2DRecHits'),
      GEMRecHitLabel = cms.InputTag('gemRecHits'),
      ME0RecHitLabel = cms.InputTag('me0Segments'),
      RPCRecSegmentLabel = cms.InputTag('rpcRecHits'),
      Fitter = cms.string('KFFitterForRefitInsideOut'),
      Smoother = cms.string('KFSmootherForRefitInsideOut'),
      Propagator = cms.string('SmartPropagatorAnyRK'),
      TrackerRecHitBuilder = cms.string('WithAngleAndTemplate'),
      MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
      DoPredictionsOnly = cms.bool(False),
      RefitDirection = cms.string('insideOut'),
      PropDirForCosmics = cms.bool(False),
      RefitRPCHits = cms.bool(True),
      DYTthrs = cms.vint32(
        10,
        10
      ),
      DYTselector = cms.int32(1),
      DYTupdator = cms.bool(False),
      DYTuseAPE = cms.bool(False),
      DYTuseThrsParametrization = cms.bool(True),
      DYTthrsParameters = cms.PSet(
        eta0p8 = cms.vdouble(
          1,
          -0.919853,
          0.990742
        ),
        eta1p2 = cms.vdouble(
          1,
          -0.897354,
          0.987738
        ),
        eta2p0 = cms.vdouble(
          4,
          -0.986855,
          0.998516
        ),
        eta2p2 = cms.vdouble(
          1,
          -0.940342,
          0.992955
        ),
        eta2p4 = cms.vdouble(
          1,
          -0.947633,
          0.993762
        )
      ),
      SkipStation = cms.int32(-1),
      TrackerSkipSystem = cms.int32(-1),
      TrackerSkipSection = cms.int32(-1),
      RefitFlag = cms.bool(True)
    ),
    nSigma = cms.double(3),
    MaxChi2 = cms.double(100000),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
