import FWCore.ParameterSet.Config as cms

def ExceptionGenerator(**kwargs):
  mod = cms.EDAnalyzer('ExceptionGenerator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
