import FWCore.ParameterSet.Config as cms

def StopAfterNEvents(*args, **kwargs):
  mod = cms.EDFilter('StopAfterNEvents',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
