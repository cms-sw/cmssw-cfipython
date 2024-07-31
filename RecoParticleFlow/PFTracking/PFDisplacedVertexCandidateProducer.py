import FWCore.ParameterSet.Config as cms

def PFDisplacedVertexCandidateProducer(**kwargs):
  mod = cms.EDProducer('PFDisplacedVertexCandidateProducer',
    trackCollection = cms.InputTag('generalTracks'),
    verbose = cms.untracked.bool(False),
    debug = cms.untracked.bool(False),
    dcaCut = cms.double(0.5),
    primaryVertexCut = cms.double(1.8),
    dcaPInnerHitCut = cms.double(1000),
    mainVertexLabel = cms.InputTag('offlinePrimaryVertices'),
    offlineBeamSpotLabel = cms.InputTag('offlineBeamSpot'),
    tracksSelectorParameters = cms.PSet(
      nChi2_max = cms.double(5),
      pt_min = cms.double(0.2),
      pt_min_prim = cms.double(0.8),
      dxy = cms.double(0.2)
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
