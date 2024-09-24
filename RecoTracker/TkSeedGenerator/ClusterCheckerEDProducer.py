import FWCore.ParameterSet.Config as cms

def ClusterCheckerEDProducer(*args, **kwargs):
  mod = cms.EDProducer('ClusterCheckerEDProducer',
    doClusterCheck = cms.bool(True),
    MaxNumberOfStripClusters = cms.uint32(400000),
    ClusterCollectionLabel = cms.InputTag('siStripClusters'),
    MaxNumberOfPixelClusters = cms.uint32(40000),
    PixelClusterCollectionLabel = cms.InputTag('siPixelClusters'),
    cut = cms.string('strip < 400000 && pixel < 40000 && (strip < 50000 + 10*pixel) && (pixel < 5000 + 0.1*strip)'),
    silentClusterCheck = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
