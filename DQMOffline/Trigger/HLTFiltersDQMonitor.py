import FWCore.ParameterSet.Config as cms

def HLTFiltersDQMonitor(*args, **kwargs):
  mod = cms.EDProducer('HLTFiltersDQMonitor',
    folderName = cms.string('HLT/Filters'),
    efficPlotNamePrefix = cms.string('effic_'),
    triggerResults = cms.InputTag('TriggerResults', '', 'HLT'),
    triggerEvent = cms.InputTag('hltTriggerSummaryAOD', '', 'HLT'),
    triggerEventWithRefs = cms.InputTag('hltTriggerSummaryRAW', '', 'HLT'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
