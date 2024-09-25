import FWCore.ParameterSet.Config as cms

def AbortOnEventIDAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('AbortOnEventIDAnalyzer',
    eventsToAbort = cms.required.untracked.VEventID,
    throwExceptionInsteadOfAbort = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
