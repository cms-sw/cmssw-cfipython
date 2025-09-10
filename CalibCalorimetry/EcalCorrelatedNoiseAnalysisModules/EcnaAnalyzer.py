import FWCore.ParameterSet.Config as cms

def EcnaAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('EcnaAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
