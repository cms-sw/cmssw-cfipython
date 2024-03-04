import FWCore.ParameterSet.Config as cms

def L1TStage1Layer2Producer(**kwargs):
  mod = cms.EDProducer('L1TStage1Layer2Producer',
    CaloRegions = cms.required.InputTag,
    CaloEmCands = cms.required.InputTag,
    conditionsLabel = cms.required.string,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
