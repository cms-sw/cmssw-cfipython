import FWCore.ParameterSet.Config as cms

def EcalTestPulseAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('EcalTestPulseAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
