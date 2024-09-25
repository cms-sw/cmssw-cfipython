import FWCore.ParameterSet.Config as cms

def L1MuonSeededTrackingRegionsEDProducer(*args, **kwargs):
  mod = cms.EDProducer('L1MuonSeededTrackingRegionsEDProducer',
    Propagator = cms.string(''),
    L1MinPt = cms.double(-1),
    L1MaxEta = cms.double(5),
    L1MinQuality = cms.uint32(0),
    SetMinPtBarrelTo = cms.double(3.5),
    SetMinPtEndcapTo = cms.double(1),
    CentralBxOnly = cms.bool(True),
    RegionPSet = cms.PSet(
      mode = cms.string('BeamSpotSigma'),
      input = cms.InputTag(''),
      maxNRegions = cms.int32(10),
      beamSpot = cms.InputTag('hltOnlineBeamSpot'),
      vertexCollection = cms.InputTag('notUsed'),
      maxNVertices = cms.int32(1),
      ptMin = cms.double(0),
      originRadius = cms.double(0.2),
      zErrorBeamSpot = cms.double(24.2),
      ptRanges = cms.vdouble(
        0,
        1000000000
      ),
      deltaEtas = cms.vdouble(0.35),
      deltaPhis = cms.vdouble(0.2),
      precise = cms.bool(True),
      nSigmaZVertex = cms.double(3),
      zErrorVetex = cms.double(0.2),
      nSigmaZBeamSpot = cms.double(4),
      whereToUseMeasurementTracker = cms.string('Never'),
      measurementTrackerName = cms.InputTag(''),
      searchOpt = cms.bool(False)
    ),
    ServiceParameters = cms.PSet(
      Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny'),
      RPCLayers = cms.bool(False),
      UseMuonNavigation = cms.untracked.bool(False)
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
