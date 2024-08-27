import FWCore.ParameterSet.Config as cms

def InclusiveCandidateVertexFinder(**kwargs):
  mod = cms.EDProducer('InclusiveCandidateVertexFinder',
    beamSpot = cms.InputTag('offlineBeamSpot'),
    primaryVertices = cms.InputTag('offlinePrimaryVertices'),
    tracks = cms.InputTag('particleFlow'),
    minHits = cms.uint32(0),
    maximumLongitudinalImpactParameter = cms.double(0.3),
    maximumTimeSignificance = cms.double(3),
    minPt = cms.double(0.8),
    maxNTracks = cms.uint32(30),
    clusterizer = cms.PSet(
      seedMax3DIPSignificance = cms.double(9999),
      seedMax3DIPValue = cms.double(9999),
      seedMin3DIPSignificance = cms.double(1.2),
      seedMin3DIPValue = cms.double(0.005),
      clusterMaxDistance = cms.double(0.05),
      clusterMaxSignificance = cms.double(4.5),
      distanceRatio = cms.double(20),
      clusterMinAngleCosine = cms.double(0.5),
      maxTimeSignificance = cms.double(3.5)
    ),
    vertexMinAngleCosine = cms.double(0.95),
    vertexMinDLen2DSig = cms.double(2.5),
    vertexMinDLenSig = cms.double(0.5),
    fitterSigmacut = cms.double(3),
    fitterTini = cms.double(256),
    fitterRatio = cms.double(0.25),
    useDirectVertexFitter = cms.bool(True),
    useVertexReco = cms.bool(True),
    vertexReco = cms.PSet(
      finder = cms.string('avr'),
      primcut = cms.double(1),
      seccut = cms.double(3),
      smoothing = cms.bool(True)
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
