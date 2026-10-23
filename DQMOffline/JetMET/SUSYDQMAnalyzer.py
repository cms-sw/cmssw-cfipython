import FWCore.ParameterSet.Config as cms

def SUSYDQMAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('SUSYDQMAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
