import FWCore.ParameterSet.Config as cms

def EcalDBCopy(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalDBCopy',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
