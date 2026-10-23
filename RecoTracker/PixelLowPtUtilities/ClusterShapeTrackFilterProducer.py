import FWCore.ParameterSet.Config as cms

def ClusterShapeTrackFilterProducer(*args, **kwargs):
  mod = cms.EDProducer('ClusterShapeTrackFilterProducer',
    clusterShapeCacheSrc = cms.InputTag('siPixelClusterShapeCache'),
    ptMin = cms.double(0),
    ptMax = cms.double(999999),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
