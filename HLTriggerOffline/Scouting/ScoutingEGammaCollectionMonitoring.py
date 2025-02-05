import FWCore.ParameterSet.Config as cms

def ScoutingEGammaCollectionMonitoring(*args, **kwargs):
  mod = cms.EDProducer('ScoutingEGammaCollectionMonitoring',
    OutputInternalPath = cms.string('MY_FOLDER'),
    TriggerResultTag = cms.InputTag('TriggerResults', '', 'HLT'),
    ElectronCollection = cms.InputTag('slimmedElectrons'),
    ScoutingElectronCollection = cms.InputTag('hltScoutingEgammaPacker'),
    eleIdMapTight = cms.InputTag('egmGsfElectronIDs', 'cutBasedElectronID-RunIIIWinter22-V1-tight'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
