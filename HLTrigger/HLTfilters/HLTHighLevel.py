import FWCore.ParameterSet.Config as cms

def HLTHighLevel(**kwargs):
  mod = cms.EDFilter('HLTHighLevel',
    TriggerResultsTag = cms.InputTag('TriggerResults', '', 'HLT'),
    HLTPaths = cms.vstring(),
    eventSetupPathsKey = cms.string(''),
    eventSetupPathsLabel = cms.string(''),
    andOr = cms.bool(True),
    throw = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
