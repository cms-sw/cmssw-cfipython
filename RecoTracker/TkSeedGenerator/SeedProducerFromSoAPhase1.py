import FWCore.ParameterSet.Config as cms

def SeedProducerFromSoAPhase1(**kwargs):
  mod = cms.EDProducer('SeedProducerFromSoAPhase1',
    beamSpot = cms.InputTag('offlineBeamSpot'),
    src = cms.InputTag('pixelTrackSoA'),
    minNumberOfHits = cms.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod