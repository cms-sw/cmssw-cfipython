import FWCore.ParameterSet.Config as cms

def APVModeFilter(*args, **kwargs):
  mod = cms.EDFilter('APVModeFilter',
    apvMode = cms.untracked.string('deco'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
