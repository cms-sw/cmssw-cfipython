import FWCore.ParameterSet.Config as cms

def CAOTRecHitsSoAConverter_alpaka(*args, **kwargs):
  mod = cms.EDProducer('CAOTRecHitsSoAConverter@alpaka',
    otRecHitSource = cms.InputTag('siPhase2RecHits'),
    beamSpot = cms.InputTag('offlineBeamSpot'),
    psOnly = cms.bool(False),
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
