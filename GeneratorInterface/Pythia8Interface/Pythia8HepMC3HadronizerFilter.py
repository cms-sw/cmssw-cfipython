import FWCore.ParameterSet.Config as cms

def Pythia8HepMC3HadronizerFilter(*args, **kwargs):
  mod = cms.EDFilter('Pythia8HepMC3HadronizerFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
