import FWCore.ParameterSet.Config as cms

def SiPixelPhase1Harvester(*args, **kwargs):
  mod = cms.EDProducer('SiPixelPhase1Harvester',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
