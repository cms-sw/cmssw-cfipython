import FWCore.ParameterSet.Config as cms

def HLTrigReport(*args, **kwargs):
  mod = cms.EDAnalyzer('HLTrigReport',
    HLTriggerResults = cms.InputTag('TriggerResults', '', 'HLT'),
    reportBy = cms.untracked.string('job'),
    resetBy = cms.untracked.string('never'),
    serviceBy = cms.untracked.string('never'),
    CustomDatasets = cms.untracked.PSet(),
    CustomStreams = cms.untracked.PSet(),
    ReferencePath = cms.untracked.string('HLTriggerFinalPath'),
    ReferenceRate = cms.untracked.double(100),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
