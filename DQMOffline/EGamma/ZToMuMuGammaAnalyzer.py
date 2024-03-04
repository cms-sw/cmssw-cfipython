import FWCore.ParameterSet.Config as cms

def ZToMuMuGammaAnalyzer(**kwargs):
  mod = cms.EDProducer('ZToMuMuGammaAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
