import FWCore.ParameterSet.Config as cms

def TrackWithVertexSelector(*args, **kwargs):
  mod = cms.EDProducer('TrackWithVertexSelector',
    src = cms.InputTag('generalTracks'),
    copyExtras = cms.untracked.bool(False),
    copyTrajectories = cms.untracked.bool(False),
    numberOfValidHits = cms.uint32(0),
    numberOfValidPixelHits = cms.uint32(0),
    numberOfLostHits = cms.uint32(999),
    normalizedChi2 = cms.double(999999),
    ptMin = cms.double(0.3),
    ptMax = cms.double(500),
    etaMin = cms.double(0),
    etaMax = cms.double(50),
    dzMax = cms.double(999),
    d0Max = cms.double(999),
    ptErrorCut = cms.double(0.2),
    quality = cms.string('highPurity'),
    useVtx = cms.bool(True),
    nVertices = cms.uint32(0),
    vertexTag = cms.InputTag('offlinePrimaryVertices'),
    timesTag = cms.InputTag(''),
    timeResosTag = cms.InputTag(''),
    vtxFallback = cms.bool(True),
    zetaVtx = cms.double(1),
    rhoVtx = cms.double(0.2),
    nSigmaDtVertex = cms.double(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
