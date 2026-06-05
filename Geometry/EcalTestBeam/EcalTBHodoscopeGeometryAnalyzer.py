import FWCore.ParameterSet.Config as cms

def EcalTBHodoscopeGeometryAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalTBHodoscopeGeometryAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
