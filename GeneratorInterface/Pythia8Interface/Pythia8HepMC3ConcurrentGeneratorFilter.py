import FWCore.ParameterSet.Config as cms

def Pythia8HepMC3ConcurrentGeneratorFilter(*args, **kwargs):
  mod = cms.EDFilter('Pythia8HepMC3ConcurrentGeneratorFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
