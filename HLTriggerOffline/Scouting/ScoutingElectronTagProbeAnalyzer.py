import FWCore.ParameterSet.Config as cms

def ScoutingElectronTagProbeAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('ScoutingElectronTagProbeAnalyzer',
    OutputInternalPath = cms.string('MY_FOLDER'),
    BaseTriggerSelection = cms.vstring(),
    triggerSelection = cms.vstring(),
    finalfilterSelection = cms.vstring(),
    TriggerResultTag = cms.InputTag('TriggerResults', '', 'HLT'),
    TriggerObjects = cms.InputTag('slimmedPatTrigger'),
    ElectronCollection = cms.InputTag('slimmedElectrons'),
    ScoutingElectronCollection = cms.InputTag('Run3ScoutingElectrons'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
