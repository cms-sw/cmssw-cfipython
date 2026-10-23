import FWCore.ParameterSet.Config as cms

def HcalParametersAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalParametersAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
