import FWCore.ParameterSet.Config as cms

def LumiTestWriteAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('LumiTestWriteAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
