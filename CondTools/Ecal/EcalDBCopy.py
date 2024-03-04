import FWCore.ParameterSet.Config as cms

def EcalDBCopy(**kwargs):
  mod = cms.EDAnalyzer('EcalDBCopy',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
