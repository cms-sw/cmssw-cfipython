import FWCore.ParameterSet.Config as cms

def SiPixelStatusHarvester(*args, **kwargs):
  mod = cms.EDProducer('SiPixelStatusHarvester',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
