import FWCore.ParameterSet.Config as cms

def PixelTrackCleanerBySharedHitsESProducer(*args, **kwargs):
  mod = cms.ESProducer('PixelTrackCleanerBySharedHitsESProducer',
    ComponentName = cms.string('pixelTrackCleanerBySharedHits'),
    useQuadrupletAlgo = cms.bool(False),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
