import FWCore.ParameterSet.Config as cms

def SiPixelClusterShapeCacheProducer(*args, **kwargs):
  mod = cms.EDProducer('SiPixelClusterShapeCacheProducer',
    src = cms.InputTag('siPixelClusters'),
    onDemand = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
