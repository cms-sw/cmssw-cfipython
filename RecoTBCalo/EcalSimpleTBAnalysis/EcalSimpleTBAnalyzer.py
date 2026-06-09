import FWCore.ParameterSet.Config as cms

def EcalSimpleTBAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalSimpleTBAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
