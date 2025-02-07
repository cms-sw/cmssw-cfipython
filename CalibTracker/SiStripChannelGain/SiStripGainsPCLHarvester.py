import FWCore.ParameterSet.Config as cms

def SiStripGainsPCLHarvester(*args, **kwargs):
  mod = cms.EDProducer('SiStripGainsPCLHarvester',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
