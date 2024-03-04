import FWCore.ParameterSet.Config as cms

def EnergyScaleAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('EnergyScaleAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
