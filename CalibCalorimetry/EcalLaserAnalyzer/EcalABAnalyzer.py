import FWCore.ParameterSet.Config as cms

def EcalABAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalABAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
