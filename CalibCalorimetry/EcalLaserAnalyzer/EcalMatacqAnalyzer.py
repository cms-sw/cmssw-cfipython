import FWCore.ParameterSet.Config as cms

def EcalMatacqAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalMatacqAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
