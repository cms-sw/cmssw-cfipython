import FWCore.ParameterSet.Config as cms

candidatePointSeededTrackingRegionsFromBeamSpot = cms.EDProducer('CandidatePointSeededTrackingRegionsEDProducer',
  RegionPSet = cms.PSet(
    operationMode = cms.string('BeamSpotFixed'),
    seedingMode = cms.string('Candidate'),
    input = cms.InputTag(''),
    points = cms.PSet(
      eta = cms.vdouble(),
      phi = cms.vdouble()
    ),
    maxNRegions = cms.uint32(10),
    beamSpot = cms.InputTag('hltOnlineBeamSpot'),
    vertexCollection = cms.InputTag('hltPixelVertices'),
    maxNVertices = cms.uint32(1),
    ptMin = cms.double(0.9),
    originRadius = cms.double(0.2),
    zErrorBeamSpot = cms.double(24.2),
    deltaEta_Cand = cms.double(-1),
    deltaPhi_Cand = cms.double(-1),
    deltaEta_Point = cms.double(-1),
    deltaPhi_Point = cms.double(-1),
    precise = cms.bool(True),
    nSigmaZVertex = cms.double(3),
    zErrorVetex = cms.double(0.2),
    nSigmaZBeamSpot = cms.double(4),
    whereToUseMeasurementTracker = cms.string('ForSiStrips'),
    measurementTrackerName = cms.InputTag(''),
    searchOpt = cms.bool(False)
  )
)
