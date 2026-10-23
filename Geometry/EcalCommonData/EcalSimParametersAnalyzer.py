import FWCore.ParameterSet.Config as cms

def EcalSimParametersAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalSimParametersAnalyzer',
    name = cms.untracked.string('EcalHitsEB'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
