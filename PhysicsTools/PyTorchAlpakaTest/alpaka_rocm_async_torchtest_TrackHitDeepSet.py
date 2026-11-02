import FWCore.ParameterSet.Config as cms

def alpaka_rocm_async_torchtest_TrackHitDeepSet(*args, **kwargs):
  mod = cms.EDProducer('alpaka_rocm_async::torchtest::TrackHitDeepSet',
    model = cms.required.FileInPath,
    batchSize = cms.required.uint32,
    particles = cms.required.InputTag,
    hits = cms.required.InputTag,
    hit_to_track = cms.required.InputTag,
    environment = cms.untracked.int32(0),
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
