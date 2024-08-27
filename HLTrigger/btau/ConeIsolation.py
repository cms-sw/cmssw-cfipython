import FWCore.ParameterSet.Config as cms

def ConeIsolation(**kwargs):
  mod = cms.EDProducer('ConeIsolation',
    JetTrackSrc = cms.InputTag('ic5JetTracksAssociatorAtVertex'),
    vertexSrc = cms.InputTag('offlinePrimaryVertices'),
    BeamSpotProducer = cms.InputTag('offlineBeamSpot'),
    useBeamSpot = cms.bool(False),
    MinimumNumberOfPixelHits = cms.int32(2),
    MinimumNumberOfHits = cms.int32(8),
    MaximumTransverseImpactParameter = cms.double(0.03),
    MinimumTransverseMomentum = cms.double(1),
    MaximumChiSquared = cms.double(100),
    DeltaZetTrackVertex = cms.double(0.2),
    useVertex = cms.bool(True),
    MatchingCone = cms.double(0.1),
    SignalCone = cms.double(0.07),
    IsolationCone = cms.double(0.45),
    MinimumTransverseMomentumInIsolationRing = cms.double(0),
    MinimumTransverseMomentumLeadingTrack = cms.double(6),
    MaximumNumberOfTracksIsolationRing = cms.int32(0),
    UseFixedSizeCone = cms.bool(True),
    VariableConeParameter = cms.double(3.5),
    VariableMaxCone = cms.double(0.17),
    VariableMinCone = cms.double(0.05),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
