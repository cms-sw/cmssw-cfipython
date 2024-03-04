import FWCore.ParameterSet.Config as cms

def AbortOnEventIDAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('AbortOnEventIDAnalyzer',
    eventsToAbort = cms.required.untracked.VEventID,
    throwExceptionInsteadOfAbort = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
