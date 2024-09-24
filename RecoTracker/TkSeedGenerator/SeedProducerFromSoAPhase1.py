import FWCore.ParameterSet.Config as cms

def SeedProducerFromSoAPhase1(*args, **kwargs):
  mod = cms.EDProducer('SeedProducerFromSoAPhase1',
    beamSpot = cms.InputTag('offlineBeamSpot'),
    src = cms.InputTag('pixelTrackSoA'),
    minNumberOfHits = cms.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod