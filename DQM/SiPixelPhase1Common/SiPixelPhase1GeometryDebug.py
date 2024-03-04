import FWCore.ParameterSet.Config as cms

def SiPixelPhase1GeometryDebug(**kwargs):
  mod = cms.EDProducer('SiPixelPhase1GeometryDebug',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
