import FWCore.ParameterSet.Config as cms

def TestPerformanceFW_ES_TFormula(**kwargs):
  mod = cms.EDAnalyzer('TestPerformanceFW_ES_TFormula',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
