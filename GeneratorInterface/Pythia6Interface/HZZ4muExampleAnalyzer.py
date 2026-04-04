import FWCore.ParameterSet.Config as cms

def HZZ4muExampleAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('HZZ4muExampleAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
