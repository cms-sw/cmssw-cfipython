import FWCore.ParameterSet.Config as cms

def EcalTimeOffsetConstantAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalTimeOffsetConstantAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
