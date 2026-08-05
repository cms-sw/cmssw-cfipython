import FWCore.ParameterSet.Config as cms

def alpaka_rocm_async_PixelTrackTorchHighPuritySelector(*args, **kwargs):
  mod = cms.EDProducer('alpaka_rocm_async::PixelTrackTorchHighPuritySelector',
    pixelTrackSrc = cms.InputTag('hltPhase2PixelTracksSoA'),
    maxNumberOfTracks = cms.int32(100000),
    maxPreselectedTracks = cms.int32(10000),
    minNumberOfHits = cms.int32(0),
    avgHitsPerTrack = cms.int32(8),
    minimumTrackQuality = cms.string('tight'),
    model = cms.required.FileInPath,
    scoreThreshold = cms.double(0.5),
    batchSize = cms.int32(10),
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string(''),
      synchronize = cms.optional.untracked.bool
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
