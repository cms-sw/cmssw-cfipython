import FWCore.ParameterSet.Config as cms

def JetValidation(*args, **kwargs):
  mod = cms.EDAnalyzer('JetValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
