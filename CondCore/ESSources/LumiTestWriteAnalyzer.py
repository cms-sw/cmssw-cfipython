import FWCore.ParameterSet.Config as cms

def LumiTestWriteAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('LumiTestWriteAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
