import FWCore.ParameterSet.Config as cms

def SiStripClusters2ApproxClusters(**kwargs):
  mod = cms.EDProducer('SiStripClusters2ApproxClusters',
    inputClusters = cms.InputTag('siStripClusters'),
    maxSaturatedStrips = cms.uint32(3),
    clusterShapeHitFilterLabel = cms.string('ClusterShapeHitFilter'),
    beamSpot = cms.InputTag('offlineBeamSpot'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
