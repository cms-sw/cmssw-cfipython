import FWCore.ParameterSet.Config as cms

def EcalTrivialObjectAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalTrivialObjectAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
