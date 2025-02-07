import FWCore.ParameterSet.Config as cms

def TriggerSummaryAnalyzerAOD(*args, **kwargs):
  mod = cms.EDAnalyzer('TriggerSummaryAnalyzerAOD',
    inputTag = cms.InputTag('hltTriggerSummaryAOD'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
