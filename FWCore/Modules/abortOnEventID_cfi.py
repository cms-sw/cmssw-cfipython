import FWCore.ParameterSet.Config as cms

abortOnEventID = cms.EDAnalyzer('AbortOnEventIDAnalyzer',
  throwExceptionInsteadOfAbort = cms.untracked.bool(False)
)
