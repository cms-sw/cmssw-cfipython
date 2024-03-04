import FWCore.ParameterSet.Config as cms

def GlobalDigisAnalyzer(**kwargs):
  mod = cms.EDProducer('GlobalDigisAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
