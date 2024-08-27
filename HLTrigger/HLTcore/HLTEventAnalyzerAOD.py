import FWCore.ParameterSet.Config as cms

def HLTEventAnalyzerAOD(**kwargs):
  mod = cms.EDAnalyzer('HLTEventAnalyzerAOD',
    processName = cms.string('HLT'),
    triggerName = cms.string('@'),
    triggerResults = cms.InputTag('TriggerResults', '', 'HLT'),
    triggerEvent = cms.InputTag('hltTriggerSummaryAOD', '', 'HLT'),
    stageL1Trigger = cms.uint32(1),
    verbose = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
