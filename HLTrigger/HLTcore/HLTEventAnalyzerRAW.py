import FWCore.ParameterSet.Config as cms

def HLTEventAnalyzerRAW(*args, **kwargs):
  mod = cms.EDAnalyzer('HLTEventAnalyzerRAW',
    processName = cms.string('HLT'),
    triggerName = cms.string('@'),
    triggerResults = cms.InputTag('TriggerResults', '', 'HLT'),
    triggerEventWithRefs = cms.InputTag('hltTriggerSummaryRAW', '', 'HLT'),
    verbose = cms.bool(False),
    permissive = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
