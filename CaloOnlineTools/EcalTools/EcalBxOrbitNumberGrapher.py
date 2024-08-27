import FWCore.ParameterSet.Config as cms

def EcalBxOrbitNumberGrapher(**kwargs):
  mod = cms.EDAnalyzer('EcalBxOrbitNumberGrapher',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
