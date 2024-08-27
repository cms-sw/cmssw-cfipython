import FWCore.ParameterSet.Config as cms

def SiPixelPhase1TrackingParticleV(**kwargs):
  mod = cms.EDProducer('SiPixelPhase1TrackingParticleV',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
