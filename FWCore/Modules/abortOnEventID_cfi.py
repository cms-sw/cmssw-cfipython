import FWCore.ParameterSet.Config as cms

abortOnEventID = cms.EDAnalyzer('AbortOnEventIDAnalyzer',
  eventsToAbort = cms.required.untracked.VEventID,
  throwExceptionInsteadOfAbort = cms.untracked.bool(False),
  mightGet = cms.optional.untracked.vstring
)
