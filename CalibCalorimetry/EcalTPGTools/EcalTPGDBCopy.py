import FWCore.ParameterSet.Config as cms

def EcalTPGDBCopy(**kwargs):
  mod = cms.EDAnalyzer('EcalTPGDBCopy',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
