import FWCore.ParameterSet.Config as cms

def CSCSharesInputTest(**kwargs):
  mod = cms.EDAnalyzer('CSCSharesInputTest',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
