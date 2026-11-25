import FWCore.ParameterSet.Config as cms

def alpaka_rocm_async_TracksSoAMerger(*args, **kwargs):
  mod = cms.EDProducer('alpaka_rocm_async::TracksSoAMerger',
    inputTracks = cms.VInputTag(
      'pixelTracksHighPtAlpaka',
      'pixelTracksLowPtAlpaka'
    ),
    minQuality = cms.string('highPurity'),
    matchFraction = cms.double(0),
    minHitsForDuplicate = cms.int32(3),
    dupNSigma2 = cms.double(3),
    dupMaxDeltaR2 = cms.double(0.0004),
    dupPtDifference = cms.double(0.1),
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
