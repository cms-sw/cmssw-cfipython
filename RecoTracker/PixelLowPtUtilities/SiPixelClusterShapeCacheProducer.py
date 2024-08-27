import FWCore.ParameterSet.Config as cms

def SiPixelClusterShapeCacheProducer(**kwargs):
  mod = cms.EDProducer('SiPixelClusterShapeCacheProducer',
    src = cms.InputTag('siPixelClusters'),
    onDemand = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
