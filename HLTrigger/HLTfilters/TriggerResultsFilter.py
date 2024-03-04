import FWCore.ParameterSet.Config as cms

def TriggerResultsFilter(**kwargs):
  mod = cms.EDFilter('TriggerResultsFilter',
    usePathStatus = cms.bool(False),
    hltResults = cms.InputTag('TriggerResults', '', '@skipCurrentProcess'),
    l1tResults = cms.InputTag('hltGtStage2Digis'),
    l1tIgnoreMaskAndPrescale = cms.bool(False),
    throw = cms.bool(True),
    triggerConditions = cms.vstring('HLT_*'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
