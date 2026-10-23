import FWCore.ParameterSet.Config as cms

def ExceptionGenerator(*args, **kwargs):
  mod = cms.EDAnalyzer('ExceptionGenerator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
