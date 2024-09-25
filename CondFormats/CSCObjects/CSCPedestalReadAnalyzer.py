import FWCore.ParameterSet.Config as cms

def CSCPedestalReadAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCPedestalReadAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
