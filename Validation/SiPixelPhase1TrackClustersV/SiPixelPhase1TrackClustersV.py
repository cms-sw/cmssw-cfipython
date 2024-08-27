import FWCore.ParameterSet.Config as cms

def SiPixelPhase1TrackClustersV(**kwargs):
  mod = cms.EDProducer('SiPixelPhase1TrackClustersV',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
