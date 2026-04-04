import FWCore.ParameterSet.Config as cms

def EcalTPGDBCopy(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalTPGDBCopy',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
