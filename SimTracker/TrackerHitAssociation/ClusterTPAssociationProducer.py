import FWCore.ParameterSet.Config as cms

def ClusterTPAssociationProducer(**kwargs):
  mod = cms.EDProducer('ClusterTPAssociationProducer',
    simTrackSrc = cms.InputTag('g4SimHits'),
    pixelSimLinkSrc = cms.InputTag('simSiPixelDigis'),
    stripSimLinkSrc = cms.InputTag('simSiStripDigis'),
    phase2OTSimLinkSrc = cms.InputTag('simSiPixelDigis', 'Tracker'),
    pixelClusterSrc = cms.InputTag('siPixelClusters'),
    stripClusterSrc = cms.InputTag('siStripClusters'),
    phase2OTClusterSrc = cms.InputTag('siPhase2Clusters'),
    trackingParticleSrc = cms.InputTag('mix', 'MergedTrackTruth'),
    throwOnMissingCollections = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod