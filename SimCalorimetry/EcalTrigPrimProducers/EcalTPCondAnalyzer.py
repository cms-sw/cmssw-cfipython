import FWCore.ParameterSet.Config as cms

def EcalTPCondAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalTPCondAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
