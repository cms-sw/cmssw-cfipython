import FWCore.ParameterSet.Config as cms

def DetIdSelectorTest(**kwargs):
  mod = cms.EDAnalyzer('DetIdSelectorTest',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
