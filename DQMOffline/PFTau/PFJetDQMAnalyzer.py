import FWCore.ParameterSet.Config as cms

def PFJetDQMAnalyzer(**kwargs):
  mod = cms.EDProducer('PFJetDQMAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
