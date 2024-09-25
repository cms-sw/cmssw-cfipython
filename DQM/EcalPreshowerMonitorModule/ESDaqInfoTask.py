import FWCore.ParameterSet.Config as cms

def ESDaqInfoTask(*args, **kwargs):
  mod = cms.EDAnalyzer('ESDaqInfoTask',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
