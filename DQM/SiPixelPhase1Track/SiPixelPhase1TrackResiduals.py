import FWCore.ParameterSet.Config as cms

def SiPixelPhase1TrackResiduals(*args, **kwargs):
  mod = cms.EDProducer('SiPixelPhase1TrackResiduals',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
