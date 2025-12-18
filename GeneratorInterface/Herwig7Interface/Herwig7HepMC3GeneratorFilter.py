import FWCore.ParameterSet.Config as cms

def Herwig7HepMC3GeneratorFilter(*args, **kwargs):
  mod = cms.EDFilter('Herwig7HepMC3GeneratorFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
