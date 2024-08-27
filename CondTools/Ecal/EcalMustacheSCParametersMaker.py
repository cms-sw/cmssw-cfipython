import FWCore.ParameterSet.Config as cms

def EcalMustacheSCParametersMaker(**kwargs):
  mod = cms.EDAnalyzer('EcalMustacheSCParametersMaker',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
