import FWCore.ParameterSet.Config as cms

def VertexAssociatorByPositionAndTracksProducerCPC(*args, **kwargs):
  mod = cms.EDProducer('VertexAssociatorByPositionAndTracksProducerCPC',
    trackAssociations = cms.VInputTag('trackingParticleRecoTrackAsssociation'),
    sigmaX = cms.double(-1),
    sigmaY = cms.double(-1),
    sigmaZ = cms.double(3),
    absZ = cms.double(0.1),
    maxRecoZ = cms.double(1000),
    sigmaT = cms.double(-1),
    absT = cms.double(-1),
    maxRecoT = cms.double(-1),
    sharedTrackFraction = cms.double(-1),
    weightMethod = cms.string('none'),
    filterSimVerticesForPVs = cms.bool(True),
    ignoreMissingAssociations = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
