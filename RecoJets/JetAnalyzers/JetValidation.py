import FWCore.ParameterSet.Config as cms

def JetValidation(**kwargs):
  mod = cms.EDAnalyzer('JetValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
