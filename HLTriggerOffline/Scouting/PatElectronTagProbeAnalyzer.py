import FWCore.ParameterSet.Config as cms

def PatElectronTagProbeAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('PatElectronTagProbeAnalyzer',
    OutputInternalPath = cms.string('MY_FOLDER'),
    BaseTriggerSelection = cms.vstring(),
    triggerConfigs = cms.VPSet(
      template = cms.PSetTemplate(
        pathName = cms.string(''),
        filters = cms.vstring()
      )
    ),
    l1filterSelection = cms.vstring(),
    l1filterSelectionIndex = cms.vuint32(),
    AlgInputTag = cms.InputTag('gtStage2Digis'),
    L1Seeds = cms.vstring(),
    l1tAlgBlkInputTag = cms.InputTag('gtStage2Digis'),
    l1tExtBlkInputTag = cms.InputTag('gtStage2Digis'),
    ReadPrescalesFromFile = cms.bool(False),
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
