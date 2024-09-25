import FWCore.ParameterSet.Config as cms

def HLTPathSelector(*args, **kwargs):
  mod = cms.EDFilter('HLTPathSelector',
    verbose = cms.untracked.bool(False),
    processName = cms.string(''),
    hltPathsOfInterest = cms.vstring(),
    triggerResults = cms.untracked.InputTag('TriggerResults', '', 'HLT'),
    triggerEvent = cms.untracked.InputTag('hltTriggerSummaryAOD', '', 'HLT'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
