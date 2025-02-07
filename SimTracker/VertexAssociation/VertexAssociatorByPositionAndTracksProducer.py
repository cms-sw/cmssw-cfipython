import FWCore.ParameterSet.Config as cms

def VertexAssociatorByPositionAndTracksProducer(*args, **kwargs):
  mod = cms.EDProducer('VertexAssociatorByPositionAndTracksProducer',
    absZ = cms.double(0.1),
    sigmaZ = cms.double(3),
    maxRecoZ = cms.double(1000),
    absT = cms.double(-1),
    sigmaT = cms.double(-1),
    maxRecoT = cms.double(-1),
    sharedTrackFraction = cms.double(-1),
    trackAssociation = cms.InputTag('trackingParticleRecoTrackAsssociation'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
