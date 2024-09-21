import FWCore.ParameterSet.Config as cms

def PFAnalyzer(**kwargs):
  mod = cms.EDProducer('PFAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
