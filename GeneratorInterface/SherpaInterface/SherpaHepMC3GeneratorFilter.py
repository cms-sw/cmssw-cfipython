import FWCore.ParameterSet.Config as cms

def SherpaHepMC3GeneratorFilter(*args, **kwargs):
  mod = cms.EDFilter('SherpaHepMC3GeneratorFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
