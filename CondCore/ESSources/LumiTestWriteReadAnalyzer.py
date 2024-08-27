import FWCore.ParameterSet.Config as cms

def LumiTestWriteReadAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('LumiTestWriteReadAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
