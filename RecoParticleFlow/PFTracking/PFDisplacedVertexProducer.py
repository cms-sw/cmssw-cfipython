import FWCore.ParameterSet.Config as cms

def PFDisplacedVertexProducer(**kwargs):
  mod = cms.EDProducer('PFDisplacedVertexProducer',
    vertexCandidatesLabel = cms.InputTag('particleFlowDisplacedVertexCandidate'),
    verbose = cms.untracked.bool(False),
    debug = cms.untracked.bool(False),
    transvSize = cms.double(1),
    longSize = cms.double(5),
    primaryVertexCut = cms.double(1.8),
    tobCut = cms.double(100),
    tecCut = cms.double(220),
    minAdaptWeight = cms.double(0.5),
    switchOff2TrackVertex = cms.untracked.bool(True),
    mainVertexLabel = cms.InputTag('offlinePrimaryVertices'),
    offlineBeamSpotLabel = cms.InputTag('offlineBeamSpot'),
    tracksSelectorParameters = cms.PSet(
      bSelectTracks = cms.bool(True),
      quality = cms.string('HighPurity'),
      nChi2_max = cms.double(5),
      pt_min = cms.double(0.2),
      nChi2_min = cms.double(0.5),
      dxy_min = cms.double(0.2),
      nHits_min = cms.int32(6),
      nOuterHits_max = cms.int32(9)
    ),
    vertexIdentifierParameters = cms.PSet(
      bIdentifyVertices = cms.bool(True),
      pt_min = cms.double(0.5),
      pt_kink_min = cms.double(3),
      logPrimSec_min = cms.double(0),
      looper_eta_max = cms.double(0.1),
      masses = cms.vdouble(
        0.05,
        0.485,
        0.515,
        0.48,
        0.52,
        1.107,
        1.125,
        0.2
      ),
      angles = cms.vdouble(
        15,
        15
      )
    ),
    avfParameters = cms.PSet(
      sigmacut = cms.double(6),
      Tini = cms.double(256),
      ratio = cms.double(0.25)
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
