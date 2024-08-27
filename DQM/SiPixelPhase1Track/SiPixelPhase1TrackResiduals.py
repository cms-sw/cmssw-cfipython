import FWCore.ParameterSet.Config as cms

def SiPixelPhase1TrackResiduals(**kwargs):
  mod = cms.EDProducer('SiPixelPhase1TrackResiduals',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
