import FWCore.ParameterSet.Config as cms

def L1ABCDebugger(**kwargs):
  mod = cms.EDAnalyzer('L1ABCDebugger',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
