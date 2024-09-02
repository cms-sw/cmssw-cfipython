import FWCore.ParameterSet.Config as cms

def L1TCaloLayer1Summary(**kwargs):
  mod = cms.EDProducer('L1TCaloLayer1Summary',
    caloLayer1CICADAScore = cms.InputTag('caloLayer1Digis', 'CICADAScore'),
    gtCICADAScore = cms.InputTag('gtTestcrateStage2Digis', 'CICADAScore'),
    simCICADAScore = cms.InputTag('simCaloStage2Layer1Summary', 'CICADAScore'),
    caloLayer1Regions = cms.InputTag('caloLayer1Digis'),
    simRegions = cms.InputTag('simCaloStage2Layer1Digis'),
    fedRawDataLabel = cms.InputTag('rawDataCollector'),
    histFolder = cms.string('L1T/L1TCaloLayer1Summary'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
