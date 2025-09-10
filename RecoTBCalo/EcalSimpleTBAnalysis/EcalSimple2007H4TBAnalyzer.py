import FWCore.ParameterSet.Config as cms

def EcalSimple2007H4TBAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalSimple2007H4TBAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
