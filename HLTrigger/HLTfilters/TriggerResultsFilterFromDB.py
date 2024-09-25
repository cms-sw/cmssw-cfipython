import FWCore.ParameterSet.Config as cms

def TriggerResultsFilterFromDB(*args, **kwargs):
  mod = cms.EDFilter('TriggerResultsFilterFromDB',
    usePathStatus = cms.bool(False),
    hltResults = cms.InputTag('TriggerResults'),
    l1tResults = cms.InputTag('hltGtStage2Digis'),
    l1tIgnoreMaskAndPrescale = cms.bool(False),
    throw = cms.bool(True),
    eventSetupPathsKey = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
