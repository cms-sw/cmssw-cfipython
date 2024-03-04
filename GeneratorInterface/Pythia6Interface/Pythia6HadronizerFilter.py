import FWCore.ParameterSet.Config as cms

def Pythia6HadronizerFilter(**kwargs):
  mod = cms.EDFilter('Pythia6HadronizerFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
