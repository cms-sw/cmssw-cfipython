import FWCore.ParameterSet.Config as cms

def EGEnergyAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('EGEnergyAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
