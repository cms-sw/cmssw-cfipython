import FWCore.ParameterSet.Config as cms

def CandidateVertexArbitrator(*args, **kwargs):
  mod = cms.EDProducer('CandidateVertexArbitrator',
    beamSpot = cms.InputTag('offlineBeamSpot'),
    primaryVertices = cms.InputTag('offlinePrimaryVertices'),
    tracks = cms.InputTag('particleFlow'),
    secondaryVertices = cms.InputTag('candidateVertexMerger'),
    dLenFraction = cms.double(0.333),
    dRCut = cms.double(0.4),
    distCut = cms.double(0.04),
    sigCut = cms.double(5),
    fitterSigmacut = cms.double(3),
    fitterTini = cms.double(256),
    fitterRatio = cms.double(0.25),
    trackMinLayers = cms.int32(4),
    trackMinPt = cms.double(0.4),
    trackMinPixels = cms.int32(1),
    maxTimeSignificance = cms.double(3.5),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
