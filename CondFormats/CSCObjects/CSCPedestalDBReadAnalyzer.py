import FWCore.ParameterSet.Config as cms

def CSCPedestalDBReadAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCPedestalDBReadAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
