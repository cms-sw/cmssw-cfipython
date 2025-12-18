import FWCore.ParameterSet.Config as cms

def ScoutingEGammaCollectionMonitoring(*args, **kwargs):
  mod = cms.EDProducer('ScoutingEGammaCollectionMonitoring',
    OutputInternalPath = cms.string('MY_FOLDER'),
    triggerSelection = cms.vstring(),
    AlgInputTag = cms.InputTag('gtStage2Digis'),
    l1tAlgBlkInputTag = cms.InputTag('gtStage2Digis'),
    l1tExtBlkInputTag = cms.InputTag('gtStage2Digis'),
    ReadPrescalesFromFile = cms.bool(False),
    L1Seeds = cms.vstring(),
    TriggerResultTag = cms.InputTag('TriggerResults', '', 'HLT'),
    ElectronCollection = cms.InputTag('slimmedElectrons'),
    ScoutingElectronCollection = cms.InputTag('hltScoutingEgammaPacker'),
    eleIdMapTight = cms.InputTag('egmGsfElectronIDs', 'cutBasedElectronID-RunIIIWinter22-V1-tight'),
    useOfflineObject = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
