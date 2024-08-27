import FWCore.ParameterSet.Config as cms

def PixelTrackCleanerBySharedHitsESProducer(**kwargs):
  mod = cms.ESProducer('PixelTrackCleanerBySharedHitsESProducer',
    ComponentName = cms.string('pixelTrackCleanerBySharedHits'),
    useQuadrupletAlgo = cms.bool(False),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
