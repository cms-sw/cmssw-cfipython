import FWCore.ParameterSet.Config as cms

def HLTHighLevel(*args, **kwargs):
  mod = cms.EDFilter('HLTHighLevel',
    TriggerResultsTag = cms.InputTag('TriggerResults', '', 'HLT'),
    HLTPaths = cms.vstring(),
    eventSetupPathsKey = cms.string(''),
    eventSetupPathsLabel = cms.string(''),
    andOr = cms.bool(True),
    throw = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
