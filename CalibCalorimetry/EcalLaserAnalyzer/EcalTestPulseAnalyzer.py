import FWCore.ParameterSet.Config as cms

def EcalTestPulseAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalTestPulseAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
