import FWCore.ParameterSet.Config as cms

def SiPixelPhase1TrackClusters(**kwargs):
  mod = cms.EDProducer('SiPixelPhase1TrackClusters',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
