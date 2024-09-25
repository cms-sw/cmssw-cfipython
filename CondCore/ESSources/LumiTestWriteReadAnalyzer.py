import FWCore.ParameterSet.Config as cms

def LumiTestWriteReadAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('LumiTestWriteReadAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
