import FWCore.ParameterSet.Config as cms

def TkMSParameterizationTest(*args, **kwargs):
  mod = cms.EDAnalyzer('TkMSParameterizationTest',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
