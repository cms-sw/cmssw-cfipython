import FWCore.ParameterSet.Config as cms

def SiStripClusters2ApproxClusters_v1(*args, **kwargs):
  mod = cms.EDProducer('SiStripClusters2ApproxClusters_v1',
    inputClusters = cms.InputTag('siStripClusters'),
    maxSaturatedStrips = cms.uint32(3),
    clusterShapeHitFilterLabel = cms.string('ClusterShapeHitFilter'),
    beamSpot = cms.InputTag('offlineBeamSpot'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
