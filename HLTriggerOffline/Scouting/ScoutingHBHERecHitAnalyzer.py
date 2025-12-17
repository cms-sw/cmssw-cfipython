import FWCore.ParameterSet.Config as cms

def ScoutingHBHERecHitAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('ScoutingHBHERecHitAnalyzer',
    src = cms.required.InputTag,
    topFolderName = cms.string('HLT/ScoutingOffline/CaloRecHits'),
    L1TriggerResults = cms.InputTag('l1bits'),
    HLTTriggerResults = cms.InputTag('TriggerResults', '', 'HLT'),
    lazy_eval = cms.untracked.bool(False),
    cut = cms.string(''),
    triggers = cms.VPSet(
      cms.PSet(
        expr = cms.vstring('DST_PFScouting_JetHT'),
        name = cms.string('')
      ),
      template = cms.PSetTemplate(
        name = cms.string(''),
        expr = cms.required.vstring
      )
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
