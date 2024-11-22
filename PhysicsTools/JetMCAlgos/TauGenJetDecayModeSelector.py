import FWCore.ParameterSet.Config as cms

def TauGenJetDecayModeSelector(*args, **kwargs):
  mod = cms.EDFilter('TauGenJetDecayModeSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
