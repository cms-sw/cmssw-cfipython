import FWCore.ParameterSet.Config as cms

def EcalTBHodoscopeRawInfoDumper(**kwargs):
  mod = cms.EDAnalyzer('EcalTBHodoscopeRawInfoDumper',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
