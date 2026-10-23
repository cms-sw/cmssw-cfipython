import FWCore.ParameterSet.Config as cms

def SiPixelBarycenter(*args, **kwargs):
  mod = cms.EDProducer('SiPixelBarycenter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
