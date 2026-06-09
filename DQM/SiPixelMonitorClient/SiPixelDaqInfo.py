import FWCore.ParameterSet.Config as cms

def SiPixelDaqInfo(*args, **kwargs):
  mod = cms.EDProducer('SiPixelDaqInfo',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
