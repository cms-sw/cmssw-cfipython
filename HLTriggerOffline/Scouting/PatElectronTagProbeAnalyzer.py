import FWCore.ParameterSet.Config as cms

def PatElectronTagProbeAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('PatElectronTagProbeAnalyzer',
    OutputInternalPath = cms.string('MY_FOLDER'),
    TriggerResultTag = cms.InputTag('TriggerResults', '', 'HLT'),
    TriggerObjects = cms.InputTag('slimmedPatTrigger'),
    ElectronCollection = cms.InputTag('slimmedElectrons'),
    ScoutingElectronCollection = cms.InputTag('Run3ScoutingElectrons'),
    eleIdMapTight = cms.InputTag('egmGsfElectronIDs', 'cutBasedElectronID-RunIIIWinter22-V1-tight'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
