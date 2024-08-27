import FWCore.ParameterSet.Config as cms

def TrackIPProducer(**kwargs):
  mod = cms.EDProducer('TrackIPProducer',
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(8),
    minimumTransverseMomentum = cms.double(1),
    primaryVertex = cms.InputTag('offlinePrimaryVertices'),
    maximumLongitudinalImpactParameter = cms.double(17),
    computeGhostTrack = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetTracks = cms.InputTag('ak4JetTracksAssociatorAtVertexPF'),
    jetDirectionUsingGhostTrack = cms.bool(False),
    minimumNumberOfPixelHits = cms.int32(2),
    jetDirectionUsingTracks = cms.bool(False),
    computeProbabilities = cms.bool(True),
    useTrackQuality = cms.bool(False),
    maximumChiSquared = cms.double(5),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
