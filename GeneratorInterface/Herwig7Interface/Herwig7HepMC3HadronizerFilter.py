import FWCore.ParameterSet.Config as cms

def Herwig7HepMC3HadronizerFilter(*args, **kwargs):
  mod = cms.EDFilter('Herwig7HepMC3HadronizerFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
