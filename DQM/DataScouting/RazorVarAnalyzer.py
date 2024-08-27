import FWCore.ParameterSet.Config as cms

def RazorVarAnalyzer(**kwargs):
  mod = cms.EDProducer('RazorVarAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
