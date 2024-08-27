import FWCore.ParameterSet.Config as cms

def CandIPProducer(**kwargs):
  mod = cms.EDProducer('CandIPProducer',
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(8),
    minimumTransverseMomentum = cms.double(1),
    primaryVertex = cms.InputTag('offlinePrimaryVertices'),
    maximumLongitudinalImpactParameter = cms.double(17),
    computeGhostTrack = cms.bool(True),
    maxDeltaR = cms.double(0.4),
    candidates = cms.InputTag('particleFlow'),
    jetDirectionUsingGhostTrack = cms.bool(False),
    minimumNumberOfPixelHits = cms.int32(2),
    jetDirectionUsingTracks = cms.bool(False),
    computeProbabilities = cms.bool(True),
    useTrackQuality = cms.bool(False),
    jets = cms.InputTag('ak4PFJetsCHS'),
    ghostTrackPriorDeltaR = cms.double(0.03),
    maximumChiSquared = cms.double(5),
    explicitJTA = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
