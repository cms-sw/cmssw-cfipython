import FWCore.ParameterSet.Config as cms

def TrigObjP4FlatTableProducer(*args, **kwargs):
  mod = cms.EDProducer('TrigObjP4FlatTableProducer',
    triggerEvent = cms.InputTag('hltTriggerSummaryAOD', '', 'HLT'),
    tableName = cms.string('TrigObj'),
    pathNames = cms.vstring(),
    extraFilters = cms.vstring(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
