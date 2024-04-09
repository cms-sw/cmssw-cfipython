import FWCore.ParameterSet.Config as cms

def Pythia8HepMC3ConcurrentGeneratorFilter(**kwargs):
  mod = cms.EDFilter('Pythia8HepMC3ConcurrentGeneratorFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod