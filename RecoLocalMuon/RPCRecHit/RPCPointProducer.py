import FWCore.ParameterSet.Config as cms

def RPCPointProducer(**kwargs):
  mod = cms.EDProducer('RPCPointProducer',
    incldt = cms.bool(True),
    inclcsc = cms.bool(True),
    incltrack = cms.bool(False),
    debug = cms.untracked.bool(False),
    rangestrips = cms.double(4),
    rangestripsRB4 = cms.double(4),
    MinCosAng = cms.double(0.85),
    MaxD = cms.double(80),
    MaxDrb4 = cms.double(150),
    ExtrapolatedRegion = cms.double(0.5),
    cscSegments = cms.InputTag('hltCscSegments'),
    dt4DSegments = cms.InputTag('hltDt4DSegments'),
    tracks = cms.InputTag('standAloneMuons'),
    minBX = cms.int32(-2),
    maxBX = cms.int32(2),
    TrackTransformer = cms.PSet(
      DoPredictionsOnly = cms.bool(False),
      Fitter = cms.string('KFFitterForRefitInsideOut'),
      TrackerRecHitBuilder = cms.string('WithTrackAngle'),
      Smoother = cms.string('KFSmootherForRefitInsideOut'),
      MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
      RefitDirection = cms.string('alongMomentum'),
      RefitRPCHits = cms.bool(False),
      Propagator = cms.string('SmartPropagatorAnyRKOpposite')
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
