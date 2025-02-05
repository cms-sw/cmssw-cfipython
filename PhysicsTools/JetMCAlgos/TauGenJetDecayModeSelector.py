import FWCore.ParameterSet.Config as cms

def TauGenJetDecayModeSelector(*args, **kwargs):
  mod = cms.EDFilter('TauGenJetDecayModeSelector',
    src = cms.InputTag(''),
    select = cms.vstring(),
    filter = cms.bool(False),
    throwOnMissing = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
