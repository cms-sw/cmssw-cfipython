import FWCore.ParameterSet.Config as cms

def ESDcsInfoTask(*args, **kwargs):
  mod = cms.EDAnalyzer('ESDcsInfoTask',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
