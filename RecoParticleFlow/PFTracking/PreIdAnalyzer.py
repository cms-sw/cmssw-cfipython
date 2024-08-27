import FWCore.ParameterSet.Config as cms

def PreIdAnalyzer(**kwargs):
  mod = cms.EDProducer('PreIdAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
