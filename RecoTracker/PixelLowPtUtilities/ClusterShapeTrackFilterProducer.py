import FWCore.ParameterSet.Config as cms

def ClusterShapeTrackFilterProducer(**kwargs):
  mod = cms.EDProducer('ClusterShapeTrackFilterProducer',
    clusterShapeCacheSrc = cms.InputTag('siPixelClusterShapeCache'),
    ptMin = cms.double(0),
    ptMax = cms.double(999999),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
