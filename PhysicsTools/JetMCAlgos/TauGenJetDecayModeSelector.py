import FWCore.ParameterSet.Config as cms

def TauGenJetDecayModeSelector(**kwargs):
  mod = cms.EDFilter('TauGenJetDecayModeSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
