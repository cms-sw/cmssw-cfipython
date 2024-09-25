import FWCore.ParameterSet.Config as cms

def EcalTrigPrimAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalTrigPrimAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
