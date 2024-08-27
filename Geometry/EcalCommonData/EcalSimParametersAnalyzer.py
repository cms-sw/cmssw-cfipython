import FWCore.ParameterSet.Config as cms

def EcalSimParametersAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('EcalSimParametersAnalyzer',
    name = cms.untracked.string('EcalHitsEB'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
