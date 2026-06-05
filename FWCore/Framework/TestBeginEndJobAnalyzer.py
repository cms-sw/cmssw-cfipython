import FWCore.ParameterSet.Config as cms

def TestBeginEndJobAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('TestBeginEndJobAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
