import FWCore.ParameterSet.Config as cms

def ModuleNumbering(**kwargs):
  mod = cms.EDAnalyzer('ModuleNumbering',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
