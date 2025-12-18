import FWCore.ParameterSet.Config as cms

def Pythia8ConcurrentHadronizerFilter(*args, **kwargs):
  mod = cms.EDFilter('Pythia8ConcurrentHadronizerFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
