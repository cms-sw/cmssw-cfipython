import FWCore.ParameterSet.Config as cms

def JetAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('JetAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
