import FWCore.ParameterSet.Config as cms

def alpaka_cuda_async_Phase2OTRecHitsSoAConverter(*args, **kwargs):
  mod = cms.EDProducer('alpaka_cuda_async::Phase2OTRecHitsSoAConverter',
    pixelRecHitSoASource = cms.InputTag('hltPhase2SiPixelRecHitsSoA'),
    otRecHitSource = cms.InputTag('hltSiPhase2RecHits'),
    beamSpot = cms.InputTag('hltOnlineBeamSpot'),
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
