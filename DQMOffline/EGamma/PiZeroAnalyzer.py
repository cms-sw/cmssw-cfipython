import FWCore.ParameterSet.Config as cms

def PiZeroAnalyzer(**kwargs):
  mod = cms.EDProducer('PiZeroAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
