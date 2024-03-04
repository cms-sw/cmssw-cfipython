import FWCore.ParameterSet.Config as cms

def APVModeFilter(**kwargs):
  mod = cms.EDFilter('APVModeFilter',
    apvMode = cms.untracked.string('deco'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
