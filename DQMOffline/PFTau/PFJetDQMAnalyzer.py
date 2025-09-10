import FWCore.ParameterSet.Config as cms

def PFJetDQMAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('PFJetDQMAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
