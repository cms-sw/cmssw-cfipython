import FWCore.ParameterSet.Config as cms

def GlobalHitsAnalyzer(**kwargs):
  mod = cms.EDProducer('GlobalHitsAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
