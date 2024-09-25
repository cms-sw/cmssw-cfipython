import FWCore.ParameterSet.Config as cms

def EcalObjectAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalObjectAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
