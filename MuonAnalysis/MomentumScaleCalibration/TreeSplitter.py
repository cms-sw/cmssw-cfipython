import FWCore.ParameterSet.Config as cms

def TreeSplitter(**kwargs):
  mod = cms.EDAnalyzer('TreeSplitter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
