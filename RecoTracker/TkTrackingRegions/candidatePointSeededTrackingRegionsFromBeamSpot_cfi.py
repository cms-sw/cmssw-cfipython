import FWCore.ParameterSet.Config as cms

candidatePointSeededTrackingRegionsFromBeamSpot = cms.EDProducer('CandidatePointSeededTrackingRegionsEDProducer',
  RegionPSet = cms.PSet(
    seedingMode = cms.string('Candidate'),
    input = cms.InputTag(''),
    points = cms.PSet(
      eta = cms.vdouble(),
      phi = cms.vdouble()
    ),
    maxNRegions = cms.uint32(10),
    operationMode = cms.string('BeamSpotFixed'),
    beamSpot = cms.InputTag('hltOnlineBeamSpot'),
    vertexCollection = cms.InputTag('hltPixelVertices'),
    maxNVertices = cms.int32(1),
    nSigmaZBeamSpot = cms.double(4),
    zErrorBeamSpot = cms.double(24.2),
    nSigmaZVertex = cms.double(3),
    zErrorVertex = cms.double(0.2),
    ptMin = cms.double(0.9),
    originRadius = cms.double(0.2),
    deltaEta_Cand = cms.double(-1),
    deltaPhi_Cand = cms.double(-1),
    deltaEta_Point = cms.double(-1),
    deltaPhi_Point = cms.double(-1),
    precise = cms.bool(True),
    whereToUseMeasurementTracker = cms.string('ForSiStrips'),
    measurementTrackerName = cms.InputTag(''),
    searchOpt = cms.bool(False)
  ),
  mightGet = cms.optional.untracked.vstring
)
