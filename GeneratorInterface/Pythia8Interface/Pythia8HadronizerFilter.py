import FWCore.ParameterSet.Config as cms

def Pythia8HadronizerFilter(**kwargs):
  mod = cms.EDFilter('Pythia8HadronizerFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
