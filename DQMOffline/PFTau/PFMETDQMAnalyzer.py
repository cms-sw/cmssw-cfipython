import FWCore.ParameterSet.Config as cms

def PFMETDQMAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('PFMETDQMAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
