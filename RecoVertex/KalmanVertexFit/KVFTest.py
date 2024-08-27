import FWCore.ParameterSet.Config as cms

def KVFTest(**kwargs):
  mod = cms.EDAnalyzer('KVFTest',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
