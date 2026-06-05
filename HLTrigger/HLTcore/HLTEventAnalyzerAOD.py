import FWCore.ParameterSet.Config as cms

def HLTEventAnalyzerAOD(*args, **kwargs):
  mod = cms.EDAnalyzer('HLTEventAnalyzerAOD',
    processName = cms.string('HLT'),
    triggerName = cms.string('@'),
    triggerResults = cms.InputTag('TriggerResults', '', 'HLT'),
    triggerEvent = cms.InputTag('hltTriggerSummaryAOD', '', 'HLT'),
    stageL1Trigger = cms.uint32(1),
    verbose = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
