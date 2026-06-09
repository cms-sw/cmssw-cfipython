import FWCore.ParameterSet.Config as cms

def ScoutingMuonTriggerAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('ScoutingMuonTriggerAnalyzer',
    OutputInternalPath = cms.string('MY_FOLDER'),
    triggerSelection = cms.vstring(),
    hltProcessName = cms.string(''),
    special_HLT_Menus = cms.vstring(),
    ScoutingMuonCollection = cms.InputTag('hltScoutingMuonPackerVtx'),
    AlgInputTag = cms.InputTag('gtStage2Digis'),
    l1Seeds = cms.vstring(),
    l1tAlgBlkInputTag = cms.InputTag('gtStage2Digis'),
    l1tExtBlkInputTag = cms.InputTag('gtStage2Digis'),
    ReadPrescalesFromFile = cms.bool(False),
    muonSelection = cms.string(''),
    triggerConfiguration = cms.PSet(
      hltResults = cms.InputTag('TriggerResults', '', 'HLT'),
      l1tResults = cms.InputTag(''),
      l1tIgnoreMaskAndPrescale = cms.bool(False),
      throw = cms.bool(True),
      usePathStatus = cms.bool(False)
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
