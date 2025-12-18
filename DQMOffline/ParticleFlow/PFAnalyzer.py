import FWCore.ParameterSet.Config as cms

def PFAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('PFAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
