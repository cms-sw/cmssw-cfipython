import FWCore.ParameterSet.Config as cms

def LSTInputProducer_alpaka(*args, **kwargs):
  mod = cms.EDProducer('LSTInputProducer@alpaka',
    ptCut = cms.double(0.8),
    phase2OTRecHits = cms.InputTag('siPhase2RecHits'),
    beamSpot = cms.InputTag('offlineBeamSpot'),
    seedTracks = cms.VInputTag(
      'lstInitialStepSeedTracks',
      'lstHighPtTripletStepSeedTracks'
    ),
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
