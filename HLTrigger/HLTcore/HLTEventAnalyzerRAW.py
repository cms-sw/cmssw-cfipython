import FWCore.ParameterSet.Config as cms

def HLTEventAnalyzerRAW(**kwargs):
  mod = cms.EDAnalyzer('HLTEventAnalyzerRAW',
    processName = cms.string('HLT'),
    triggerName = cms.string('@'),
    triggerResults = cms.InputTag('TriggerResults', '', 'HLT'),
    triggerEventWithRefs = cms.InputTag('hltTriggerSummaryRAW', '', 'HLT'),
    verbose = cms.bool(False),
    permissive = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
