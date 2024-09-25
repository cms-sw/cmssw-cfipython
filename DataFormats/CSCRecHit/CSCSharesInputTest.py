import FWCore.ParameterSet.Config as cms

def CSCSharesInputTest(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCSharesInputTest',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
