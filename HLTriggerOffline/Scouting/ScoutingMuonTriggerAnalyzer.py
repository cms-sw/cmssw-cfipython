import FWCore.ParameterSet.Config as cms

def ScoutingMuonTriggerAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('ScoutingMuonTriggerAnalyzer',
    OutputInternalPath = cms.string('MY_FOLDER'),
    triggerSelection = cms.vstring(),
    ScoutingMuonCollection = cms.InputTag('hltScoutingMuonPackerVtx'),
    AlgInputTag = cms.InputTag('gtStage2Digis'),
    l1Seeds = cms.vstring(),
    l1tAlgBlkInputTag = cms.InputTag('gtStage2Digis'),
    l1tExtBlkInputTag = cms.InputTag('gtStage2Digis'),
    ReadPrescalesFromFile = cms.bool(False),
    triggerConfiguration = cms.PSet(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
