import FWCore.ParameterSet.Config as cms

def alpaka_rocm_async_PixelTrackTorchHighPuritySelector(*args, **kwargs):
  mod = cms.EDProducer('alpaka_rocm_async::PixelTrackTorchHighPuritySelector',
    pixelTrackSrc = cms.InputTag('hltPhase2PixelTracksSoA'),
    maxNumberOfTracks = cms.int32(122880),
    maxPreselectedTracks = cms.int32(9984),
    minNumberOfHits = cms.int32(0),
    avgHitsPerTrack = cms.int32(8),
    minimumTrackQuality = cms.string('tight'),
    model = cms.required.FileInPath,
    scoreThreshold = cms.double(0.4),
    batchSize = cms.int32(4992),
    scoreThresholdLowDxy = cms.double(-1),
    dxyRampKnee = cms.double(2),
    useHitFeatures = cms.bool(False),
    pixelRecHitSrc = cms.InputTag('siPixelRecHitsPreSplittingAlpaka'),
    vectorHitsSrc = cms.InputTag('phase2OTVectorHitsSoA'),
    otRecHitsSoASrc = cms.InputTag('caOTRecHitsSoA'),
    inferenceHalf = cms.bool(True),
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
